import env_loader  # noqa: F401
from io import BytesIO

from flask import Flask, jsonify, render_template, request
from PIL import Image

from api_module import search_product
from blip_module import get_caption
from comparison_module import compare_products
from food_context import infer_food_context
from llm_reasoning import ask_llm
from nutrition_knowledge import build_nutrition_profile
from nutrition_parser import parse_nutrition
from ocr_module import extract_text

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
DEFAULT_QUESTION = "Give me a quick summary of this product and whether it seems healthy."


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def load_image(uploaded_file):
    if uploaded_file is None or not uploaded_file.filename:
        raise ValueError("Please upload an image file.")
    if not allowed_file(uploaded_file.filename):
        raise ValueError("Only JPG, JPEG, and PNG files are supported.")

    image_bytes = uploaded_file.read()
    if not image_bytes:
        raise ValueError("The uploaded file is empty.")

    try:
        return Image.open(BytesIO(image_bytes)).convert("RGB")
    except Exception as exc:
        raise ValueError("The uploaded file could not be processed as an image.") from exc


def analyze_image(image, question):
    caption = get_caption(image)
    item_context = infer_food_context(caption)

    ocr_text = ""
    if item_context["should_use_ocr"]:
        ocr_text = extract_text(image)

    final_context = infer_food_context(caption, ocr_text) if ocr_text else item_context

    should_search_api = final_context["should_search_api"]
    if final_context["should_use_ocr"] and not ocr_text:
        ocr_text = extract_text(image)
    if final_context["category"] == "unknown" and ocr_text:
        final_context = infer_food_context(caption, ocr_text)
        should_search_api = final_context["should_search_api"]

    ocr_nutrition = parse_nutrition(ocr_text)
    api_data = search_product(caption, ocr_text=ocr_text, item_context=final_context) if should_search_api else {}
    nutrition_profile = build_nutrition_profile(final_context, ocr_nutrition, api_data, ocr_text=ocr_text, caption=caption)
    final_question = question.strip() or DEFAULT_QUESTION
    answer = ask_llm(final_question, caption, ocr_text, ocr_nutrition, api_data, final_context, nutrition_profile)
    return {
        "question": final_question,
        "caption": caption,
        "item_context": final_context,
        "ocr_text": ocr_text,
        "nutrition": ocr_nutrition,
        "nutrition_profile": nutrition_profile,
        "health_summary": nutrition_profile["summary"],
        "good_points": nutrition_profile["good_points"],
        "bad_points": nutrition_profile["bad_points"],
        "api_data": api_data,
        "answer": answer,
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/analyze")
def analyze_product():
    try:
        image = load_image(request.files.get("image"))
        question = request.form.get("question", "")
        result = analyze_image(image, question)
        return jsonify({"ok": True, "result": result})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except Exception as exc:
        return jsonify({"ok": False, "error": f"Analysis failed: {exc}"}), 500


@app.post("/api/compare")
def compare_product_images():
    try:
        image_one = load_image(request.files.get("image1"))
        image_two = load_image(request.files.get("image2"))
        product_one = analyze_image(image_one, DEFAULT_QUESTION)
        product_two = analyze_image(image_two, DEFAULT_QUESTION)
        comparison = compare_products(
            {
                "caption": product_one["caption"],
                "item_context": product_one["item_context"],
                "nutrition_profile": product_one["nutrition_profile"],
                "nutrition": product_one["nutrition"],
                "ocr": product_one["ocr_text"],
                "api": product_one["api_data"],
            },
            {
                "caption": product_two["caption"],
                "item_context": product_two["item_context"],
                "nutrition_profile": product_two["nutrition_profile"],
                "nutrition": product_two["nutrition"],
                "ocr": product_two["ocr_text"],
                "api": product_two["api_data"],
            },
        )
        return jsonify(
            {
                "ok": True,
                "result": {
                    "product1": product_one,
                    "product2": product_two,
                    "comparison": comparison,
                },
            }
        )
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except Exception as exc:
        return jsonify({"ok": False, "error": f"Comparison failed: {exc}"}), 500


if __name__ == "__main__":
    app.run(debug=True)

# llm_reasoning.py
import env_loader  # noqa: F401
from google import genai
import os

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def _format_number(value):
    if value is None:
        return None
    try:
        num = float(value)
    except Exception:
        return None
    if num.is_integer():
        return str(int(num))
    return f"{num:.1f}"


def _local_answer(question, caption, nutrition, item_context, nutrition_profile=None):
    category = (item_context or {}).get("category", "unknown")
    label = (item_context or {}).get("label", "the item")
    q = question.lower()
    profile = nutrition_profile or {}
    highlights = profile.get("highlights", {})
    summary = profile.get("summary") or ""
    good_points = profile.get("good_points", [])
    bad_points = profile.get("bad_points", [])

    def metric(name):
        value = highlights.get(name)
        formatted = _format_number(value)
        return f"{formatted} per 100g" if formatted is not None else None

    if "calorie" in q or "energy" in q:
        cal = metric("calories")
        if cal:
            return f"{label.title()} has about {cal}. {summary}".strip()

    if "protein" in q:
        protein = metric("protein")
        if protein:
            return f"{label.title()} has about {protein}. {summary}".strip()

    if "sugar" in q:
        sugar = metric("sugar")
        if sugar:
            return f"{label.title()} has about {sugar}. {summary}".strip()

    if "fat" in q:
        fat = metric("fat")
        if fat:
            return f"{label.title()} has about {fat}. {summary}".strip()

    if "fiber" in q or "fibre" in q:
        fiber = metric("fiber")
        if fiber:
            return f"{label.title()} has about {fiber}. {summary}".strip()

    if "sodium" in q or "salt" in q:
        sodium = metric("sodium")
        if sodium:
            return f"{label.title()} has about {sodium}. {summary}".strip()

    if category == "fruit":
        if "healthy" in q or "good" in q:
            return (
                f"This looks like {label}, a fresh fruit. "
                f"{summary} "
                f"Good points: {', '.join(good_points[:2])}. "
                f"Bad points: {', '.join(bad_points[:1])}."
            ).strip()
        return f"This appears to be {label}, a fresh fruit. {summary}".strip()

    if category == "vegetable":
        if "healthy" in q or "good" in q:
            return (
                f"This looks like {label}, a vegetable. "
                f"{summary} "
                f"Good points: {', '.join(good_points[:2])}. "
                f"Bad points: {', '.join(bad_points[:1])}."
            ).strip()
        return f"This appears to be {label}, a vegetable. {summary}".strip()

    if category == "dry_fruits_and_nuts":
        return (
            f"This looks like {label}, which is usually nutrient-dense but calorie-dense. "
            f"{summary} "
            f"Good points: {', '.join(good_points[:2])}. "
            f"Bad points: {', '.join(bad_points[:2])}."
        ).strip()

    if category == "packaged_food" and nutrition:
        return (
            f"This looks like packaged food ({label}). "
            f"{summary} "
            f"Good points: {', '.join(good_points[:2])}. "
            f"Bad points: {', '.join(bad_points[:2])}."
        )

    if category == "packaged_food":
        return f"This looks like packaged food ({label}). {summary}".strip()

    return "I could not generate a confident local answer from the current image."


def ask_llm(question, caption, ocr_text, nutrition, api_data, item_context=None, nutrition_profile=None):
    prompt = f"""
    You are a retail product assistant.

    Image description:
    {caption}

    Detected item context:
    {item_context}

    Nutrition profile:
    {nutrition_profile}

    OCR extracted text:
    {ocr_text}

    Nutrition data:
    {nutrition}

    Product API data:
    {api_data}

    User question:
    {question}

    Give a short, clear and helpful answer.
    """

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return response.text
    except Exception:
        return _local_answer(question, caption, nutrition, item_context, nutrition_profile)

import re


CATEGORY_KEYWORDS = {
    "fruit": {
        "apple",
        "banana",
        "orange",
        "mango",
        "grape",
        "grapes",
        "strawberry",
        "blueberry",
        "blackberry",
        "raspberry",
        "guava",
        "pomegranate",
        "pear",
        "peach",
        "plum",
        "cherry",
        "pineapple",
        "kiwi",
        "melon",
        "watermelon",
        "papaya",
        "chikoo",
        "sapota",
        "custard apple",
        "dragon fruit",
        "muskmelon",
        "sweet lime",
        "lemon",
        "lime",
        "avocado",
        "jackfruit",
        "coconut",
    },
    "vegetable": {
        "carrot",
        "tomato",
        "potato",
        "sweet potato",
        "onion",
        "garlic",
        "cucumber",
        "lettuce",
        "spinach",
        "broccoli",
        "cauliflower",
        "cabbage",
        "pepper",
        "capsicum",
        "chilli",
        "chili",
        "okra",
        "ladyfinger",
        "brinjal",
        "eggplant",
        "pumpkin",
        "bottle gourd",
        "ridge gourd",
        "bitter gourd",
        "zucchini",
        "bean",
        "beans",
        "pea",
        "peas",
        "corn",
        "beetroot",
        "radish",
        "turnip",
        "celery",
        "mushroom",
        "ginger",
        "fenugreek",
        "coriander",
        "parsley",
        "curry leaves",
    },
    "dry_fruits_and_nuts": {
        "almond",
        "almonds",
        "cashew",
        "cashews",
        "pistachio",
        "pistachios",
        "walnut",
        "walnuts",
        "hazelnut",
        "hazelnuts",
        "pecan",
        "pecans",
        "macadamia",
        "brazil nut",
        "peanut",
        "peanuts",
        "raisin",
        "raisins",
        "date",
        "dates",
        "fig",
        "figs",
        "apricot",
        "apricots",
        "prune",
        "prunes",
        "dry fruit",
        "dry fruits",
        "trail mix",
        "nut mix",
        "seed mix",
        "sunflower seeds",
        "pumpkin seeds",
        "flax seeds",
        "chia seeds",
    },
    "packaged_food": {
        "nutrition facts",
        "nutrition information",
        "ingredients",
        "serving size",
        "barcode",
        "pack",
        "packet",
        "box",
        "jar",
        "can",
        "bottle",
        "bag",
        "sachet",
        "carton",
        "nutrition",
        "calories",
        "kcal",
        "protein",
        "sugar",
        "fat",
        "chocolate",
        "choco",
        "cocoa",
        "milk chocolate",
        "dark chocolate",
        "white chocolate",
        "chocolate bar",
        "candy",
        "confectionery",
        "biscuits",
        "cookies",
        "chips",
        "milk",
        "yogurt",
        "juice",
        "cola",
        "soda",
        "soft drink",
        "water",
        "bread",
        "tea",
        "coffee",
        "noodles",
        "pasta",
        "cereal",
        "oats",
        "sauce",
        "ketchup",
        "jam",
        "jelly",
        "spread",
        "muesli",
        "granola",
        "tea",
        "coffee",
        "milk powder",
        "cadbury",
        "dairy milk",
    },
}


def _score_category(text, category_terms):
    score = 0
    matches = []
    for term in category_terms:
        pattern = rf"\b{re.escape(term)}\b"
        if re.search(pattern, text):
            score += 2 if len(term.split()) > 1 else 1
            matches.append(term)
    return score, matches


def infer_food_context(caption, ocr_text=""):
    caption_text = (caption or "").lower()
    ocr_text = (ocr_text or "").lower()

    scored = []
    for category, terms in CATEGORY_KEYWORDS.items():
        caption_score, caption_matches = _score_category(caption_text, terms)
        ocr_score, ocr_matches = _score_category(ocr_text, terms)
        combined_score = caption_score * 2 + ocr_score
        scored.append(
            {
                "category": category,
                "score": combined_score,
                "caption_matches": caption_matches,
                "ocr_matches": ocr_matches,
            }
        )

    scored.sort(key=lambda item: item["score"], reverse=True)
    top = scored[0]

    if top["score"] == 0:
        return {
            "category": "unknown",
            "label": "unknown",
            "confidence": 0.0,
            "should_use_ocr": True,
            "should_search_api": True,
            "summary": "Could not confidently identify the item type.",
        }

    label = top["caption_matches"][0] if top["caption_matches"] else top["ocr_matches"][0]
    family = top["category"]
    readable_family = {
        "fruit": "Fresh fruit",
        "vegetable": "Vegetable",
        "dry_fruits_and_nuts": "Dry fruits and nuts",
        "packaged_food": "Packaged food",
    }.get(family, "Unknown")

    is_fresh_produce = family in {"fruit", "vegetable", "dry_fruits_and_nuts"}
    confidence = min(0.95, 0.45 + (top["score"] / 6.0))

    return {
        "category": family,
        "label": label,
        "confidence": round(confidence, 2),
        "should_use_ocr": not is_fresh_produce,
        "should_search_api": not is_fresh_produce,
        "summary": f"Detected {readable_family.lower()} ({label}).",
    }

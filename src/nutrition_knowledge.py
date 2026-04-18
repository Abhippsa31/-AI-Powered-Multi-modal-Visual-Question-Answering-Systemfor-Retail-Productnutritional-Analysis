def _base_profile(name, category, per_100g, good_points, bad_points, summary):
    return {
        "name": name,
        "category": category,
        "per_100g": per_100g,
        "good_points": good_points,
        "bad_points": bad_points,
        "summary": summary,
    }


LOCAL_PROFILES = [
    _base_profile(
        "apple",
        "fruit",
        {"calories": 52, "protein": 0.3, "carbs": 14.0, "sugar": 10.4, "fat": 0.2, "fiber": 2.4, "sodium": 1},
        ["High in fiber for a fruit", "Low in fat", "Hydrating"],
        ["Contains natural sugar"],
        "Apple is generally a healthy fruit and a good everyday snack.",
    ),
    _base_profile(
        "banana",
        "fruit",
        {"calories": 89, "protein": 1.1, "carbs": 22.8, "sugar": 12.2, "fat": 0.3, "fiber": 2.6, "sodium": 1},
        ["Good source of potassium", "Energy rich", "Low in fat"],
        ["Natural sugar is moderately high"],
        "Banana is a nutritious fruit and useful for quick energy.",
    ),
    _base_profile(
        "orange",
        "fruit",
        {"calories": 47, "protein": 0.9, "carbs": 11.8, "sugar": 9.4, "fat": 0.1, "fiber": 2.4, "sodium": 0},
        ["Rich in vitamin C", "Low in fat"],
        ["Natural sugar"],
        "Orange is a healthy citrus fruit with good vitamin content.",
    ),
    _base_profile(
        "mango",
        "fruit",
        {"calories": 60, "protein": 0.8, "carbs": 15.0, "sugar": 13.7, "fat": 0.4, "fiber": 1.6, "sodium": 1},
        ["Good source of vitamin A", "Contains fiber"],
        ["Higher natural sugar"],
        "Mango is nutritious but sweeter than many other fruits.",
    ),
    _base_profile(
        "guava",
        "fruit",
        {"calories": 68, "protein": 2.6, "carbs": 14.3, "sugar": 8.9, "fat": 1.0, "fiber": 5.4, "sodium": 2},
        ["High fiber", "Good vitamin C", "Better protein for a fruit"],
        ["Some natural sugar"],
        "Guava is a very good fruit choice, especially because of its fiber.",
    ),
    _base_profile(
        "papaya",
        "fruit",
        {"calories": 43, "protein": 0.5, "carbs": 10.8, "sugar": 7.8, "fat": 0.3, "fiber": 1.7, "sodium": 8},
        ["Low calorie", "Contains vitamin C and A"],
        ["Natural sugar"],
        "Papaya is a light and healthy fruit choice.",
    ),
    _base_profile(
        "carrot",
        "vegetable",
        {"calories": 41, "protein": 0.9, "carbs": 9.6, "sugar": 4.7, "fat": 0.2, "fiber": 2.8, "sodium": 69},
        ["Low calorie", "Good fiber", "Contains beta-carotene"],
        ["Small amount of natural sugar"],
        "Carrot is a healthy vegetable and a good low-calorie snack.",
    ),
    _base_profile(
        "tomato",
        "vegetable",
        {"calories": 18, "protein": 0.9, "carbs": 3.9, "sugar": 2.6, "fat": 0.2, "fiber": 1.2, "sodium": 5},
        ["Very low calorie", "Hydrating"],
        ["Low protein"],
        "Tomato is a very light and healthy vegetable.",
    ),
    _base_profile(
        "cucumber",
        "vegetable",
        {"calories": 15, "protein": 0.7, "carbs": 3.6, "sugar": 1.7, "fat": 0.1, "fiber": 0.5, "sodium": 2},
        ["Very low calorie", "Hydrating"],
        ["Low protein and fiber"],
        "Cucumber is a very light and refreshing vegetable.",
    ),
    _base_profile(
        "spinach",
        "vegetable",
        {"calories": 23, "protein": 2.9, "carbs": 3.6, "sugar": 0.4, "fat": 0.4, "fiber": 2.2, "sodium": 79},
        ["High in micronutrients", "Good protein for a vegetable", "Good fiber"],
        ["Sodium can be moderate depending on preparation"],
        "Spinach is a very healthy leafy vegetable.",
    ),
    _base_profile(
        "broccoli",
        "vegetable",
        {"calories": 34, "protein": 2.8, "carbs": 6.6, "sugar": 1.7, "fat": 0.4, "fiber": 2.6, "sodium": 33},
        ["High fiber", "Good protein for a vegetable", "Low calorie"],
        ["Low energy density"],
        "Broccoli is one of the healthiest vegetables.",
    ),
    _base_profile(
        "almond",
        "dry_fruits_and_nuts",
        {"calories": 579, "protein": 21.2, "carbs": 21.6, "sugar": 4.4, "fat": 49.9, "fiber": 12.5, "sodium": 1},
        ["High protein", "Healthy fats", "Good fiber"],
        ["Very calorie dense"],
        "Almonds are nutrient-rich but should be eaten in moderation.",
    ),
    _base_profile(
        "cashew",
        "dry_fruits_and_nuts",
        {"calories": 553, "protein": 18.2, "carbs": 30.2, "sugar": 5.9, "fat": 43.9, "fiber": 3.3, "sodium": 12},
        ["Good protein", "Healthy fats"],
        ["High calories"],
        "Cashews are nutritious but calorie dense.",
    ),
    _base_profile(
        "raisins",
        "dry_fruits_and_nuts",
        {"calories": 299, "protein": 3.1, "carbs": 79.2, "sugar": 59.2, "fat": 0.5, "fiber": 3.7, "sodium": 11},
        ["Some fiber", "Quick energy"],
        ["High sugar"],
        "Raisins are healthy in small portions but high in sugar.",
    ),
    _base_profile(
        "date",
        "dry_fruits_and_nuts",
        {"calories": 282, "protein": 2.5, "carbs": 75.0, "sugar": 63.0, "fat": 0.4, "fiber": 8.0, "sodium": 2},
        ["High fiber", "Natural energy"],
        ["High sugar and calories"],
        "Dates are nutritious but very sweet and calorie dense.",
    ),
    _base_profile(
        "chocolate",
        "packaged_food",
        {"calories": 535, "protein": 7.5, "carbs": 59.0, "sugar": 52.0, "fat": 30.0, "fiber": 3.0, "sodium": 80},
        ["Contains some protein", "Provides quick energy"],
        ["High sugar", "High saturated fat", "Calorie dense"],
        "Chocolate is tasty but should generally be treated as an occasional treat.",
    ),
    _base_profile(
        "chips",
        "packaged_food",
        {"calories": 536, "protein": 6.0, "carbs": 53.0, "sugar": 0.5, "fat": 34.0, "fiber": 4.0, "sodium": 525},
        ["Crunchy snack"],
        ["High fat", "High sodium", "Calorie dense"],
        "Chips are usually not a healthy everyday snack because of fat and sodium.",
    ),
    _base_profile(
        "biscuits",
        "packaged_food",
        {"calories": 480, "protein": 7.0, "carbs": 70.0, "sugar": 24.0, "fat": 20.0, "fiber": 2.0, "sodium": 450},
        ["Quick snack"],
        ["High sugar", "High refined carbs", "Moderate fat"],
        "Biscuits can be convenient, but many are high in sugar and refined flour.",
    ),
    _base_profile(
        "milk",
        "packaged_food",
        {"calories": 42, "protein": 3.4, "carbs": 5.0, "sugar": 5.0, "fat": 1.0, "fiber": 0.0, "sodium": 44},
        ["Good protein", "Contains calcium", "Useful daily beverage"],
        ["Contains lactose natural sugar"],
        "Milk is generally a nutritious drink for most people.",
    ),
    _base_profile(
        "yogurt",
        "packaged_food",
        {"calories": 61, "protein": 3.5, "carbs": 4.7, "sugar": 4.7, "fat": 3.3, "fiber": 0.0, "sodium": 46},
        ["Good protein", "May support digestion"],
        ["Some varieties have added sugar"],
        "Plain yogurt is usually a good food choice, while sweetened versions should be limited.",
    ),
    _base_profile(
        "bread",
        "packaged_food",
        {"calories": 265, "protein": 9.0, "carbs": 49.0, "sugar": 5.0, "fat": 3.2, "fiber": 2.7, "sodium": 491},
        ["Quick source of energy"],
        ["Can be high in sodium", "Often refined carbs"],
        "Bread is a common staple, but whole-grain versions are better.",
    ),
    _base_profile(
        "juice",
        "packaged_food",
        {"calories": 45, "protein": 0.5, "carbs": 11.0, "sugar": 10.0, "fat": 0.2, "fiber": 0.2, "sodium": 4},
        ["Hydrating", "May contain vitamin C"],
        ["Can be high in sugar", "Less fiber than whole fruit"],
        "Juice can be okay sometimes, but whole fruit is usually healthier.",
    ),
    _base_profile(
        "cola",
        "packaged_food",
        {"calories": 42, "protein": 0.0, "carbs": 10.6, "sugar": 10.6, "fat": 0.0, "fiber": 0.0, "sodium": 4},
        ["Quick energy"],
        ["High sugar", "No protein or fiber"],
        "Cola and similar soft drinks are usually not healthy everyday choices.",
    ),
    _base_profile(
        "water",
        "packaged_food",
        {"calories": 0, "protein": 0.0, "carbs": 0.0, "sugar": 0.0, "fat": 0.0, "fiber": 0.0, "sodium": 0},
        ["Hydrating", "No calories"],
        ["No nutrients"],
        "Water is the healthiest drink choice in most cases.",
    ),
]


def _normalize(text):
    return " ".join((text or "").lower().replace("-", " ").replace("/", " ").split())


def _alias_tokens(profile):
    return {_normalize(profile["name"])}


def find_local_profile(text):
    content = _normalize(text)
    best = None
    best_score = 0

    for profile in LOCAL_PROFILES:
        score = 0
        name = _normalize(profile["name"])
        if name and name in content:
            score += 4

        for alias in _alias_tokens(profile):
            if alias in content:
                score += 4

        if score > best_score:
            best_score = score
            best = profile

    return best, best_score


def normalize_nutrients(raw):
    if not raw:
        return {}

    if any(key.endswith("_100g") for key in raw):
        return {
            "calories": raw.get("energy-kcal_100g") or raw.get("energy-kcal") or raw.get("energy_100g"),
            "protein": raw.get("proteins_100g") or raw.get("proteins"),
            "carbs": raw.get("carbohydrates_100g") or raw.get("carbohydrates"),
            "sugar": raw.get("sugars_100g") or raw.get("sugars"),
            "fat": raw.get("fat_100g") or raw.get("fat"),
            "fiber": raw.get("fiber_100g") or raw.get("fiber"),
            "sodium": raw.get("sodium_100g") or raw.get("sodium"),
            "saturated_fat": raw.get("saturated-fat_100g") or raw.get("saturated_fat_100g"),
        }

    return {
        "calories": raw.get("energy") or raw.get("energy_kcal"),
        "protein": raw.get("protein"),
        "carbs": raw.get("carbohydrate"),
        "sugar": raw.get("sugar"),
        "fat": raw.get("fat"),
        "fiber": raw.get("fiber"),
        "sodium": raw.get("sodium"),
        "saturated_fat": raw.get("saturated_fat"),
    }


def merge_nutrients(*sources):
    merged = {}
    for source in sources:
        for key, value in (source or {}).items():
            if value is not None and value != "":
                merged[key] = value
    return merged


def assess_health(nutrients, category):
    calories = float(nutrients.get("calories") or 0)
    protein = float(nutrients.get("protein") or 0)
    sugar = float(nutrients.get("sugar") or 0)
    fat = float(nutrients.get("fat") or 0)
    fiber = float(nutrients.get("fiber") or 0)
    sodium = float(nutrients.get("sodium") or 0)
    sat_fat = float(nutrients.get("saturated_fat") or 0)

    score = 50.0
    if category in {"fruit", "vegetable"}:
        score = 82.0
    elif category == "dry_fruits_and_nuts":
        score = 72.0
    elif category == "packaged_food":
        score = 45.0

    score += min(10, fiber * 2)
    score += min(10, protein * 1.5)
    score -= min(18, sugar * 0.8)
    score -= min(12, sat_fat * 2)
    score -= min(10, sodium / 100)
    score -= min(10, fat / 5)
    score -= min(8, calories / 80)

    if calories < 80 and category in {"fruit", "vegetable"}:
        score += 5

    score = max(0, min(100, score))

    good_points = []
    bad_points = []
    if fiber >= 3:
        good_points.append("Good fiber content")
    if protein >= 5:
        good_points.append("Good protein content")
    if sugar <= 8:
        good_points.append("Lower sugar")
    if category in {"fruit", "vegetable"}:
        good_points.append("Natural whole food")
    if category == "dry_fruits_and_nuts":
        good_points.append("Healthy fats and micronutrients")

    if sugar >= 15:
        bad_points.append("High sugar")
    if sat_fat >= 5:
        bad_points.append("High saturated fat")
    if sodium >= 300:
        bad_points.append("High sodium")
    if calories >= 400:
        bad_points.append("High calories")
    if category == "dry_fruits_and_nuts" and calories >= 300:
        bad_points.append("Portion control needed")

    if not good_points:
        good_points.append("No major concerns from the available values")
    if not bad_points:
        bad_points.append("No major red flags from the available values")

    if score >= 75:
        verdict = "Generally healthy"
    elif score >= 55:
        verdict = "Moderate choice"
    else:
        verdict = "Best in moderation"

    return {
        "health_score": round(score),
        "verdict": verdict,
        "good_points": good_points,
        "bad_points": bad_points,
        "calories": calories or None,
        "protein": protein or None,
        "carbs": float(nutrients.get("carbs") or 0) or None,
        "sugar": sugar or None,
        "fat": fat or None,
        "fiber": fiber or None,
        "sodium": sodium or None,
        "saturated_fat": sat_fat or None,
    }


def build_nutrition_profile(item_context, ocr_nutrition, api_data, ocr_text="", caption=""):
    category = (item_context or {}).get("category", "unknown")
    label = (item_context or {}).get("label", "")
    search_text = " ".join([label, caption or "", ocr_text or "", api_data.get("name", "") if api_data else ""])

    local_profile, score = find_local_profile(search_text)
    local_nutrients = (local_profile or {}).get("per_100g", {})
    api_nutrients = normalize_nutrients((api_data or {}).get("nutrition", {}))
    ocr_normalized = normalize_nutrients(ocr_nutrition)

    per_100g = merge_nutrients(local_nutrients, api_nutrients, ocr_normalized)

    if category in {"fruit", "vegetable", "dry_fruits_and_nuts"} and local_profile:
        profile_name = local_profile["name"]
        summary = local_profile["summary"]
        good_points = local_profile["good_points"][:]
        bad_points = local_profile["bad_points"][:]
    elif category == "packaged_food" and local_profile:
        profile_name = local_profile["name"]
        summary = local_profile["summary"]
        good_points = local_profile["good_points"][:]
        bad_points = local_profile["bad_points"][:]
    else:
        profile_name = label or api_data.get("name") or "unknown"
        summary = "Nutritional details were built from the available image and API signals."
        good_points = []
        bad_points = []

    assessment = assess_health(per_100g, category)
    good_points = list(dict.fromkeys(good_points + assessment["good_points"]))
    bad_points = list(dict.fromkeys(bad_points + assessment["bad_points"]))

    return {
        "name": profile_name,
        "category": category,
        "source": "local_profile" if local_profile else "api_or_ocr",
        "match_score": score,
        "per_100g": per_100g,
        "health_score": assessment["health_score"],
        "verdict": assessment["verdict"],
        "summary": summary,
        "good_points": good_points,
        "bad_points": bad_points,
        "highlights": {
            "calories": assessment["calories"],
            "protein": assessment["protein"],
            "carbs": assessment["carbs"],
            "sugar": assessment["sugar"],
            "fat": assessment["fat"],
            "fiber": assessment["fiber"],
            "sodium": assessment["sodium"],
            "saturated_fat": assessment["saturated_fat"],
        },
    }


def compare_nutrition_profiles(profile1, profile2, item1=None, item2=None):
    name1 = (profile1 or {}).get("name", "item 1")
    name2 = (profile2 or {}).get("name", "item 2")
    score1 = float((profile1 or {}).get("health_score") or 0)
    score2 = float((profile2 or {}).get("health_score") or 0)
    p1 = (profile1 or {}).get("highlights", {})
    p2 = (profile2 or {}).get("highlights", {})

    def safe(v):
        return float(v) if v is not None else None

    cal1, cal2 = safe(p1.get("calories")), safe(p2.get("calories"))
    sugar1, sugar2 = safe(p1.get("sugar")), safe(p2.get("sugar"))
    protein1, protein2 = safe(p1.get("protein")), safe(p2.get("protein"))
    fiber1, fiber2 = safe(p1.get("fiber")), safe(p2.get("fiber"))
    sat1, sat2 = safe(p1.get("saturated_fat")), safe(p2.get("saturated_fat"))
    sodium1, sodium2 = safe(p1.get("sodium")), safe(p2.get("sodium"))

    reasons = []
    if cal1 is not None and cal2 is not None and cal1 != cal2:
        reasons.append(f"{name1.title() if score1 >= score2 else name2.title()} has fewer calories.")
    if sugar1 is not None and sugar2 is not None and sugar1 != sugar2:
        reasons.append(f"{name1.title() if sugar1 < sugar2 else name2.title()} has lower sugar.")
    if protein1 is not None and protein2 is not None and protein1 != protein2:
        reasons.append(f"{name1.title() if protein1 > protein2 else name2.title()} has more protein.")
    if fiber1 is not None and fiber2 is not None and fiber1 != fiber2:
        reasons.append(f"{name1.title() if fiber1 > fiber2 else name2.title()} has more fiber.")
    if sat1 is not None and sat2 is not None and sat1 != sat2:
        reasons.append(f"{name1.title() if sat1 < sat2 else name2.title()} has less saturated fat.")
    if sodium1 is not None and sodium2 is not None and sodium1 != sodium2:
        reasons.append(f"{name1.title() if sodium1 < sodium2 else name2.title()} has less sodium.")

    if score1 > score2 + 5:
        winner = name1
    elif score2 > score1 + 5:
        winner = name2
    else:
        winner = None

    if winner:
        base = f"{winner.title()} looks healthier overall based on the available nutrition profile."
    else:
        base = "Both products look fairly close overall based on the available nutrition profile."

    if reasons:
        base += " " + " ".join(reasons[:4])

    return {
        "winner": winner,
        "summary": base,
        "profile1": profile1,
        "profile2": profile2,
    }

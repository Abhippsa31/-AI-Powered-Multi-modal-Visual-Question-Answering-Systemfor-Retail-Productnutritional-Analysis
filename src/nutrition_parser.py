import re

def parse_nutrition(text):

    nutrients = {}

    patterns = {
        "calories": r"(?:energy|calories?|kcal).*?(\d+\.?\d*)",
        "protein": r"protein.*?(\d+\.?\d*)",
        "carbs": r"(?:carbohydrate|carbs?).*?(\d+\.?\d*)",
        "sugar": r"(?:added\s+sugars?|total\s+sugars?|sugars?).*?(\d+\.?\d*)",
        "fat": r"(?:total\s+fat|fat).*?(\d+\.?\d*)",
        "saturated_fat": r"(?:saturated\s+fat|sat(?:urated)?\.?\s*fat).*?(\d+\.?\d*)",
        "fiber": r"(?:dietary\s+fiber|fiber).*?(\d+\.?\d*)",
        "sodium": r"sodium.*?(\d+\.?\d*)",
        "calcium": r"calcium.*?(\d+\.?\d*)",
        "potassium": r"potassium.*?(\d+\.?\d*)"
    }

    for nutrient, pattern in patterns.items():
        match = re.search(pattern, text.lower())
        if match:
            nutrients[nutrient] = float(match.group(1))

    return nutrients

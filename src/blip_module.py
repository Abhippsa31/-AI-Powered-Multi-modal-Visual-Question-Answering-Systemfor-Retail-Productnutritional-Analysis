from transformers import BlipForConditionalGeneration, BlipProcessor

_processor = None
_model = None


def _load_blip():
    global _processor, _model
    if _processor is None or _model is None:
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
    return _processor, _model


def normalize_caption(text):
    cleaned = " ".join(text.split()).strip()
    if not cleaned:
        return "Product packaging image"

    cleaned = cleaned[0].upper() + cleaned[1:]
    if cleaned.endswith("."):
        return cleaned
    return f"{cleaned}."


def get_caption(image):
    try:
        processor, model = _load_blip()
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        return normalize_caption(processor.decode(out[0], skip_special_tokens=True))
    except Exception:
        return "Product packaging image."

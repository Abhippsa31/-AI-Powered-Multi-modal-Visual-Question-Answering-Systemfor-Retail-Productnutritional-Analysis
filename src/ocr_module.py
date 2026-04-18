from pathlib import Path
import os
import shutil

import cv2
import numpy as np
import pytesseract


def _configure_tesseract():
    env_candidates = [
        os.getenv("TESSERACT_CMD"),
        os.getenv("TESSERACT_PATH"),
    ]
    candidates = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]

    for candidate in env_candidates:
        if candidate and Path(candidate).exists():
            pytesseract.pytesseract.tesseract_cmd = candidate
            return candidate

    system_candidate = shutil.which("tesseract")
    if system_candidate:
        pytesseract.pytesseract.tesseract_cmd = system_candidate
        return system_candidate

    for candidate in candidates:
        if Path(candidate).exists():
            pytesseract.pytesseract.tesseract_cmd = candidate
            return candidate

    return None


TESSERACT_PATH = _configure_tesseract()


def _preprocess_image(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if gray.shape[1] < 1400:
        scale = 1400 / gray.shape[1]
        gray = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    denoised = cv2.fastNlMeansDenoising(gray, None, 18, 7, 21)
    blurred = cv2.GaussianBlur(denoised, (3, 3), 0)
    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11,
    )

    kernel = np.ones((2, 2), np.uint8)
    processed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    return processed


def normalize_ocr_text(text):
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    cleaned = " ".join(lines)
    cleaned = " ".join(cleaned.split())
    return cleaned


def extract_text(image):
    if TESSERACT_PATH is None:
        raise RuntimeError(
            "Tesseract OCR was not found. Install it, add it to PATH, or set TESSERACT_CMD in .env."
        )

    processed = _preprocess_image(image)
    raw_text = pytesseract.image_to_string(processed, config="--psm 6")
    return normalize_ocr_text(raw_text)

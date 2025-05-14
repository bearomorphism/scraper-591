# 🏡 591 Rental Listings Scraper with OCR Analysis

This project automates scraping rental listings from [591租屋網](https://rent.591.com.tw) using Playwright, takes a screenshot, and extracts listing text using Tesseract OCR.

## 🔧 Tools Used

- [Playwright](https://playwright.dev/) – for automating browser and taking a screenshot.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – to extract text from screenshots.
- `pytesseract` – Python wrapper for Tesseract.
- `Pillow` – for image handling in Python.

## 📸 Workflow

1. **Navigate to Listing Page** using Playwright.
2. **Take Full Page Screenshot** of filtered results.
3. **Run OCR** on the screenshot to extract listing text.

## 💻 Prerequisites

### Install uv

We use uv to install the dependencies.

```bash
brew install uv
```

### Install Playwright (runtime only)
```bash
playwright install
```

### Install Tesseract OCR

#### macOS (via Homebrew)
```bash
brew install tesseract
brew install tesseract-lang  # To install Chinese languages
```

#### Windows

- Download from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Add `Tesseract-OCR` path to environment variables

## Run

```bash
uv run main.py
```

## 🛠 Troubleshooting

- **TesseractNotFoundError**: Ensure Tesseract is installed and `tesseract_cmd` is set if needed.
- **Language file error**: Ensure `chi_tra.traineddata` exists in the correct `tessdata` directory.
  - macOS default: `/opt/homebrew/share/tessdata/`

## 📄 License

MIT License

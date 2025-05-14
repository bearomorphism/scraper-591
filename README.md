# 🏡 591 Rental Listings Scraper with OCR Analysis

[ChatGPT discussion thread](https://chatgpt.com/share/6824cc3e-b164-8010-a812-7a775e3995d3)

This project automates scraping rental listings from [591租屋網](https://rent.591.com.tw) using Playwright, takes a screenshot, and extracts listing text using Tesseract OCR.

> ⚠️ **Note:** This site uses obfuscated or dynamically generated HTML content, making it difficult to scrape using static requests. I'm using Playwright to load the page in a headless browser and capture the content. However, developer tools cannot be used directly — opening them triggers client-side scripts that redirect the page back to the previous view. As a result, automated tools like Playwright are necessary to bypass these restrictions and extract the data.
>
> ⚠️ **Warning:** This project is a **work in progress** and the code is not yet optimized.

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

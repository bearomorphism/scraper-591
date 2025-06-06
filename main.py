from playwright.sync_api import sync_playwright

from PIL import Image
import pytesseract
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = (
    r"/opt/homebrew/bin/tesseract"  # Windows path example
)


with sync_playwright() as p:
    data_dir = Path("data")
    print("Launching browser...")
    browser = p.chromium.launch()
    page = browser.new_page()

    # TODO: user can fill in the url with filters
    # we can probably have some config file for the filters
    page.goto(
        "https://rent.591.com.tw/list?region=1&kind=1&layout=4,3&other=pet&price=30000_40000",
        wait_until="networkidle",  # we need this to get the price of the listing
    )
    # TODO: goto next page and take more screenshots

    print("Taking screenshot...")
    page.screenshot(path=data_dir / "listing.png", full_page=True)
    browser.close()
    print("Browser closed")

    print("Processing...")
    img = Image.open(data_dir / "listing.png")
    text = pytesseract.image_to_string(img, lang="chi_tra")  # For Traditional Chinese
    with open(data_dir / "listing.txt", "w") as f:
        f.write(text)

    # TODO: what should we do with the text?
    # TODO: data cleaning
    print("Done")

# 📄 phonenums-melodyofasong

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

A lightweight Streamlit app that pulls Indian phone numbers out of any blob of text and hands you back a clean CSV. That's pretty much it — but it does it really well (~99% accuracy).

---

## What's it for?

Got a wall of text with phone numbers scattered throughout? Paste it in, hit extract, download your CSV. Whether it's customer data, scraped content, form responses, or anything else — this saves you the headache of hunting them down manually.

Built specifically for **Indian phone numbers** (think `+91`, `98201 23456`, `22 1234 5678`, `7865043210` — all the usual formats).

---

## Features

- **Paste raw text** directly into the app
- **Upload a `.txt` file** if your text is too long to paste
- **Try Sample Data** — load a pre-built dummy contact directory to see the app in action before using your own input
- **Phone type detection** — results include whether each number is a mobile, landline, or unknown type
- **Preview** extracted numbers before downloading
- **Download as CSV** — ready to plug into whatever workflow you've got
- **Keyboard shortcut** — hit `Enter` to extract without reaching for the mouse
- **Live status updates** — see extraction progress and a count of numbers found on completion
- **Empty input detection** — warns you immediately if there's nothing to extract from
- **Download confirmation** — a toast notification confirms when your CSV has been saved
- **PayWithChai integration** — a small tip widget in the sidebar and footer if you find the tool useful
- Works with text in **any language**, as long as the phone numbers are in Latin script
- No character limit on input... for now (a 25,000 character cap is coming in a future update)

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/melodyofasong/phonenums-melodyofasong
cd phonenums-melodyofasong
pip install -r requirements.txt
```

### Running the app

```bash
streamlit run Homepage.py
```

That's it. The app will open in your browser.

---

## How to Use

1. Open the app
2. Choose your input method from the tabs — **Try Sample Data** to see a demo, **Paste Text** to type/paste directly, or **Upload File** for a `.txt` file
3. Click **Extract Numbers** (or press `Enter`)
4. Watch the live status update as numbers are found
5. Preview your results, then hit **Download as CSV**

> **Deployed on the cloud?** Yep! You can use the app directly without installing anything at: **[https://phonenums-melodyofasong.streamlit.app/](https://phonenums-melodyofasong.streamlit.app/)**

If you're not sure what to expect, just hit the **Try Sample Data** tab — it loads a fake contact directory so you can see the output format right away.

---

## Output Format

The downloaded CSV includes two columns:

| Column | Description |
|--------|-------------|
| `Phone Number` | Formatted in international format (e.g. `+91 98201 23456`) |
| `Type` | `mobile`, `landline`, or `unknown` |

---

## Project Structure

```
├── Homepage.py          # Main Streamlit app
├── pages/
│   ├── 3-Free Access.py # Free phone number access page (WIP)
│   └── 4-About.py       # About page
└── utils/
    ├── extracter.py     # Core phone number extraction logic
    ├── paywithchai.py   # PayWithChai sidebar & footer donation widget
    └── sample_text.py   # Sample data generator (uses Faker)
```

---

## Supported File Types

| Format | Status |
|--------|--------|
| `.txt` | ✅ Supported |
| `.csv` | 🔜 Coming soon |
| `.docx` | 🔜 Coming soon |
| `.pdf` | 🔜 Coming soon |
| `.html` | 🔜 Coming soon |
| `.md` | 🔜 Coming soon |

---

## Got images with phone numbers?

This app works on text, so if your numbers are stuck inside an image, you'll need to OCR it first. A few solid options:

- [OCR.best](https://ocr.best) — quick and free
- [Google Cloud Vision](https://cloud.google.com/vision) — powerful, great for bulk
- [Adobe Acrobat OCR](https://www.adobe.com/acrobat/online/pdf-to-word.html) — good for PDFs with embedded images

Once you've got the text out, paste it straight into the app.

---

## Built With

- [Streamlit](https://streamlit.io/) — UI framework
- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) — phone number parsing library
- [Faker](https://faker.readthedocs.io/) — sample data generation

---

## Roadmap

- [ ] 25,000 character limit on raw text input
- [ ] Support for `.csv`, `.docx`, `.pdf`, `.html`, `.md` uploads
- [ ] Web scraping support
- [ ] Free access to 1000 phone numbers (city-wise)
- [ ] Become your one-stop shop for anything phone-number-related 🫡

---

## Contributing

PRs and issues are welcome! Find the repo on GitHub: [melodyofasong](https://github.com/melodyofasong/phonenums-melodyofasong)

---

## License

This project is licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

You're free to use, share, and adapt this project — just give credit and don't use it for commercial purposes.

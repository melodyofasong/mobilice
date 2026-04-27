import streamlit as st
from utils.paywithchai import paywithchai_sidebar, paywithchai_footer

with st.sidebar:
    paywithchai_sidebar()

st.markdown("""
# About Us

Find this repo on GitHub: [phonenums-melodyofasong](https://github.com/melodyofasong/phonenums-melodyofasong)

A Python project built with **Streamlit** and the **phonenumbers** library to extract phone numbers from large bodies of text, built exclusively for **Indian phone numbers** with **99% accuracy**.

## What it does

Paste or upload a text document and get back a clean, ready-to-use **CSV file** of all the phone numbers found — including whether each number is a **mobile**, **landline**, or **unknown** type. Perfect for plugging straight into your workflow.

## How to use it

Choose your input method from the tabs on the main page:

- **Try Sample Data** — loads a pre-built dummy contact directory so you can see the app in action right away
- **Paste Text** — copy-paste your text directly into the textbox
- **Upload File** — upload a `.txt` file

Press **Extract Numbers** or hit `Enter` on your keyboard and you're done.

Your text can be in **any language**, as long as the phone numbers are written in **Latin script**.

> **Note:** There is currently no character limit on the raw text input, paste as much as you like. A **25,000 character limit** will be introduced in a future update.

## Output format

Results are shown in a preview table with two columns — the phone number in international format, and its type (mobile, landline, or unknown). You can download this as a CSV with one click, and a confirmation will appear when the file is saved.

## Supported file types

Currently supported: `.txt`

Coming soon: `.csv`, `.docx`, `.pdf`, `.html`, `.md`

We're working on becoming your **one-stop shop for anything phone number-related**, including web scraping support and free access to city-wise phone number datasets.

## Got images with text?

If your phone numbers are buried in an image, run it through an OCR tool first and then paste the extracted text here. Some good options:

- [OCR.best](https://ocr.best)
- [Google Cloud Vision](https://cloud.google.com/vision)
- [Adobe Acrobat OCR](https://www.adobe.com/acrobat/online/pdf-to-word.html)

## Support the project

If this tool saved you some time, consider buying a chai ☕ — the tip widget is right there in the sidebar. It helps keep this free and running.

## About the developer

Built and maintained by a 16-year-old self-taught developer from India. This is a solo project, so feedback and contributions are genuinely appreciated — find the repo on GitHub and open an issue or PR anytime.

""")

paywithchai_footer()
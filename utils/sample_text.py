import streamlit as st
from faker import Faker
import random

def generate_sample_text() -> str:
    fake = Faker('en_IN')
    random.seed(42) 

    faker_lines = []
    for _ in range(8):
        name = fake.name()
        phone = fake.phone_number()
        company = fake.company()
        city = fake.city()
        templates = [
            f"Contact {name} from {company} at {phone}.",
            f"{name} ({city}) — Reach out on {phone}.",
            f"For inquiries, call {name}: {phone}",
            f"{company} representative {name} is available at {phone}.",
        ]
        faker_lines.append(random.choice(templates))

    manual_lines = [
        "Call our support desk at 9876543210 between 9am–6pm.",
        "WhatsApp only: +919845012345 (no calls please)",
        "Landline (Chennai office): 044-27654321",
        "Mumbai HQ: (022) 4567-8901 | Pune branch: 020-66123456",
        "Toll-free: 1800-103-4567 (BSNL subscribers dial 1800 180 1234)",
        "Mr. Arjun's direct line is 98765-43210, ask for ext. 42.",
        "Emergency contact: +91 73456 89012",
        "Old format still in use: 0124-4567890",
    ]

    all_lines = faker_lines + manual_lines
    random.shuffle(all_lines)

    intro = (
        "CLIENT CONTACT DIRECTORY — Q2 2024\n"
        "====================================\n"
        "The following records were exported from our CRM. "
        "Please extract and verify all phone numbers before outreach.\n\n"
    )

    body = "\n".join(all_lines)

    footer = (
        "\n\nFor internal queries contact admin@example.in "
        "or call 011-23456789. Last updated by Priya Menon (+91 98234 00156)."
    )

    return intro + body + footer


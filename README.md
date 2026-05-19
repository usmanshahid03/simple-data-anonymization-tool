# Data Anonymizer

A simple utility to anonymize sensitive personal data using two techniques:

- **Generalization** – Converts exact values into broader categories (e.g. age 25 → "20-30", zip 98101 → "981")
- **Suppression** – Replaces sensitive fields with "*" (e.g. medical diagnoses)

## Usage

Run the script directly to see a sample anonymization on a demo dataset:

    python data_anonymizer.py

## Supported Columns

| Column    | Method          | Output Example |
|-----------|-----------------|----------------|
| Age       | Generalization  | "20-30"        |
| Zip Code  | Generalization  | "981"          |
| Diagnosis | Suppression     | "*"            |

## Requirements

    pip install pandas numpy

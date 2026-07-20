# Execution example

This example illustrates the intended public workflow using synthetic documents only.

## Environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Add development AWS credentials to `.env` or use an approved AWS credential provider.

## Start the application

```powershell
python app.py
```

The current public repository does not yet include the complete runnable application. A later phase will add a reconstructed demo entry point and synthetic form.

## Illustrative processing log

```text
Found 3 supported documents
Processing: synthetic_membership_form_001.pdf
Converting PDF page 1 to image
Submitting page to Amazon Textract
Detected 24 key-value candidates and 6 selection elements
Calculated layout adjustment: x=4.2 px, y=-2.1 px
Associated 27 configured fields
Applied cleaning and validation rules
Flagged 2 fields for manual review
Saved synthetic validation report
Processing completed
```

## Illustrative structured result

| field | extracted value | confidence | status |
| --- | --- | ---: | --- |
| document_type | Membership form | 99.1 | Valid |
| applicant_name | Sample User | 97.8 | Valid |
| application_date | 2026-07-20 | 95.4 | Normalized |
| city | Bogotá | 91.2 | Validated against synthetic list |
| phone | 3000000000 | 83.7 | Manual review |

## Expected outputs

```text
output/
├── extracted_records.xlsx
├── validation_report.xlsx
└── final_export.txt
```

These names and values are illustrative. No production schema or customer information is included.

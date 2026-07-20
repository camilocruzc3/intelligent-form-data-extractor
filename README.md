# Intelligent Form Data Extractor

Public portfolio case study of an Intelligent Document Processing (IDP) application that extracts, structures, validates and exports data from scanned forms using Python, Amazon Textract and configurable business rules.

> **Repository status:** this public version documents the architecture, workflow and selected reusable concepts from a private working implementation. It does not publish confidential forms, customer data, production rules or the complete private source code.

## What this project demonstrates

- Batch processing of PDF files and document images.
- PDF-to-image conversion for page-level analysis.
- Form understanding with Amazon Textract `AnalyzeDocument` and the `FORMS` feature.
- Extraction of key-value pairs, selection elements, coordinates and confidence values.
- Spatial field association using reference coordinates and dynamic tolerance.
- Data cleaning and normalization for dates, locations, telephone numbers and adjacent OCR noise.
- Configurable validation rules supported by master lists.
- Transformation from vertical extraction results to review-friendly horizontal records.
- Human-in-the-loop review through a Windows desktop interface.
- Export to Excel reports and configurable flat files.

## Problem

Organizations frequently receive forms as scanned PDFs or images. Manually transcribing these documents is slow, difficult to audit and prone to errors. Basic OCR can recover text, but it does not automatically guarantee that values are associated with the correct fields, normalized or compliant with downstream data rules.

This project addresses the complete processing workflow: extraction, spatial association, data quality controls, human review and structured export.

## Processing workflow

```text
PDF files and document images
              |
              v
File validation and PDF-to-image conversion
              |
              v
Amazon Textract form analysis
              |
              v
Key-value, checkbox, geometry and confidence parsing
              |
              v
Coordinate alignment and dynamic tolerance
              |
              v
Cleaning, normalization and configurable validations
              |
              v
Human review in the desktop application
              |
              v
Excel reports and flat-file export
```

See [`docs/architecture.md`](docs/architecture.md) and [`docs/processing-workflow.md`](docs/processing-workflow.md) for more detail.

## Core capabilities

### Document extraction

The application processes PDF, PNG, JPG, JPEG, TIFF and TIF files. PDF pages are converted to images before being submitted to Amazon Textract for form analysis.

### Spatial association

Extracted fields preserve document geometry. Reference coordinates and a dynamic tolerance mechanism are used to compensate for small layout shifts between form versions and associate values with the expected business fields.

### Data quality

The pipeline applies cleaning and validation rules such as:

- Removal of contaminating adjacent words.
- Reconstruction and normalization of fragmented dates.
- Standardization of common field formats.
- Validation against configurable master lists.
- Identification of records that require manual review.

### Human review and export

A desktop interface allows users to inspect extracted records, correct values, apply validations and generate the final structured output.

## Technology stack

Python, Amazon Textract, boto3, pandas, NumPy, OpenCV, Pillow, pdf2image, Poppler, openpyxl, python-dotenv, Tkinter and ttkbootstrap.

## Public repository structure

```text
docs/                       Architecture and portfolio documentation
assets/screenshots/         Sanitized application screenshots
sample_data/                Synthetic-data guidance only
.env.example                Safe configuration template
.gitignore                  Protection for credentials and operational data
requirements.txt            Minimal public dependency list
```

## Documentation

- [`Case study`](docs/case-study.md)
- [`Architecture`](docs/architecture.md)
- [`Processing workflow`](docs/processing-workflow.md)
- [`Technical decisions`](docs/technical-decisions.md)
- [`Execution example`](docs/execution-example.md)
- [`Security and privacy`](docs/security.md)
- [`Current limitations`](docs/limitations.md)
- [`Roadmap`](docs/roadmap.md)

## Application preview

Sanitized screenshots will be added to `assets/screenshots/`. Real forms, personal information, internal paths and production outputs will not be published.

## Security and privacy

This repository intentionally excludes:

- Real forms and document images.
- Personal, financial or customer information.
- AWS credentials and access-key files.
- Production validation catalogs and coordinate maps.
- Generated Excel reports and flat files.
- Logs, temporary images and packaged binaries.
- Client-specific rules and the private repository history.

See [`docs/security.md`](docs/security.md).

## Portfolio context

The original implementation was developed as a desktop automation solution for structured form processing. This repository presents the engineering approach without exposing confidential information or contractual assets.

## License

MIT License.
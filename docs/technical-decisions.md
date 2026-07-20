# Technical decisions

## Amazon Textract

Amazon Textract was selected to extract form key-value pairs and selection elements without training a custom OCR model.

**Benefits**

- Managed document-analysis service.
- Native form analysis.
- Confidence and geometry metadata.
- Simple Python integration with boto3.

**Trade-offs**

- External-service dependency and usage cost.
- Sensitive-document governance must be evaluated before processing.
- Extraction quality still depends on document resolution and layout.

## Coordinate-aware field association

The application does not rely only on recognized labels. It also uses field coordinates and a configurable reference layout.

A dynamic tolerance is calculated from anchor fields to compensate for small shifts between document scans or form versions. This makes the assignment process more resilient than fixed pixel matching.

## Configurable validation rules

Master lists and rule files are kept outside the core extraction logic where practical. This allows data-quality rules to evolve without rewriting the full application.

## pandas and Excel

pandas and openpyxl support cleaning, validation, reshaping, reporting and integration with spreadsheet-based configuration used by operational teams.

## Desktop interface

A local desktop interface was appropriate for a controlled Windows workflow where users select folders, monitor batch progress, review extracted records and generate final files.

## Human-in-the-loop review

OCR output is treated as a candidate result rather than unquestioned truth. Confidence, validation findings and editable records support manual verification before downstream delivery.

## Public reconstruction strategy

The public version documents generic engineering decisions and selected reusable logic. It intentionally excludes customer names, field catalogs, real forms, production output structures and private operational rules.

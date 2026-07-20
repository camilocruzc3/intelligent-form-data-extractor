# Processing workflow

## 1. Input discovery

The application scans a selected folder for supported PDF and image files. Unsupported files are skipped and the batch size is reported to the user.

## 2. PDF conversion

Each PDF is converted into page-level images so the same extraction path can be used for both PDFs and standalone images.

## 3. Textract analysis

Each page is submitted to Amazon Textract with form analysis enabled. The response contains keys, values, words, selection elements, confidence scores and normalized geometry.

## 4. Response parsing

The parser reconstructs readable key-value pairs, checkbox states and pixel coordinates. Page and source-file metadata are retained for traceability.

## 5. Dynamic alignment

Known anchor fields are compared with reference coordinates. Their average displacement is calculated and used to adjust the expected layout. Final X and Y tolerances include an additional margin to cover small scan variations.

## 6. Field association

Extracted values are matched to configured business fields according to adjusted coordinates, page and document segment.

## 7. Cleaning and normalization

The pipeline removes adjacent OCR noise, reconstructs fragmented dates, standardizes recurring values and records meaningful transformations as review findings.

## 8. Validation

General and conditional rules verify formats, required values and membership in configured master lists. Invalid or uncertain fields are marked for review.

## 9. Reshaping

Vertical extraction rows are transformed into horizontal records suitable for operational review and downstream export.

## 10. Human review

Users inspect and edit the structured information through a desktop interface before approving the final result.

## 11. Export

The workflow generates intermediate Excel reports, validation findings and a configured flat-file output for downstream processing.

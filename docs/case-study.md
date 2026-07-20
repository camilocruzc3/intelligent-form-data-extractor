# Case study

## Context

Organizations often receive structured information through scanned forms, PDFs and images. Manual transcription is slow, repetitive and vulnerable to errors, especially when documents contain checkboxes, handwritten fields, layout variations and incomplete values.

## Problem

The private implementation was created to automate the extraction, structuring, validation and export of form data while keeping a human review step before final delivery.

## Solution

The application processes batches of PDF and image files, converts PDFs to images, sends document pages to Amazon Textract, parses key-value relationships and selection elements, and preserves confidence and coordinate metadata.

The extracted information is then:

- Associated with configured field titles.
- Adjusted for layout displacement through dynamic coordinate tolerance.
- Cleaned and normalized.
- Validated against configurable business rules and master lists.
- Transformed into a horizontal record structure.
- Reviewed in a desktop interface.
- Exported to Excel reports and a configurable flat file.

## My contribution

- Designed and implemented the Python processing workflow.
- Integrated Amazon Textract for form analysis.
- Developed coordinate-based field association and dynamic tolerance logic.
- Built data-cleaning and validation routines with pandas.
- Implemented a desktop review workflow.
- Created Excel reports and flat-file export logic.
- Packaged the workflow for Windows-oriented local execution.

## Portfolio scope

This repository is a sanitized public reconstruction. It documents the architecture and selected generic components without publishing client documents, personal data, production rules, master files, credentials or the private repository history.

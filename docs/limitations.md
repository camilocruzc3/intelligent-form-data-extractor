# Limitations

This repository is a public portfolio reconstruction of a private working application. It is not yet a complete public demo or production-ready cloud service.

## Current limitations

- The complete private application is not published.
- The workflow is primarily designed for local Windows execution.
- Amazon Textract requires AWS credentials, network access and usage budget.
- Recognition quality depends on image resolution, handwriting, scan quality and layout consistency.
- Coordinate-based association depends on representative reference layouts and anchor fields.
- Business validations are only as reliable as their configured master lists.
- The desktop workflow does not provide enterprise identity management or role-based access control.
- Automated unit, integration and regression coverage is not yet represented in this public repository.
- There is no public benchmark for field-level precision, recall or end-to-end processing accuracy.
- Poppler and Windows packaging are intentionally excluded from the public repository.

## Production considerations

A production evolution should include centralized secrets management, document permissions, asynchronous processing, retry and dead-letter handling, monitoring, cost controls, quality evaluation, CI/CD and secure storage policies.

# Security and privacy

This project handles documents that may contain personal, financial or operational information. The public repository therefore follows a strict separation between demonstrable engineering work and private production assets.

## Excluded from this repository

- Real forms and scanned identity documents.
- Personal or customer information.
- Production Excel outputs and flat files.
- AWS credentials and local environment files.
- Customer-specific field catalogs, validation lists and output layouts.
- Application logs, temporary images and extraction results.
- Private repository history and internal paths.

## Credential handling

- AWS credentials must be loaded from environment variables or a secure credential provider.
- `.env` files must never be committed.
- IAM permissions should be restricted to the minimum actions and resources required.
- Credentials should be rotated when exposure is suspected.

## Document-processing controls

A production deployment should add:

- File type and size validation.
- Malware scanning before processing.
- Encryption in transit and at rest.
- Controlled temporary-file retention and secure deletion.
- Document-level authorization.
- Audit logs with defined retention policies.
- Masking or tokenization for sensitive fields.

## Public screenshots and examples

Any future screenshot or sample document must use synthetic data. Names, account numbers, addresses, identifiers, internal paths and customer branding must be removed or replaced before publication.

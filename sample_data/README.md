# Synthetic sample data

Only synthetic documents may be added to this directory.

A future public demo should include a fictitious multi-page form containing invented names, identifiers, addresses, dates and checkbox selections. The sample must not reproduce a customer's real form layout, branding, field catalog or downstream file specification.

Recommended files:

```text
sample_data/
├── documents/
│   └── synthetic_membership_form.pdf
├── config/
│   ├── field_coordinates_demo.xlsx
│   └── validation_lists_demo.xlsx
└── expected/
    └── expected_records.json
```

PDF, image and spreadsheet files remain ignored by default until they are individually reviewed and explicitly allowed in `.gitignore`.

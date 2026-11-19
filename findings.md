# Findings: messy.env

## Defects found

1. **Invalid data type:** `APP_PORT=hello`. The port must be a whole number, and `hello` is text.
2. **Debug policy violation:** `DEBUG=true`. For deployment, `DEBUG` must be exactly `false`.
3. **Empty required setting:** `DB_PASSWORD=` has no value, but it must be present and nonempty.
4. **Naming mismatch:** the file has `dbhost` (lowercase, legacy name) and also `DB_HOST=db`. The contract requires the exact key `DB_HOST`. Keys are case-sensitive, so `dbhost` does not count as `DB_HOST`.

## Validation rules (the configuration contract)

| Key | Rule |
|---|---|
| `APP_PORT` | Whole number from 1024 to 65535, inclusive |
| `DEBUG` | Must be exactly `false` |
| `DB_HOST` | Must be present and nonempty |
| `DB_PASSWORD` | Must be present and nonempty; its value is never displayed |

## How the validator handles this

- `validate()` returns a list of error strings, which is empty when the configuration is valid.
- Error messages name the key and the problem, never the value (for example `DB_PASSWORD is missing or empty`).
- The script exits with code 0 when valid and 1 when there are errors.
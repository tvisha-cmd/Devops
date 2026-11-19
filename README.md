# Configuration Validator

A small Python script that checks an `.env` configuration file before deployment. It reports problems clearly and never prints secret values.

## The rules

| Key | Rule |
|---|---|
| `APP_PORT` | Whole number from 1024 to 65535, inclusive |
| `DEBUG` | Must be exactly `false` |
| `DB_HOST` | Must be present and nonempty |
| `DB_PASSWORD` | Must be present and nonempty (its value is never displayed) |

Keys are case-sensitive, so `dbhost` does not count as `DB_HOST`.

## How to run

You need Python 3. From the project folder:

```powershell
python validator.py <path-to-env-file>
```

On macOS/Linux, use `python3` instead of `python`.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Configuration accepted |
| 1 | One or more errors found |

Check the code in PowerShell with `$LASTEXITCODE`, or in bash with `echo $?`.

## Test files

| File | What it tests | Expected output | Exit code |
|---|---|---|---|
| `valid.env.example` | Valid settings (dummy values) | `Configuration accepted` | 0 |
| `messy.env` | Bad port, debug on, empty password | `APP_PORT is not an integer`, `DEBUG must be false`, `DB_PASSWORD is missing or empty` | 1 |
| `bad-port.env.example` | `APP_PORT=80` (too low) | `APP_PORT is out of range` | 1 |
| `no-host.env.example` | `DB_HOST` removed | `DB_HOST is missing or empty` | 1 |

## Reproduce the tests

```powershell
python validator.py valid.env.example
$LASTEXITCODE
python validator.py messy.env
$LASTEXITCODE
python validator.py bad-port.env.example
$LASTEXITCODE
python validator.py no-host.env.example
$LASTEXITCODE
```

## Automated tests (optional)

```powershell
pip install pytest
python -m pytest -v
```

## Security notes

- Error messages name the key, never the value.
- Only dummy values are committed. Never commit a real `.env` file with real passwords.
- If a file is saved with a byte order mark (BOM), the first key may be misread. Save env files as plain UTF-8.

## Files

- `validator.py`: the validator
- `findings.md`: defects found in `messy.env`
- `test-evidence.md`: test results and exit codes
- `*.env.example`: example configurations with dummy values

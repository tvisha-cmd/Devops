# Test evidence

| File | Output | Exit code |
|---|---|---|
| valid.env.example | Configuration accepted | 0 |
| messy.env | APP_PORT is not an integer / DEBUG must be false / DB_PASSWORD is missing or empty | 1 |
| bad-port.env.example (APP_PORT=80) | APP_PORT is out of range | 1 |
| no-host.env.example (DB_HOST removed) | DB_HOST is missing or empty | 1 |

No password values appear in any output.
"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys

def validate(values):
    errors = []
    # TODO: APP_PORT must be an integer in 1024..65535.
    port = values.get("APP_PORT")
    if port is None :
        errors.append("APP_PORT is missing");
    else:
        try:
            n = int(port)
            if not (1024 <= n <= 65535):
                errors.append("APP_PORT is out of range")
        except ValueError:
            errors.append("APP_PORT is not an integer") 
    # TODO: DEBUG must be false, DB_HOST and DB_PASSWORD must be nonempty.
    debug = values.get("DEBUG");
    if debug is None:
        errors.append("DEBUG is missing")
    elif debug.lower() != "false":
        errors.append("DEBUG must be false")
    for key in ("DB_HOST", "DB_PASSWORD"):
        if not values.get(key):
            errors.append(f"{key} is missing or empty")
    return errors
    # Return useful errors naming keys, not secret values.

    raise NotImplementedError("Complete the configuration contract")

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))

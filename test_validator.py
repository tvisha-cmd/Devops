from validator import validate 

def test_good_config():
    assert validate({"APP_PORT": "8080", "DEBUG": "false", "DB_HOST": "localhost", "DB_PASSWORD": "X"}) ==[]

def test_bad_port():
    errors = validate({"APP_PORT": "hello", "DEBUG": "false",
                     "DB_HOST": "db", "DB_PASSWORD": "X"}) 
    assert errors == ["APP_PORT is not an integer"]
def test_no_secret_leak():
    errors = validate({"APP_PORT": "8080", "DEBUG": "true",
                       "DB_HOST": "db", "DB_PASSWORD": "supersecret"})
    assert all("supersecret" not in e for e in errors)
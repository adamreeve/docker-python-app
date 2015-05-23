import os
import base64


DEBUG = os.getenv("DEBUG", "false") == "true"
TESTING = os.getenv("TESTING", "false") == "true"

secret_key = os.getenv("SECRET_KEY")
if secret_key is None:
    raise ValueError("SECRET_KEY must be set")
SECRET_KEY = base64.b64decode(secret_key)

DB_CONNECTION = "postgresql://{0}:{1}@{2}/{3}".format(
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_NAME"))

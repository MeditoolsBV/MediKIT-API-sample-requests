import enum
import json
import os
import uuid
from datetime import datetime, timedelta, timezone

import jwt
import requests


# Define required enums
class Realms(enum.StrEnum):
    TEST = "dev"
    ACCEPTATION = "acc"
    PRODUCTION = "prd"

    @classmethod
    def from_env(cls) -> "Realms":
        env = os.environ.get("ENV", "TEST")
        match env:
            case "TEST":
                return cls.TEST
            case "ACC":
                return cls.ACCEPTATION
            case "PRD":
                return cls.PRODUCTION
            case _:
                raise ValueError("ENV should be one of 'TEST', 'ACC' or 'PRD'")


# Set auth data
REALM = Realms.from_env()
CLIENT_ID = os.environ["CLIENT_ID"]
with open(os.environ["SIGNING_KEY_PATH"], "r") as f:
    PRIVATE_KEY = f.read()

# Generate JWT
client_assertion = jwt.encode(
    {
        "jti": str(uuid.uuid4()),  # Unique identifier - log this for debug correlation
        "sub": CLIENT_ID,
        "iss": CLIENT_ID,
        "aud": f"https://www.medikit.nl/auth/realms/{REALM}",
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=5),
        "scope": "openid profile email",
    },
    PRIVATE_KEY,
    algorithm="RS512",
)

# Get token
response = requests.post(
    url=f"https://www.medikit.nl/auth/realms/{REALM}/protocol/openid-connect/token",
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
    },
    data={
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion,
    },
)
print(response.json().get("access_token"))

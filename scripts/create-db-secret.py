#!/usr/bin/env python3
"""Create a namespaced database Secret without putting passwords in argv or files."""
import argparse
import base64
import getpass
import json
import secrets
import subprocess
from urllib.parse import quote

parser = argparse.ArgumentParser()
parser.add_argument("--namespace", default="orbit")
parser.add_argument("--release", default="orbit")
args = parser.parse_args()
password = getpass.getpass("Database password (blank generates a new random password): ")
password = password or secrets.token_urlsafe(32)
if len(password) < 12:
    raise SystemExit("Use at least 12 characters.")
url = f"postgresql+psycopg://orbit:{quote(password, safe='')}@{args.release}-postgres:5432/orbit"
secret = {
    "apiVersion": "v1", "kind": "Secret",
    "metadata": {"name": "orbit-database", "namespace": args.namespace},
    "type": "Opaque",
    "data": {key: base64.b64encode(value.encode()).decode() for key, value in {
        "POSTGRES_PASSWORD": password, "DATABASE_URL": url,
    }.items()},
}
# create refuses to overwrite a password for an existing PostgreSQL volume.
subprocess.run(["kubectl", "create", "-f", "-"], input=json.dumps(secret), text=True, check=True)
print("Created orbit-database. The password was not printed or saved to the repository.")

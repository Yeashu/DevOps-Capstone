#!/usr/bin/env python3
"""Keep live request and latency panels populated during a demonstration."""
import argparse
import json
import time
from urllib.request import Request, urlopen

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://localhost:3000")
parser.add_argument("--seconds", type=int, default=180)
args = parser.parse_args()
deadline = time.monotonic() + args.seconds
count = 0
while time.monotonic() < deadline:
    body = json.dumps({"expression": "sqrt(144) + sin(pi/2)"}).encode()
    request = Request(args.url.rstrip("/") + "/api/evaluate", data=body,
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=5) as response:
        response.read()
    count += 1
    time.sleep(.2)
print(f"Completed {count} real evaluation requests without creating notebook records.")

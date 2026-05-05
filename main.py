#!/usr/bin/env python3
"""ts-explorer - A simple utility module."""

import json
import os
from datetime import datetime

VERSION = "0.5.28"

def load_config(path="config.json"):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {"debug": False}

def run():
    config = load_config()
    print(f"[{datetime.now()}] Running {VERSION}")
    return config

if __name__ == "__main__":
    run()

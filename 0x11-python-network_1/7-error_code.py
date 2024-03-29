#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""

from sys import argv
import requests

if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.HTTPError as e:
        print(f"Error code: {e}")

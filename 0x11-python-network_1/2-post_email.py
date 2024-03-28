#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
o the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

import urllib.request
import sys

if __name__ == "__main__":
    """Encode email"""
    data = {}
    data['email'] = str(sys.argv[2])
    email = urllib.parse.urlencode(data)
    """Get the url"""
    url = sys.argv[1]
    full_url = url + "?" + email
    """Send POST request"""
    req = urllib.request.Request(full_url, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

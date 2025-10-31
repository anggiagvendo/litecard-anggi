import pytest, json
from playwright.sync_api import Page, expect, sync_playwright

base_url = "https://bff-api.demo.litecard.io"
username = "qa-a3@litecard.com.au"
password = "bR5x$9wNzE"

def test_authenticate() :
    with sync_playwright() as p : 
        request_context = p.request.new_context()

        login_payload = {
            "username" : f"{username}",
            "password" : f"{password}"
        }

        response = request_context.post(f"{base_url}/api/v1/token", data=login_payload)
        assert response.ok, f"Auth failed {response.text()}"

        token = response.json()["access_token"]
        print(f"access_token : {token}")
        return token

def test_api_request(request_context, method, endpoint, token=None, body=None):
    headers = {"Content-type":"application/json"}
    if token :
        headers["Authorization"] = f"Bearer {token}"

    url = f"{base_url}{endpoint}"
    payload = json.dumps(body) if body else None

    if method == "Get":
        res = request_context.get(url, headers=headers)
    elif method == "POST":
        res = request_context.post(url, data=payload, headers=headers)
    elif method == "PATCH":
        res = request_context.patch(url, data=payload, headers=headers)
    elif method == "PUT":
        res = request_context.put(url, data=payload, headers=headers)
    elif method == "DELETE":
        res = request_context.delete(url, headers=headers)
    else:
        raise ValueError("Invalid HTTP method")
    
    assert res.ok, f"{method} {endpoint} failed {res.text()}"
    return res.json()


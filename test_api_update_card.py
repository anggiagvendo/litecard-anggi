import pytest, json
from playwright.sync_api import Page, expect, sync_playwright

base_url = "https://bff-api.demo.litecard.io"
username = "qa-a3@litecard.com.au"
password = "bR5x$9wNzE"

#get login access_token for reusable cases
def get_token(request_context) :
    
        login_payload = {
            "username" : f"{username}",
            "password" : f"{password}"
        }

        response = request_context.post(f"{base_url}/api/v1/token", data=login_payload)
        assert response.ok, f"Auth failed {response.text()}"

        token = response.json()["access_token"]
        print(f"access_token : {token}")
        return token

#declaration for API methods
def api_request(request_context, method, endpoint, token=None, body=None):
    headers = {"Content-type":"application/json"}
    if token :
        headers["Authorization"] = f"Bearer {token}"

    url = f"{base_url}{endpoint}"

    if method == "GET":
        res = request_context.get(url, headers=headers)
    elif method == "POST":
        res = request_context.post(url, data=body, headers=headers)
    elif method == "PATCH":
        res = request_context.patch(url, data=body, headers=headers)
    elif method == "PUT":
        res = request_context.put(url, data=body, headers=headers)
    elif method == "DELETE":
        res = request_context.delete(url, headers=headers)
    else:
        raise ValueError("Invalid HTTP method")
    
    assert res.ok, f"{method} {endpoint} failed {res.text()}"
    return res.json()

def test_api_flow() : 
        
        with sync_playwright() as p : 
            request_context = p.request.new_context()

            #Call login function
            token = get_token(request_context)

            #Load json
            with open("email_to_cardId.json","r") as f:
                users = json.load(f)
        
            #collecting cardID from json and repeat action based on data count in json
            for item in users:
                card_id = item["cardId"]
                email = item ["email"]

                print (f"\n collecting {email} and {card_id}")

                #test API flow
                #Update birthday card
                update_payload = {
                    "cardId": f"{card_id}",
                    "cardPayload": { 
                    "birthday": "1993-11-11T10:26:01.963Z"      
                    }}
                
                update_birthday_card = api_request(request_context, "PATCH", f"/api/v1/card", token, body=json.dumps(update_payload))

                print (f"\n update birthday result : {update_birthday_card}")

                #GET API
                get_result = api_request(request_context, "GET", f"/api/v1/card/{card_id}", token)
                print(f"\n card data : {get_result}")


            #Update status to inactive and delete
            limited_users = users[:2]

            for item in limited_users : 
                card_id = item["cardId"]
                email = item ["email"]

                print (f"\n collecting limited users {email} and {card_id}")

                #update status to inactive
                update_status_inactive_payload = {
                    "cardId": f"{card_id}", 
                    "status": "INACTIVE" 
                }

                update_status_inactive = api_request(request_context, "POST", f"/api/v1/card/status", token, body=json.dumps(update_status_inactive_payload))
                print(f"updating status of {card_id} with email {email} into INACTIVE!")

                #update status to delete
                update_status_inactive_payload = {
                    "cardId": f"{card_id}", 
                    "status": "DELETED" 
                }

                update_status_inactive = api_request(request_context, "POST", f"/api/v1/card/status", token, body=json.dumps(update_status_inactive_payload))
                print(f"updating status of {card_id} with email {email} into DELETED!")

                #GET API
                get_result = api_request(request_context, "GET", f"/api/v1/card/{card_id}", token)
                print(f"\n card data : {get_result}")



# litecard-anggi
# Installation Steps
This part will guide to use the automation script at your local.

If you have Python installed in your device, skip step 1 and 2 :
1. Download Python from official site https://www.python.org/downloads/
2. Verify Python and pip by executing these commands in cmd : 
 - ```python --version```
 - ```pip --version```
3. Install Pytest plugin by running this command : 
 - ```pip install pytest-playwright```
4. Install Playwright browser : 
 - ```playwright install```
5. Create a folder for the Playwright project (just make folder like usual).
6. Put the Playwright project into the created folder.
7. Open cmd and ensure directory is at the Playwright project folder.
8. For UI test, execute this command in cmd : 
 - ```pytest test_ui_form.py -s```
9. After executing the UI automation, the json file will be created. This json file will be used for API automation.
10. For API test, execute this command in cmd (ensure that json file has been created from UI automation):
 - ```pytest test_api_update_card.py -s```

<br><br>

# Manual Test Case Document

## Test Case Information #1
| Field | Details |
|---|---|
| **Test Case ID** | TC-UI-001 |
| **Title** | User pass creation |
| **Module** | Create pass |
| **Method** | UI |
| **Priority** | High |
| **Last update** | Oct 11st, 2025 |

---

## Pre-Conditions
- Have browser like : 
    - Opera 
    - Chrome
    - Edge
    - Safari
- Have form ID : pb9e77oLuLZQYjauf-lDW

---

## Test Steps & Expected Results

| Steps | Location | Test Step | Expected Result | Additional Note | Status (Pass/Fail) | Remarks |
|--------:|-----------|-----------|----------------|--------------|-------------------|--------|
| 1 | Browser | Navigate to submission form https://demo.litecard.io/form/custom/{{FORM_ID}}  | Form submission page is displayed |  |  |  |
| 2 | Form page| Fill all required fields | All fields are filled |  |  |  |
| 3 | Form page | Check mark term and conditions |  Can be check marked |  |  |  |
| 4 | Form page | Press submit button | Card creation notification appears at top | Need to wait for 5s for card creation process |  |  |
| 5 | Form page | Wait for card creation | User is redirected to wallet option page after card creation is successful  |  |  |  |
| 6 | Wallet option page | Wallet UI element observe | There are 2 options to add into Google or Apple wallet  |  |  |  |

## Test Case Information #2
| Field | Details |
|---|---|
| **Test Case ID** | TC-UI-001 |
| **Title** | Card parameter update |
| **Module** | Card update |
| **Method** | API |
| **Priority** | High |
| **Last update** | Oct 11st, 2025 |

---

## Pre-Conditions
- Have access to API swagger : https://bff-api.demo.litecard.io/api/v1/swagger#
- Username : qa-a3@litecard.com.au
- Password : bR5x$9wNzE

---

## Test Steps & Expected Results

| Steps | Feature | API url | Method | Test Step | Expected Result | Additional Note | Status (Pass/Fail) | Remarks |
|--------:|---|---|---|---|---|---|---|---|
| 1 | Authentication| https://bff-api.demo.litecard.io/api/v1/token | POST | Fill username and password then submit to get auth token  | access_token is generated |  |  |  |
| 2 | Authorize access_token| - | - | Fill the access token into authorization pop-up from authorization button at top right of Swagger page  | access_token is verified |  |  |  |
| 3 | Update birthday parameter| https://bff-api.demo.litecard.io/api/v1/card | PATCH | Fill request body with json format below {*update birthday payload*}  | success update birthday |  |  |  |
| 4 | Update passes into inactive| https://bff-api.demo.litecard.io/api/v1/card/status | POST |  Fill request body with json format below {*update passes into inactive*}  | success update pass status |  |  |  |
| 5 | Validate the card update|https://bff-api.demo.litecard.io/api/v1/card | GET | Fill request body with json format below {*update passes into deleted*}  | both birthday and parameter updates are reflected well for each passes |  |  |  |


 - update birthday payload : 
`{ 
"cardId": "<CARD_ID>", 
"cardPayload": { 
"birthday": "2025-10-25T10:26:01.963Z" 
} 
}`

- update passes into inactive : 
`{ 
"cardId": "<CARD_ID>", 
"status": "ACTIVE" 
}`

- update passes into deleted : 
`{ 
"cardId": "<CARD_ID>", 
"status": "DELETED" 
}`



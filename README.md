# litecard-anggi
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
| 5 | Validate the card update|https://bff-api.demo.litecard.io/api/v1/card | GET | Fill request body with json format below {*update passes into inactive*}  | both birthday and parameter updates are reflected well for each passes |  |  |  |



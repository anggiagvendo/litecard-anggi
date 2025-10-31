import pytest
from playwright.sync_api import Page, expect

def test_ui_form (page : Page):
    #parameters
    username = "qa-a3@litecard.com.au"
    password = "bR5x$9wNzE"
    template_id = "lZ7osD5xxaLBfrZz3attN"
    form_id = "pb9e77oLuLZQYjauf-lDW"
    first_name = "Anggi"
    last_name ="Agvendo"
    created_emails = []
    current_index = 1
    max_count = 5
    
    
    #repeating steps of user creation
    while current_index <= max_count : 

        email = f"{first_name}{last_name}+{current_index}@gmail.com"

        #open the form and ensure submit button is visible
        page.goto(f"https://demo.litecard.io/form/custom/{form_id}")
        page.wait_for_timeout(5000)
        expect(page.locator('xpath=//*[@id="root"]/div/main/div/div/div[2]/div/div[3]/div/div')).to_be_visible()

        #filling out form
        page.get_by_role("textbox", name="First Name").fill(f"{first_name}")
        page.get_by_role("textbox", name="Last Name").fill(f"{last_name}")
        page.get_by_role("textbox", name="Email").fill(f"{email}")
        page.get_by_role("textbox", name="DD/MM/YYYY").fill("23/10/2025")
        page.get_by_role("spinbutton").fill("55555")
        page.locator('xpath=//*[@id="root"]/div/main/div/div/div[2]/div/div[3]/div/div/div/div[1]/label/span/input[1]').click()
        page.get_by_role("button", name="Submit").click()
        page.wait_for_timeout(10000)

        #detect google wallet and iOS wallet existence
        expect(page.get_by_role("link", name="Add to Apple Wallet")).to_be_visible()
        expect(page.get_by_role("link", name="Add to Google Wallet")).to_be_visible()

        #update parameter control
        current_index += 1
        created_emails.append(email)


    #login dashboard
    page.goto("https://demo.litecard.io/")
    expect(page.get_by_role("button", name="Log In")).to_be_visible()
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("textbox", name="Email address")).to_be_visible()
    page.get_by_role("textbox", name="Email address").fill(f"{username}")
    page.get_by_role("textbox", name="Password").fill(f"{password}")
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(10000)
    expect(page.get_by_role("heading", name="View Passes")).to_be_visible()

    #extracting ID
    rows_count = page.locator("//*[@id='page-container']//table/tbody/tr").count()
    card_ids = []

    for i in range(rows_count):
        cell_xpath = f"//*[@id='page-container']//table/tbody/tr[{i+1}]/td[1]"
        cell_locator = page.locator(cell_xpath)
    
    # ensure element exists before reading
        if cell_locator.count() > 0:
            value = cell_locator.inner_text().strip()
            if value:  # only append if not blank
                card_ids.append(value)

    card_ids = card_ids[:len(created_emails)]

    #map email to card id
    email_card_map = []

    for i in range(min(len(created_emails), len(card_ids))):
        email_card_map.append({
            "email": created_emails[i],
            "cardId": card_ids[i]
        })

    print(email_card_map)


    page.pause()
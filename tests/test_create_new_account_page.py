import pytest
import allure
import os
from faker import Faker
from dotenv import load_dotenv

load_dotenv()

fake = Faker()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PASSWORD_CONFIRM = os.getenv("PASSWORD_CONFIRM")


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with valid data")
@pytest.mark.critical
@pytest.mark.smoke
def test_create_new_user_account_valid_data(create_new_account_page):
    create_new_account_page.open_page()
    # create_new_account_page.accept_cookies()
    create_new_account_page.fill_login_form(fake.name(), fake.last_name(), fake.email(), EMAIL, PASSWORD)
    create_new_account_page.message_verification(
        "Thank you for registering with Main Website Store."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an existing email address")
@pytest.mark.medium
@pytest.mark.regression
def test_create_new_user_account_existing_data(create_new_account_page):
    create_new_account_page.open_page()
    # create_new_account_page.accept_cookies()
    create_new_account_page.fill_login_form("Skyla", "Kemmer", EMAIL, "VShbp3hR3", "VShbp3hR3")
    create_new_account_page.message_verification(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid email address")
@pytest.mark.medium
@pytest.mark.extended
def test_create_new_user_account_incorrect_email(create_new_account_page):
    create_new_account_page.open_page()
    # create_new_account_page.accept_cookies()
    create_new_account_page.fill_login_form("Kasandra", "Herzog", "Christoph1gmail.com", PASSWORD, PASSWORD)
    create_new_account_page.invalid_email_message_verification(
        "Please enter a valid email address (Ex: johndoe@domain.com)."
    )

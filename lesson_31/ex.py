from behave import given, when, then
from myapp.auth import login_user


def open_url(args):
    pass

def filled_field(text):
    pass

def status_for_element(element):
    pass


@given('the user is on the login page')
def step_user_on_login_page(context):
    context.page = "login"


@when('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    context.username = "testuser"
    context.password = "secure123"
    context.result = login_user(context.username, context.password)


@when('the user enters invalid credentials')
def step_user_enters_invalid_credentials(context):
    context.username = "wronguser"
    context.password = "wrongpass"
    context.result = login_user(context.username, context.password)


@when('clicks the login button')
def step_click_login_button(context):
    pass  # Usually included in the login_user() call


@then('the user should be redirected to the dashboard')
def step_redirect_dashboard(context):
    assert context.result == "dashboard"


@then('an error message should be displayed')
def step_error_displayed(context):
    assert context.result == "error"
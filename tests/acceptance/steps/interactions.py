from behave import *

from BDDSelenium.tests.acceptance.page_model.base_page import BasePage
from BDDSelenium.tests.acceptance.page_model.new_posts_page import NewPostPage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_imp(context, link_text):
    page = BasePage(context.browser)
    links = page.navigation
    matching_links = [li for li in links if li.text == link_text]
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise AttributeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.browser)
    page.form_field(field_name).send_keys(content)


@when("I press the submit button")
def step_impl(context):
    page = NewPostPage(context.browser)
    page.submit_button.click()

from behave import *
from selenium import webdriver

from BDDSelenium.tests.acceptance.page_model.blog_page import BlogPage
from BDDSelenium.tests.acceptance.page_model.home_page import HomePage
from BDDSelenium.tests.acceptance.page_model.new_posts_page import NewPostPage

use_step_matcher('re')

DRIVER_PATH = "F:/Python Projects/InterviewPractice/Selenium/chromedriver.exe"


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    page = HomePage(context.browser)
    context.browser.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    page = BlogPage(context.browser)
    context.browser.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    page = NewPostPage(context.browser)
    context.browser.get(page.url)


@then('I am on the blog page')
def step_imp(context):
    expected_url = BlogPage(context.browser).url
    assert context.browser.current_url == expected_url


@then('I am on the homepage')
def step_imp(context):
    expected_url = HomePage(context.browser).url
    assert context.browser.current_url == expected_url

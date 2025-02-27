import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.django_db
def test_home_page(browser):
    # browser.get('http://localhost:8000/' + reverse('home'))
    # browser.get('http://localhost:8000/')

    # assert 'install' in browser.title

    # heading = browser.find_element('tag name', 'h1')
    # assert heading.text == 'The install worked successfully! Congratulations!'
    ...


@pytest.mark.django_db
def test_create_todo_page(browser):
    browser.get('http://localhost:8000/' + reverse('create_todo'))
    
    header = browser.find_element(By.TAG_NAME, 'title')
    header_title = header.get_attribute('textContent')
    assert header_title == 'Document', f"Expected title to be 'Document' but got {header_title}"

    title_input = browser.find_element(By.NAME, 'title')
    description_input = browser.find_element(By.NAME, 'description')
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    title_input.send_keys('push ups')
    description_input.send_keys('Do 20 push ups today')
    submit_button.click()

    redirect_url = 'http://localhost:8000/'
    assert browser.current_url == redirect_url, f"Expected to be redirected to {redirect_url} but got {browser.current_url}"
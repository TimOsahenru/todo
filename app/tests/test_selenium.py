import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page(browser):
    # browser.get('http://localhost:8000/' + reverse('home'))
    browser.get('http://localhost:8000/')

    assert 'install' in browser.title

    heading = browser.find_element('tag name', 'h1')
    assert heading.text == 'The install worked successfully! Congratulations!'
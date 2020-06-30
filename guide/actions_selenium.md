# ```actions_selenium``` built in Actions

Some of the code examples on this page assume use the page file below

```python
# pages/google_homepage.py
from selenium.webdriver.common.by import By


class google_homepage:
    search_textbox = (By.NAME, 'q')
```

## Actions for navigation

### ```actions_selenium.navigate_to```

Navigates the browser to the URL passed as the first argument to the
constructor.

```python
from actions_selenium import navigate_to

actor.attempts_to(
    navigate_to('https://www.google.co.uk')
)
```

## Actions for saving screenshots

### ```actions_selenium.save_screenshot_to_file```

## Actions for finding elements

### ```actions_selenium.find_element```

Finds an element using a locator (usually from a page object) passed as the
first argument to the constructor.

This action will always return the element.

```python
from actions_selenium import find_element
from pages.google_homepage import google_homepage

element = actor.attempts_to(
    find_element(google_homepage.search_box)
)
```

#### ```.and_store_as(id)``` method

Make the action store the element in the ```Actor```'s state identified by the
first argument to the method.

```python
from actions_selenium import find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box')
)
```

#### ```.if_nothing_is_found_fail_with_message(message)``` method

If the element specified by the locator could not be found, this method will
make the test fail after the element could not be found with the message passed
as the first argument to the method.

```python
from actions_selenium import find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box')
    .if_nothing_is_found_fail_with_message('Unable to find "Search Box"')
)
```

### ```actions_selenium.find_element_with_locator_and_text```

### ```actions_selenium.find_elements```

### ```actions_selenium.find_sub_element```

### ```actions_selenium.find_stored_element_in```

## Actions for interacting with elements

### ```actions_selenium.click_on```

An Action to click on an element

#### ```.element(locator)``` method

Clicks on an element using a locator (usually from a page object).

```python
from actions_selenium import click_on
from pages.google_homepage import google_homepage

actor.attempts_to(
    click_on().element(google_homepage.search_box)
)
```

#### ```.stored_element(id)``` method

Clicks on an element stored in the ```Actor```'s state identified by the id
passed as the first argument to the method. The element will usually be stored
in the actor's state using one of the ```action_selenium.find_*``` actions.


```python
from actions_selenium import click_on, find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box'),
    click_on().stored_element('search_box')
)
```

### ```actions_selenium.click_on_sub_element```

### ```actions_selenium.enter_text```

### ```actions_selenium.send_key_to```

## Actions for getting information about elements

### ```actions_selenium.text_of```

### ```actions_selenium.value_of```

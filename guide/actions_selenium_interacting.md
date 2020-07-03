# ```actions_selenium``` - Actions for interacting with elements

Some of the examples on this page use the
[google_homepage](actions_selenium_page.md) page object.

## ```actions_selenium.click_on```

An Action to click on an element

### ```.element(locator)``` method

Clicks on an element using a locator (usually from a page object).

```python
from actions_selenium import click_on
from pages.google_homepage import google_homepage

actor.attempts_to(
    click_on().element(google_homepage.search_box)
)
```

### ```.stored_element(id)``` method

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

## ```actions_selenium.click_on_sub_element```

## ```actions_selenium.enter_text```

## ```actions_selenium.send_key_to```

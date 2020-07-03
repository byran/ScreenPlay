# ```actions_selenium``` - Actions for finding elements

Some of the examples on this page use the
[google_homepage](actions_selenium_page.md) page object.


## ```actions_selenium.find_element```

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

### ```.and_store_as(id)``` method

Make the action store the element in the ```Actor```'s state identified by the
first argument to the method.

```python
from actions_selenium import find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box')
)
```

### ```.if_nothing_is_found_fail_with_message(message)``` method

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

## ```actions_selenium.find_element_with_locator_and_text```

## ```actions_selenium.find_elements```

## ```actions_selenium.find_sub_element```

## ```actions_selenium.find_stored_element_in```

# Guide to using ScreenPlay with Behave

## General process for writing a feature & scenarios

1. Writing a feature file
2. [Create step definitions for the feature steps](creating_step_definitions.md)
3. For each given or when (generic) step definition:
   1. [Implement the tasks that the step definition runs](creating_a_task.md)
   2. [Implement a page to hold the locators](creating_a_page.md)
   3. (optionally) Implement actions to complete the tasks
4. For each then step definition:
   1. Implement the question to get information about the state of the system
   under test
   2. Implement the matcher to check the answer the question returned

## Other ScreenPlay features

* Using the Actor's state to store information
* Implementing abilitites

## Built in Abilities, Tasks, Actions, Matchers

### Abiltiies

* abilities.browse_the_web

### Tasks

* tasks_selenium.save_screenshot

### Actions

#### ```actions_common```

[actions_common](actions_common.md)

* actions_common.fail_with_message
* actions_common.if_value_of
* actions_common.pause_for
* actions_common.select_element_at_index

#### ```actions_selenium```

[Actions for navigation](actions_selenium_navigation.md)

* actions_selenium.navigate_to

[Actions for saving screenshots](actions_selenium_save_screenshots.md)

* actions_selenium.save_screenshot_to_file

[Actions for finding elements](actions_selenium_find.md)

* actions_selenium.find_element
* actions_selenium.find_element_with_locator_and_text
* actions_selenium.find_elements
* actions_selenium.find_stored_element_in
* actions_selenium.find_sub_element

[Actions for interacting with elements](actions_selenium_interacting.md)

* actions_selenium.click_on
* actions_selenium.click_on_sub_element
* actions_selenium.enter_text
* actions_selenium.send_key_to

[Actions for querying information](actions_selenium_information.md)

* actions_selenium.text_of
* actions_selenium.value_of

### Matchers

screenplay.matchers

* screenplay.matchers.contains
* screenplay.matchers.equals
* screenplay.matchers.is_an_empty_list

matchers_selenium

* matchers_selenium.is_displayed
* matchers_selenium.is_not_present

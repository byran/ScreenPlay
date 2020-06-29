from behave import runner, model
from screenplay.behave_extensions import add_screenplay_objects_to
from screenplay.log import Log
from abilities.browse_the_web import browse_the_web
from tasks_selenium import save_screenshot
from actions_selenium._find_base_action import find_base_action
import os
import pathlib


def find_element_failure_actions():
    return [save_screenshot()]


def before_all(context: runner.Context):
    repositoryRoot = pathlib.Path(__file__).parent.parent.parent.absolute()
    save_screenshot.path = os.path.join(repositoryRoot, 'docs', 'test_results')
    find_base_action.create_fail_actions_callback = find_element_failure_actions


def before_scenario(context: runner.Context, scenario: model.Scenario):
    Log.to_actions()
    add_screenplay_objects_to(context)
    context.actors.add_person_called('Byran').who_can(browse_the_web.using_Chrome())
    context.actors.switch_active('Byran')


def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.actors.clean_up()

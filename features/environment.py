from behave import runner, model
from screenplay.behave import add_screenplay_objects_to
from screenplay.log import Log
from abilities.browse_the_web import browse_the_web
from abilities.control_led import control_led


def before_scenario(context: runner.Context, scenario: model.Scenario):
    Log.to_actions()
    add_screenplay_objects_to(context)
    context.actors.add_person_called('Byran').who_can(browse_the_web.using_Chrome(), control_led())


def after_scenario(context: runner.Context, scenario: model.Scenario):
    context.actors.clean_up()

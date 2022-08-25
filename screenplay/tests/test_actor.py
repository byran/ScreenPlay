import pytest
from screenplay import Actor, see_that, using, value_of
from screenplay.matchers.equals import equals
from .stub_abilities import StubAbility, SecondStubAbility
from .stub_tasks import StubTask, StubTaskWithResult
from .stub_questions import StubQuestion


def test_An_actors_name_can_be_retrieved():
    frank = Actor.named('Frank')

    assert frank.name == 'Frank'


def test_An_Ability_can_be_added_and_reterived_from_an_Actor():
    bob = Actor.named('Bob')

    bob.can(StubAbility())

    ability = bob.ability(StubAbility)

    assert ability is not None, "Ability not found"


def test_Multiple_Ability_objects_can_be_added_and_reterived_from_an_Actor():
    bob = Actor.named('Bob')

    bob.can(StubAbility())
    bob.can(SecondStubAbility())

    assert bob.ability(StubAbility) is not None, "Ability not found"
    assert bob.ability(SecondStubAbility) is not None, "Ability not found"


def test_Trying_to_get_an_ability_an_Actor_does_not_have_causes_an_assertion():
    bob = Actor.named('Bob')

    bob.can(SecondStubAbility())

    with pytest.raises(AssertionError):
        bob.ability(StubAbility)


def test_Multiple_Ability_objects_are_cleaned_up_with_an_Actor_is_cleaned_up():
    bob = Actor.named('Bob')

    first_ability = StubAbility()
    second_ability = SecondStubAbility()
    bob.can(first_ability)
    bob.can(second_ability)

    bob.clean_up()

    assert first_ability.clean_up_run, 'Ability not cleaned up'
    assert second_ability.clean_up_run, 'Ability not cleaned up'


def test_An_Actor_can_perform_Tasks():
    claire = Actor.named('Claire')

    task1 = StubTask()
    task2 = StubTask()

    claire.attempts_to(
        task1,
        task2
    )

    assert task1.called, "Task 1 not run"
    assert task2.called, "Task 2 not run"


def test_An_Actor_can_perform_Tasks_specified_as_a_function():
    claire = Actor.named('Claire')

    actual: int = 0

    def FunctionTask(value: int):
        def Task(actor):
            nonlocal actual
            actual = value
        Task.is_action = True
        return Task

    claire.attempts_to(
        FunctionTask(10)
    )

    assert actual == 10, "Function Action was not called"


def test_An_Actor_can_check_conditions_and_does_not_assert_if_the_conditions_are_all_True():
    david = Actor.named('David')

    david.should(
        see_that(StubQuestion('1'), equals('1')),
        see_that(StubQuestion('2'), equals('2'))
    )


def test_An_Actor_will_assert_if_any_of_the_checked_conditions_are_all_False():
    david = Actor.named('David')

    with pytest.raises(AssertionError):
        david.should(
            see_that(StubQuestion('1'), equals('1')),
            see_that(StubQuestion('text'), equals('2'))
        )


def test_An_Actor_will_pass_questions_that_return_True_without_a_matcher():
    david = Actor.named('David')

    david.should(
        see_that(StubQuestion(True))
    )


def test_An_Actor_will_fail_questions_that_return_False_without_a_matcher():
    david = Actor.named('David')

    with pytest.raises(AssertionError):
        david.should(
            see_that(StubQuestion(False))
        )


def test_An_Actors_state_can_be_updated_with_a_using_task():
    frank = Actor.named('Frank')

    frank.attempts_to(
        using(StubTaskWithResult(2)).as_('Bob')
    )

    assert value_of(frank.state['Bob']) == 2


def test_A_using_task_without_an_id_asserts():
    frank = Actor.named('Frank')

    with pytest.raises(AssertionError):
        frank.attempts_to(
            using(StubTaskWithResult(2))
        )


def test_A_using_task_whose_sub_task_does_not_return_a_value_sets_the_state_to_none():
    frank = Actor.named('Frank')

    frank.attempts_to(
        using(StubTask()).as_('Simon')
    )

    assert value_of(frank.state['Simon']) is None

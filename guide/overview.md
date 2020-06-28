# Guide to using ScreenPlay with Behave

## General process for writing a feature & scenarios

1. Writing a feature file
2. [Create step definitions for the feature steps](creating_step_definitions.md)
3. For each given or when (generic) step definition:
   1. [Implement the tasks that the step definition runs](creating_a_task.md)
   2. (optionally) Implement actions to complete the tasks
4. For each then step definition:
   1. Implement the question to get information about the state of the system
   under test
   2. Implement the matcher to check the answer the question returned

## Implementing other ScreenPlay classes

* Implementing abilitites

## Other ScreenPlay functions

* Actors state

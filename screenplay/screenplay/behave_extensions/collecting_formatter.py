from behave.model import Feature, Scenario, Step
from behave.formatter.base import Formatter
from behave.model_core import Status
from typing import List
from itertools import chain
from ..log import Log
import time


class CollectedStep:
    def __init__(self, name: str, step_type: str):
        self.name = name
        self.step_type = step_type
        self.text: List[str] = []
        self.error_message = None
        self.status = 'not run'


class CollectedScenario:
    def __init__(self, name: str, tags: List[str]):
        self.name = name
        self.tags: List[str] = tags
        self.status = 'not run'
        self.steps: List[CollectedStep] = []


class CollectedFeature:
    def __init__(self, file_name: str, name: str, description: List[str], tags: List[str]):
        self.file_name = file_name
        self.name = name
        self.description: List[str] = description
        self.tags: List[str] = tags
        self.start_time = time.time()
        self.run_time = 0
        self.scenarios: List[CollectedScenario] = []

    def finished(self):
        self.run_time = time.time() - self.start_time


class CollectingFormatter(Formatter):
    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)

        self.currentFeature: CollectedFeature = None
        self.currentScenario: CollectedScenario = None
        self.currentStep: CollectedStep = None

        self.stepsToProcess: List[CollectedStep] = []
        self.currentStep_text: List[str] = []

        Log.write_line = self.write_function()

    def write_function(self):
        def formatter_write_line(*values, sep=''):
            line = sep.join(map(str, chain.from_iterable(values)))
            print(line)
            self.currentStep_text.append(line)
        return formatter_write_line

    def feature(self, feature: Feature):
        self.currentFeature = CollectedFeature(feature.filename, feature.name, feature.description, feature.tags)

    def scenario(self, scenario: Scenario):
        self.currentScenario = CollectedScenario(scenario.name, scenario.tags)
        self.currentFeature.scenarios.append(self.currentScenario)

        self.stepsToProcess = []

    def step(self, step: Step):
        stepToStore = CollectedStep(step.name, step.keyword)
        self.currentScenario.steps.append(stepToStore)

        self.stepsToProcess.append(stepToStore)

    def match(self, match):
        self.currentStep = self.stepsToProcess.pop(0)
        self.currentStep_text = []

    def result(self, step_result):
        self.currentStep.status = step_result.status.name
        self.currentStep.text = self.currentStep_text
        self.currentStep.error_message = step_result.error_message

        self.currentScenario.status = step_result.status.name

    def eof(self):
        self.currentFeature.finished()

    def close(self):
        pass

from behave.formatter.base import Formatter
from behave.model_core import Status
from typing import IO, Any
from xml.etree import ElementTree as ET
import time
from itertools import chain
from ..log import Log


class ScreenplayFormatter(Formatter):
    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)
        self.stream: IO[Any] = self.open()
        self.steps = []
        self.xml = ET.Element('features')
        Log.write_line = self.write_function()

    def write_function(self):
        def formatter_write_line(*values, sep=''):
            self.step_text += sep.join(map(str, chain.from_iterable(values))) + '\n'
        return formatter_write_line

    def feature(self, feature):
        self.feature_xml = ET.SubElement(self.xml, 'feature')
        self.feature_xml.attrib['name'] = feature.name
        self.scenario_xml = None
        self.step_xml = None
        self.feature_start_time = time.time()

    def scenario(self, scenario):
        self.scenario_xml = ET.SubElement(self.feature_xml, 'scenario')
        self.scenario_xml.attrib['name'] = scenario.name
        self.scenario_xml.attrib['status'] = 'passed'
        self.step_xml = None

    def step(self, step):
        self.steps.append(step)

    def match(self, match):
        step = self.steps.pop(0)

        self.step_xml = ET.SubElement(self.scenario_xml, 'step')
        self.step_xml.attrib['name'] = step.name

        self.step_text = ''

    def result(self, step_result):
        self.step_xml.attrib['status'] = step_result.status.name

        if step_result.status.value != Status.passed:
            self.scenario_xml.attrib['status'] = step_result.status.name

        self.step_xml.text = self.step_text

    def eof(self):
        self.feature_xml.attrib['time'] = str(time.time() - self.feature_start_time)

    def close(self):
        self.stream.write(ET.tostring(self.xml, encoding='UTF-8').decode('UTF-8'))

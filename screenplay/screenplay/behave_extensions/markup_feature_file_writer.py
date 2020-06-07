from .collecting_formatter import CollectedFeature, CollectedScenario, CollectedStep
from .markup_file_writer import MarkupFileWriter

status_style = {
    'not run': 'notrun',
    # behave.model_core.Status
    'untested': 'notrun',
    'skipped': 'notrun',
    'passed': 'passed',
    'failed': 'failed',
    'undefined': 'notimplemented',
    'executing': 'notrun'
}

def write_markup_feature_file(feature: CollectedFeature, writer: MarkupFileWriter):
    writer.write_heading_1('Feature: ' + feature.name)
    writer.write_paragraph(*feature.description)

    for scenario in feature.scenarios:
        writer.write_heading_2('Scenario: ' + scenario.name)

        writer.begin_table()
        for step in scenario.steps:
            style = status_style.get(step.status, 'failed')
            writer.add_table_row(step.step_type + ' ' + step.name, writer.text_with_style(step.status, style))
        writer.end_table()

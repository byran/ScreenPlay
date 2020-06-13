from .collecting_formatter import CollectedFeature, CollectedStep
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
    _write_tags(writer, feature.tags)
    writer.write_heading_1('Feature: ' + feature.name)
    writer.write_lines(*feature.description)

    for scenario in feature.scenarios:
        writer.horizontal_line()
        _write_tags(writer, scenario.tags)
        writer.write_heading_2('Scenario: ' + scenario.name)

        writer.begin_table()
        for step in scenario.steps:
            style = status_style.get(step.status, 'failed')

            screenshots_message = create_links_to_screenshots(step, writer)
            error_message = '' if step.error_message is None else step.error_message

            writer.add_table_row(step.step_type + ' ' + step.name,
                                 writer.text_with_style(step.status, style),
                                 screenshots_message, error_message)
        writer.end_table()


def create_links_to_screenshots(step: CollectedStep, writer: MarkupFileWriter) -> str:
    screenshots = []
    for line in step.text:
        line_text: str = line.strip()
        line_split = line_text.split("'")
        if len(line_split) == 3 and line_split[0] == 'Save screenshot ':
            screenshots.append(writer.link_to_relative_file(line_split[1]))
    return ' '.join(screenshots)


def _write_tags(writer: MarkupFileWriter, tags):
    if len(tags) > 0:
        writer.write_tags('@' + ' @'.join(tags))

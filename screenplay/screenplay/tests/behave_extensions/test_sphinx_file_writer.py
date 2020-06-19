from screenplay.behave_extensions.sphinx_file_writer import SphinxFileWriter
import io


start_of_sphinx_file = \
".. role:: passed\n\
.. role:: failed\n\
.. role:: notrun\n\
.. role:: notimplemented\n\
.. role:: tags\n\n"


def test_a_new_file_starts_with_the_styling_information():
    stream = io.StringIO()

    SphinxFileWriter(stream)

    assert stream.getvalue() == start_of_sphinx_file


def test_a_heading_1_outputs_text_with_equals_symbols_below():
    stream = io.StringIO()

    file = SphinxFileWriter(stream)

    file.write_heading_1('Hello')

    expected_text = start_of_sphinx_file + 'Hello\n=====\n\n'

    assert stream.getvalue() == expected_text, '"{actual}"\n\n"{expected}"\n'.format(expected=expected_text, actual=stream.getvalue())


def test_a_heading_2_outputs_text_with_minus_symbols_below():
    stream = io.StringIO()

    file = SphinxFileWriter(stream)

    file.write_heading_2('World')

    expected_text = start_of_sphinx_file + 'World\n-----\n\n'

    assert stream.getvalue() == expected_text, '"{actual}"\n\n"{expected}"\n'.format(expected=expected_text, actual=stream.getvalue())


def test_a_heading_3_outputs_text_with_circumflex_symbols_below():
    stream = io.StringIO()

    file = SphinxFileWriter(stream)

    file.write_heading_3('Something')

    expected_text = start_of_sphinx_file + 'Something\n^^^^^^^^^\n\n'

    assert stream.getvalue() == expected_text, '"{actual}"\n\n"{expected}"\n'.format(expected=expected_text, actual=stream.getvalue())


def test_a_table_is_output_correctly():
    stream = io.StringIO()

    file = SphinxFileWriter(stream)

    file.begin_table('First', 'Second')
    file.add_table_row('abc', 'def')
    file.add_table_row('ghi', 'jkl')
    file.end_table()

    expected_text = start_of_sphinx_file + \
        '===== ======\n' + \
        'First Second\n' + \
        '===== ======\n' + \
        'abc   def   \n' + \
        'ghi   jkl   \n' + \
        '===== ======\n\n'

    assert stream.getvalue() == expected_text, '"{actual}"\n\n"{expected}"\n'.format(expected=expected_text, actual=stream.getvalue())

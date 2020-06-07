from .markup_file_writer import MarkupFileWriter
from typing import IO, Any, List


class SphinxFileWriter(MarkupFileWriter):
    def __init__(self, file: IO[Any]):
        self._file = file
        self._table_headers: List[str] = []
        self._table_rows: List[List[str]] = []

        self._file.write('.. role:: passed\n\n')
        self._file.write('.. role:: failed\n\n')
        self._file.write('.. role:: notrun\n\n')
        self._file.write('.. role:: notimplemented\n\n')

    def write_line(self, text: str):
        self._file.write('| ' + text + '\n')

    def new_paragraph(self):
        self._file.write('\n')

    def write_paragraph(self, *lines: str):
        for line in lines:
            self._file.write('| ' + line + '\n')
        self._file.write('\n')

    def _write_heading_level(self, text: str, char: str):
        markup = (char * len(text)) + '\n\n'
        self._file.write(text + '\n' + markup)

    def write_heading_1(self, text: str):
        self._write_heading_level(text, '=')

    def write_heading_2(self, text: str):
        self._write_heading_level(text, '-')

    def write_heading_3(self, text: str):
        self._write_heading_level(text, '^')

    def begin_table(self, *columns: str):
        self._table_headers = columns
        self._table_rows = []

    def add_table_row(self, *columns: str):
        self._table_rows.append(columns)

    def _calculate_table_column_widths(self):
        column_widths = []

        for header in self._table_headers:
            column_widths.append(len(header))

        for row in self._table_rows:
            for i, text in enumerate(row):
                if len(column_widths) <= i:
                    column_widths.append(0)

                if len(text) > column_widths[i]:
                    column_widths[i] = len(text)
        return column_widths

    def end_table(self):
        column_widths = self._calculate_table_column_widths()

        table_seperator = ' '.join(map(lambda n: '=' * n, column_widths)) + '\n'

        def write_row(row):
            columns = []
            for i, text in enumerate(row):
                columns.append(text + ' ' * (column_widths[i] - len(text)))
            self._file.write(' '.join(columns) + '\n')

        self._file.write(table_seperator)
        if len(self._table_headers) > 0:
            write_row(self._table_headers)
            self._file.write(table_seperator)
        for row in self._table_rows:
            write_row(row)
        self._file.write(table_seperator)

    def text_with_style(self, text: str, style: str):
        return ':{style}:`{text}`'.format(text=text, style=style)

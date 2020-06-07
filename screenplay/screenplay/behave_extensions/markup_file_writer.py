
class MarkupFileWriter:
    def write_line(self, text: str):
        pass

    def new_paragraph(self):
        pass

    def write_paragraph(self, *lines: str):
        pass

    def write_heading_1(self, text: str):
        pass

    def write_heading_2(self, text: str):
        pass

    def write_heading_3(self, text: str):
        pass

    def begin_table(self, *columns: str):
        pass

    def add_table_row(self, *columns: str):
        pass

    def end_table(self):
        pass

    def text_with_style(self, text: str, style: str) -> str:
        return ''

    def link_to_relative_file(self, file: str) -> str:
        return ''

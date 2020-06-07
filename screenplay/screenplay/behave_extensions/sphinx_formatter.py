from .collecting_formatter import CollectingFormatter
from .sphinx_file_writer import SphinxFileWriter
from .markup_feature_file_writer import write_markup_feature_file
from os import path

class SphinxScreenplayFormatter(CollectingFormatter):
    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)

        self.outputDirectory = path.join(config.base_dir, config.userdata['behave.formatter.sphinx.path'])

    def eof(self):
        super().eof()
        (_, file_name) = path.split(self.currentFeature.file_name)
        (file_name, _) = path.splitext(file_name)
        filePath = path.join(self.outputDirectory, file_name + '.rst')

        file = open(filePath, 'wt')
        sphinxWriter = SphinxFileWriter(file)
        write_markup_feature_file(self.currentFeature, sphinxWriter)
        file.close()

    def close(self):
        super().close()

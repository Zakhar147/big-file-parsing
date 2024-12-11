from modules.utils.calc import calc_chunk_size, calc_file_size
from modules.utils.validate import validate_file_path

class FileHandler:
    def __init__(self, file_path):
        validate_file_path(file_path)
        self.file_path = file_path
        self.file_size = calc_file_size(self.file_path)
        self.chunk_size = calc_chunk_size(self.file_size)

    def read_chunk(self, start, size):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            f.seek(start)
            return f.read(size)
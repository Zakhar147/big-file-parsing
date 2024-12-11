class ChunkProcessor:
    def __init__(self, file_handler, chunk_size):
        self.file_handler = file_handler
        self.chunk_size = chunk_size

    def count_letters_in_chunk(self, start, size):
        chunk = self.file_handler.read_chunk(start, size)
        return sum(1 for char in chunk if char.isalpha())

    def count_digits_in_chunk(self, start, size):
        chunk = self.file_handler.read_chunk(start, size)
        return sum(1 for char in chunk if char.isdigit())

    def count_spaces_in_chunk(self, start, size):
        chunk = self.file_handler.read_chunk(start, size)
        return sum(1 for char in chunk if char == ' ')
    
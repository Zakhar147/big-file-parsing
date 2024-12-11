class ChunkProcessor:
    def __init__(self, file_handler, chunk_size):
        self.file_handler = file_handler
        self.chunk_size = chunk_size

    def count_characters_in_chunk(self, start, size):
        chunk = self.file_handler.read_chunk(start, size)
        return len(chunk)     
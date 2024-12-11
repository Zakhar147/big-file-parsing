class ChunkProcessor:
    def __init__(self, file_handler, chunk_size):
        self.file_handler = file_handler
        self.chunk_size = chunk_size

    def count_all_in_chunk(self, start, size):
        chunk = self.file_handler.read_chunk(start, size)
        
        letters = sum(1 for char in chunk if char.isalpha())
        digits = sum(1 for char in chunk if char.isdigit())
        spaces = sum(1 for char in chunk if char == ' ')
        
        return {"letters": letters, "digits": digits, "spaces": spaces}    
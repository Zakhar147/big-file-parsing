import threading

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = self.calc_file_size()
        self.chunk_size = self.calc_chunk_size()

    def calc_file_size(self):
        """Calculate the size of the file."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            f.seek(0, 2)
            return f.tell()

    def calc_chunk_size(self):
        """Calculate an appropriate chunk size based on the file size."""
        if self.file_size <= 1024 * 1024:  # File size <= 1 MB
            return self.file_size
        return max(1024 * 1024, min(100 * 1024 * 1024, self.file_size // 100))

    def count_characters_in_chunk(self, start, size):
        """Count characters in a specific chunk."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            f.seek(start)
            chunk = f.read(size)
            return len(chunk)

    def process_in_threads(self):
        """Process the file in multiple threads to count characters."""
        chunks_amount = (self.file_size + self.chunk_size - 1) // self.chunk_size
        results = [0] * chunks_amount
        threads = []

        for i in range(chunks_amount):
            start = i * self.chunk_size
            size = min(self.chunk_size, self.file_size - start)
            thread = threading.Thread(
                target=lambda idx: results.__setitem__(idx, self.count_characters_in_chunk(start, size)),
                args=(i,)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results

    def calc_total_characters(self):
        """Calculate the total number of characters in the file."""
        results = self.process_in_threads()
        return sum(results)

    @staticmethod
    def get_usage():
        """Return usage instructions."""
        return """
        Usage: python file_parsing.py [txt_file]

        Arguments:
        - `file_parsing.py`: Path to the python file.
        - `txt_file`: Path to the txt file.
        """

    @staticmethod
    def validate_file_path(file_path):
        """Validate that the file is a .txt file."""
        if not file_path.endswith(".txt"):
            raise ValueError(f"Error! {file_path} is not a txt file!")

    def process_file(self):
        """Process the file and return the total character count."""
        self.validate_file_path(self.file_path)
        return f"Total characters in file: {self.calc_total_characters()}"

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(FileProcessor.get_usage())
    else:
        file_path = sys.argv[1]
        try:
            processor = FileProcessor(file_path)
            print(processor.process_file())
        except Exception as e:
            print(e)

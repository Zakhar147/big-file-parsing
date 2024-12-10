import threading

from modules.calc.calc import calc_chunk_size, calc_file_size

from modules.validate.validate import validate_file_path

class FileParse:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = calc_file_size(self.file_path)
        self.chunk_size = calc_chunk_size(self.file_size)
        
    def count_characters_in_chunk(self, start, size):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            f.seek(start)
            chunk = f.read(size)
            return len(chunk)
        
    def thread_task(self, idx, start, size, results):
        results[idx] = self.count_characters_in_chunk(start, size)

    def process_in_threads(self):
        chunks_amount = (self.file_size + self.chunk_size - 1) // self.chunk_size
        results = [0] * chunks_amount
        threads = []

        for i in range(chunks_amount):
            start = i * self.chunk_size
            size = min(self.chunk_size, self.file_size - start)
            thread = threading.Thread(
                target=self.thread_task,
                args=(i, start, size, results)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return results
    
    def calc_total_characters(self):
        results = self.process_in_threads()
        return sum(results)
    
    def parse_file(self):
        validate_file_path(self.file_path)
        return f"Total characters in file: {self.calc_total_characters()}"

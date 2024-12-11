import threading

class ThreadManager:
    def __init__(self, chunk_size, file_size, task):
        self.num_chunks = (file_size + chunk_size - 1) // chunk_size
        self.chunk_size = chunk_size
        self.file_size = file_size
        self.task = task

    def prepare_thread_data(self):
        thread_data = []
        for i in range(self.num_chunks):
            start = i * self.chunk_size
            size = min(self.chunk_size, self.file_size - start)
            thread_data.append((i, start, size))
        return thread_data

    def start_threads(self, thread_data, chunk_processor, count_type, results):
        threads = []
        for idx, start, size in thread_data:
            thread = threading.Thread(
                target=self.task,
                args=(chunk_processor, count_type, idx, start, size, results)
            )
            threads.append(thread)
            thread.start()
        return threads

    def join_threads(self, threads):
        for thread in threads:
            thread.join()

    def run_threads_for_type(self, chunk_processor, count_type):
        results = [0] * self.num_chunks
        thread_data = self.prepare_thread_data()
        threads = self.start_threads(thread_data, chunk_processor, count_type, results)
        self.join_threads(threads)
        return sum(results)
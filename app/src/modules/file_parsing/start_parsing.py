from modules.file_parsing.FileHandler import FileHandler
from modules.file_parsing.ChunkProcessor import ChunkProcessor
from modules.file_parsing.TheardManager import ThreadManager

from modules.tasks.theard_task import thread_task

def start_parsing(file_path):
    file = FileHandler(file_path)
    
    chunk_processor = ChunkProcessor(file, file.chunk_size)
        
    thread_manager = ThreadManager(file.chunk_size, file.file_size, 
                                   lambda idx, start, size, results: thread_task(chunk_processor, idx, start, size, results))
        
    results = thread_manager.run_threads_and_get_results()
    return f"Total characters in file: {sum(results)}"

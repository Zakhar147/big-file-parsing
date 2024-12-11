from modules.file_parsing.FileHandler import FileHandler
from modules.file_parsing.ChunkProcessor import ChunkProcessor
from modules.file_parsing.TheardManager import ThreadManager

from modules.tasks.theard_task import thread_task
from modules.utils.make import make_layout

def start_parsing(file_path):
    file = FileHandler(file_path)
    chunk_processor = ChunkProcessor(file, file.chunk_size)

    thread_manager = ThreadManager(
        file.chunk_size, 
        file.file_size, 
        thread_task
    )

    total_letters = thread_manager.run_threads_for_type(chunk_processor, 'letters')
    # total_digits = thread_manager.run_threads_for_type(chunk_processor, 'digits')
    # total_spaces = thread_manager.run_threads_for_type(chunk_processor, 'spaces')

    return (
        f"\nTotal characters breakdown:\n"
        f"- Letters: {total_letters}\n"
        # f"- Digits: {total_digits}\n"
        # f"- Spaces: {total_spaces}"
    )
def thread_task(chunk_processor, idx, start, size, results):
     results[idx] = chunk_processor.count_all_in_chunk(start, size)
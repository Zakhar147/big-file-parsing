def thread_task(chunk_processor, count_type, idx, start, size, results):
    if count_type == 'letters':
        results[idx] = chunk_processor.count_letters_in_chunk(start, size)
    elif count_type == 'digits':
        results[idx] = chunk_processor.count_digits_in_chunk(start, size)
    elif count_type == 'spaces':
        results[idx] = chunk_processor.count_spaces_in_chunk(start, size)
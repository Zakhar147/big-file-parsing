def calc_file_size(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(0, 2)
        return f.tell()

def calc_chunk_size(file_size):
    if file_size <= 1024 * 1024:  # File size <= 1 MB
        return file_size
    return max(1024 * 1024, min(100 * 1024 * 1024, file_size // 100))
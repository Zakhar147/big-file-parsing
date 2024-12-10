import threading
import sys

def get_usage(): 
    return """
    Usage: *python file_parsing.py [txt_file]*

    Arguments:
    - `file_parsing.py`: Path to the python file.
    - `txt_file`: Path to the txt file.
"""

def calc_file_size(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(0, 2)
        return f.tell()

def calc_chunk_size(file_size):
    if file_size <= 1024 * 1024:  # Если файл меньше 1 МБ
        return file_size
    return max(1024 * 1024, min(100 * 1024 * 1024, file_size // 100))

def count_characters_in_chunk(file_path, start, size):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(start)
        chunk = f.read(size)
        return len(chunk)

def process_file_in_threads(file_path, chunk_size):
    file_size = calc_file_size(file_path)
    chunks_amount = (file_size + chunk_size - 1) // chunk_size

    results = [0] * chunks_amount
    threads = []

    for i in range(chunks_amount):
        start = i * chunk_size
        size = min(chunk_size, file_size - start)
        thread = threading.Thread(
            target=lambda idx: results.__setitem__(idx, count_characters_in_chunk(file_path, start, size)),
            args=(i,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def calc_total_characters(results):
    return sum(results)

def main():
    usage_message = get_usage()
    
    if len(sys.argv) != 2:
        return usage_message
    
    file_path = sys.argv[1]
    
    try: 
        if not file_path.endswith(".txt"):
            raise ValueError(f"Error! {file_path} is not txt file!")
    except ValueError as V:
        return str(V)   
    
    file_size = calc_file_size(file_path)
    chunk_size = calc_chunk_size(file_size)
    
    results = process_file_in_threads(file_path, chunk_size)
    
    total_characters = calc_total_characters(results)
    return f"Total characters in file: {total_characters}"

if __name__ == "__main__":
    print(main())

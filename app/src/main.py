import threading

def count_characters_in_chunk(file_path, start, size, results, index):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(start)
        chunk = f.read(size)
        results[index] = len(chunk) 

def main():
    file_path = 'large_file.txt'  
    chunk_size = 1024 * 1024  # Размер блока (1 МБ)
    results = []  # Список для хранения результатов от потоков
    threads = []

    # Определяем размер файла
    file_size = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(0, 2)  # Переместиться в конец файла
        file_size = f.tell()

    # Создание потоков для обработки частей файла
    num_chunks = (file_size + chunk_size - 1) // chunk_size
    for i in range(num_chunks):
        start = i * chunk_size
        size = min(chunk_size, file_size - start)
        results.append(0)  # Резервируем место для результата
        thread = threading.Thread(target=count_characters_in_chunk, args=(file_path, start, size, results, i))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Подсчёт итогового результата
    total_characters = sum(results)
    print(f"Total characters in file: {total_characters}")

if __name__ == "__main__":
    main()
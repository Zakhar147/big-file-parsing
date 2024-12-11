import sys
import time
from tqdm import tqdm

from modules.utils.make import make_usage
from modules.file_parsing.start_parsing import start_parsing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(make_usage())
    else:
        file_path = sys.argv[1]
        try:
            with tqdm(total=100, desc="Prarsing file", unit="%", colour="green") as pbar:
                start_time = time.time() 
                
                parsing_result = start_parsing(file_path)
                
                end_time = time.time() 
                elapsed_time = end_time - start_time  
                
                for _ in range(10):
                    time.sleep(0.1)
                    pbar.update(10)
                
            print(parsing_result)
            print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
        except Exception as e:
            print(e)

import sys

from modules.utils.utils import get_usage
from modules.file_parsing.start_parsing import start_parsing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(get_usage())
    else:
        file_path = sys.argv[1]
        try:
            parsing_result = start_parsing(file_path)
            print(parsing_result)
        except Exception as e:
            print(e)

import sys

from modules.parse.file_parse import FileParse

from modules.utils.utils import get_usage


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(get_usage())
    else:
        file_path = sys.argv[1]
        try:
            parser = FileParse(file_path)
            print(parser.parse_file())
        except Exception as e:
            print(e)

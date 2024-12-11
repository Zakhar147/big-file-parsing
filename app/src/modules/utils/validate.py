def validate_file_path(file_path):
    if not file_path.endswith(".txt"):
        raise ValueError(f"Error! {file_path} is not a txt file!")
def make_usage():
    return """
    Usage: python file_parsing.py [txt_file]

    Arguments:
    - `file_parsing.py`: Path to the python file.
    - `txt_file`: Path to the txt file.
    """
    
def make_result_container(num_chunks):
    return [{} for _ in range(num_chunks)]

def make_layout(results):
    total_counts = {"letters": 0, "digits": 0, "spaces": 0}
    for result in results:
        for key in total_counts:
            total_counts[key] += result.get(key, 0)
            
    return (
        f"Total characters breakdown:\n"
        f"- Letters: {total_counts['letters']}\n"
        f"- Digits: {total_counts['digits']}\n"
        f"- Spaces: {total_counts['spaces']}"
    )
    
from typing import List


def format_output(what_to_format: List[str]) -> str:
    tabulated_what_to_format = [f"\t{line}" for line in what_to_format]
    return "\n".join(tabulated_what_to_format)

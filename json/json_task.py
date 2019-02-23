import re


def plain_text_regex_number_add_up():
    """Adds infile numbers up returns sum of all numbers."""
    with open('input.txt', 'r') as f:
        return sum(map(int, re.findall(r'(\-?\d+)', f.read())))


if __name__ == '__main__':
    print(plain_text_regex_number_add_up())


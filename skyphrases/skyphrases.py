def how_many_phrases_are_valid():
    """Coounts valid passwords (lines) from a document,
    returns count of valid lines."""
    with open('input.txt', 'r') as f:
        phrases = [line.split() for line in f.readlines()]
        return sum([0 if len(line) != len(set(line)) else 1 for line in phrases])


if __name__ == '__main__':
    print(how_many_phrases_are_valid())

def sequential_pattern_match(tokens):
    for first, rest in _splits(tokens):
        x = _halves_match(first, rest)
        if x:
            return x

def _splits(tokens):
    for i in xrange(min(len(tokens), MAX_PATTERN_LENGTH), 0, -1):
        yield tokens[:i], tokens[i:]

def _halves_match(first, rest):
    tag = test(first)
    if tag:
        return [(first, tag)] + (rest and sequential_pattern_match(rest))

def test(tokens):
    length = len(tokens)
    if length == 1:
        if tokens[0] == "Nexium":
            return "MEDICINE"
        elif tokens[0] == "pain":
            return "SYMPTOM"
        else:
            return "O"
    elif length == 2:
        if tokens == ["Barium", "Swallow"]:
            return "INTERVENTION"
        elif tokens == ["Swallow", "Test"]:
            return "INTERVENTION"
    elif tokens == ["pain", "in", "stomach"]:
        return "SYMPTOM"
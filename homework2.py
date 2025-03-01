def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

def run_tests():
    test_cases = [
        ("AAAA", 3),
        ("BBBBB", 4),
        ("ABABABAB", 0),
        ("BABABA", 0),
        ("AAABBB", 4),
        ("A", 0),
        ("", 0),
        ("ABBA", 1),
        ("ABABABAAB", 1),
        ("AABBCC", 3)
    ]
    
    for s, expected in test_cases:
        result = alternatingCharacters(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
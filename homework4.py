def lenIfValidResult(s, charA, charB):
    last_char = None
    count = 0
    for char in s:
        if char == charA or char == charB:
            if char == last_char:
                return 0
            count += 1
            last_char = char
    return count

def alternate(s):
    max_len = 0
    unique_chars = list(set(s))
    n = len(unique_chars)
    
    if n <= 1:
        return 0
    
    for i in range(n):
        for j in range(i + 1, n):
            charA = unique_chars[i]
            charB = unique_chars[j]
            result_len = lenIfValidResult(s, charA, charB)
            max_len = max(max_len, result_len)
    
    return max_len

def run_tests():
    test_cases = [
        ("beabeefeab", 5),
        ("asdcbsdcagfsdbgdfanfghbsfdab", 8),
        ("asvkugfiugsalddlasguifgukvsa", 0),
        ("aaaa", 0),
        ("ababab", 6),
        ("abcabcabc", 6),
        ("a", 0),
        ("", 0),
        ("ab", 2),
        ("abc", 2)
    ]
    
    for s, expected in test_cases:
        result = alternate(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
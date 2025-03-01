def funnyString(s):
    # Reverse the string
    r = s[::-1]
    
    # Calculate differences for the original string
    original_diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    
    # Calculate differences for the reversed string
    reversed_diffs = [abs(ord(r[i]) - ord(r[i-1])) for i in range(1, len(r))]
    
    # Compare differences
    if original_diffs == reversed_diffs:
        return "Funny"
    else:
        return "Not Funny"

def run_tests():
    test_cases = [
        ("acxz", "Funny"),
        ("bcxz", "Not Funny"),
        ("abcd", "Funny"),
        ("a", "Funny"),
        ("aa", "Funny"),
        ("ab", "Funny"),
        ("ba", "Funny"),
        ("abcba", "Funny"),
        ("abccba", "Funny"),
        ("abccbx", "Not Funny")
    ]
    
    for s, expected in test_cases:
        result = funnyString(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
def caesarCipher(s, k):
    code = ""
    k = k % 26
    for char in s:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            code += chr((ord(char) - shift + k) % 26 + shift)
        else:
            code += char
    return code

def run_tests():
    test_cases = [
        ("middle-Outz", 2, "okffng-Qwvb"),
        ("Always-Look-on-the-Bright-Side-of-Life", 5, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"),
        ("A", 1, "B"),
        ("a", 1, "b"),
        ("Z", 1, "A"),
        ("z", 1, "a"),
        ("", 1, ""),
        ("abc", 0, "abc"),
        ("xyz", 3, "abc"),
        ("Hello, World!", 13, "Uryyb, Jbeyq!")
    ]
    
    for s, k, expected in test_cases:
        result = caesarCipher(s, k)
        assert result == expected, f"Test failed for input {s} with shift {k}: expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
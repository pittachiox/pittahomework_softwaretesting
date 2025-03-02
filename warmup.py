def staircase(n, display="#"):
    if n <= 0 or n > 30:
        raise ValueError("n must be between 1 and 30")
    
    result = []
    for i in range(1, n + 1):
        # เพิ่มอักขระ display จำนวน i ครั้ง และขึ้นบรรทัดใหม่
        result.append(display * i)
    return "\n".join(result)

def run_tests():
    test_cases = [
        (1, "#", "#"),
        (2, "#", "#\n##"),
        (3, "#", "#\n##\n###"),
        (4, "*", "*\n**\n***\n****"),
        (5, "@", "@\n@@\n@@@\n@@@@\n@@@@@"),
        (0, "#", ValueError),  # ค่าผิดพลาด
        (31, "#", ValueError)  # ค่าผิดพลาด
    ]
    
    for n, display, expected in test_cases:
        try:
            result = staircase(n, display)
            assert result == expected, f"Test failed for input {n}, {display}: expected {expected}, got {result}"
        except ValueError as e:
            assert expected == ValueError, f"Test failed for input {n}, {display}: expected ValueError, got {e}"
    
    print("All tests passed!")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    run_tests()
    
    n = int(input("Enter the size of the staircase (0 < n <= 30): "))
    display = input("Enter the display character (default is '#'): ") or "#"
    print(staircase(n, display))
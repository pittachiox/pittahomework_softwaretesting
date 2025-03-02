def staircase(n, display="#"):
    if n <= 0 or n > 30:
        raise ValueError("n must be between 1 and 30")
    
    result = []
    for i in range(1, n + 1):
        # เพิ่มอักขระ display จำนวน i ครั้ง และขึ้นบรรทัดใหม่
        result.append(display * i)
    return "\n".join(result)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    n = int(input("Enter the size of the staircase (0 < n <= 30): "))
    display = input("Enter the display character (default is '#'): ") or "#"
    print(staircase(n, display))
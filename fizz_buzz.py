x = int(input("input x : "))
def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

# Test cases
def test_fizzbuzz():
    # กรณีที่ x หารด้วย 3 และ 5 ลงตัว (FizzBuzz)
    assert fizzbuzz(15) == "FizzBuzz", "Test case 1 failed"
    
    # กรณีที่ x หารด้วย 3 ลงตัว (Fizz)
    assert fizzbuzz(9) == "Fizz", "Test case 2 failed"
    
    # กรณีที่ x หารด้วย 5 ลงตัว (Buzz)
    assert fizzbuzz(10) == "Buzz", "Test case 3 failed"
    
    # กรณีที่ x ไม่หารด้วย 3 หรือ 5 ลงตัว
    assert fizzbuzz(7) == 7, "Test case 4 failed"
    
    # กรณีที่ x เป็นศูนย์
    assert fizzbuzz(0) == "FizzBuzz", "Test case 5 failed"
    
    # กรณีที่ x เป็นจำนวนลบและหารด้วย 3 ลงตัว
    assert fizzbuzz(-6) == "Fizz", "Test case 6 failed"
    
    # กรณีที่ x เป็นจำนวนลบและหารด้วย 5 ลงตัว
    assert fizzbuzz(-10) == "Buzz", "Test case 7 failed"
    
    # กรณีที่ x เป็นจำนวนลบและไม่หารด้วย 3 หรือ 5 ลงตัว
    assert fizzbuzz(-7) == -7, "Test case 8 failed"
    
    print("All test cases passed!")

# รันการทดสอบ
test_fizzbuzz()


# result = fizzbuzz(x)
# print(result)
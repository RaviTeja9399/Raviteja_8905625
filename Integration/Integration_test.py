import larger_number

def test_c_larger_number():
 assert larger_number == num1 or larger_number == num2, "Incorrect result"
if num1 > num2:
    assert larger_number == num1, "Incorrect larger number"
else:
    assert larger_number == num2, "Incorrect larger number"

# Assert statements to validate the result
assert larger_number == num1 or larger_number == num2, "Incorrect result"
if num1 > num2:
    assert larger_number == num1, "Incorrect larger number"
else:
    assert larger_number == num2, "Incorrect larger number"

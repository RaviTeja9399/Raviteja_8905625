import list_sum
 
def test_list_sum():
    list_nos = [1, 2, 3, 4, 5]
    result = list_sum.list_sum_no(list_nos)
 
    assert result == 15, f"Error: The calculated sum {result} is not equal to the expected result 15"
 

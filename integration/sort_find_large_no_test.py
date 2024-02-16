[12:45 PM] Jaskirat Kaur
import find_large
 
def test_cube_root():
    list_val = [10, 20, 4, 45, 99]
    result = find_large.find_large_no(list_val)
 
    assert result == 79, f"Error: The number {result} is not largest. Expected result 99"
 

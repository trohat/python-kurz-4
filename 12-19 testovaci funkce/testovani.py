
test_number = 0

def test_equality(calculated, expected):
    global test_number
    test_number += 1  
    
    if calculated == expected:
        print("\033[92m", "\033[103m", f"Testxx no.{test_number} passed.", "\033[0m")
    else:
        print("\033[91m", f"Test no.{test_number} did not pass.", "\033[0m")
        print("\033[93m", f"Computed value: {calculated}", "\033[0m")
        print("\033[93m", f"Expected value: {expected}", "\033[0m")
     
num_test_cases = int(input())

for _ in range(num_test_cases):
    # Read the number of elements in set A
    num_elements_a = int(input())
    # Read the elements of set A
    set_a = set(map(int, input().split()))
    
    num_elements_b = int(input())
    set_b = set(map(int, input().split()))
    
    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")

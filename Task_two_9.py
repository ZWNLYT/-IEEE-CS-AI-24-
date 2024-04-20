def find_common_elements(set1, set2):
    return set1.intersection(set2)

set1_input = input("Enter elements of the first set separated by spaces: ")
set1 = set(set1_input.split())
set2_input = input("Enter elements of the second set separated by spaces: ")
set2 = set(set2_input.split())

common_elements = find_common_elements(set1, set2)
print("Common elements:", common_elements)

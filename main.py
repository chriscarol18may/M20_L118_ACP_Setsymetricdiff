def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example A
set1_A = {'blue', 'green'}
set2_A = {'blue', 'yellow'}
symmetric_diff_A = find_symmetric_difference(set1_A, set2_A)
print(f"Symmetric difference for Set1_A and Set2_A: {symmetric_diff_A}")

# Example B
set1_B = {1, 2, 3, 4, 5}
set2_B = {1, 5, 6, 7, 8, 9}
symmetric_diff_B = find_symmetric_difference(set1_B, set2_B)
print(f"Symmetric difference for Set1_B and Set2_B: {symmetric_diff_B}")
def calculate_jumbo_javelin_length(num_rods, rod_lengths):
    total_length = sum(rod_lengths)
    fused_length = total_length - (num_rods - 1)
    return fused_length

num_rods = int(input())
rod_lengths = [int(input()) for _ in range(num_rods)]


jumbo_javelin_length = calculate_jumbo_javelin_length(num_rods, rod_lengths)
print(jumbo_javelin_length)

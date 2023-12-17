def count_steps_back(heights):
    steps = 0
    line = []

    for height in heights:
        idx = len(line)
        for i, h in enumerate(line):
            if h > height:
                idx = i
                break
        line.insert(idx, height)
        steps += len(line) - (idx + 1)

    return steps

num_datasets = int(input())

for _ in range(num_datasets):
    dataset_num, *heights = map(int, input().split())
    steps = count_steps_back(heights)
    print(dataset_num, steps)
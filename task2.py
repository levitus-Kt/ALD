def longest_increasing_streak(nums: list[int]) -> dict:
    if not nums:
        return {"length": 0, "streak": []}

    max_length = 1
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            start_index = i
            current_length = 1

    if current_length > max_length:
        max_length = current_length
        max_start_index = start_index

    if max_length < 2:
        return {"length": 0, "streak": []}

    last = max_start_index + max_length

    return {
        "length": max_length,
        "streak": nums[max_start_index:last],
    }


nums = [1, 3, 3, 5, 5, 4, 7]
print(longest_increasing_streak(nums))

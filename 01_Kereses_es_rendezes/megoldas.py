def count_subarrays_with_at_most_k_distinct(n, k, array):

    left = 0
    count = 0
    freq = {}
    distinct_count = 0

    for right in range(n):
        if array[right] not in freq:
            freq[array[right]] = 0
        if freq[array[right]] == 0:
            distinct_count += 1
        freq[array[right]] += 1

        while distinct_count > k:
            freq[array[left]] -= 1
            if freq[array[left]] == 0:
                distinct_count -= 1
            left += 1

        count += right - left + 1

    return count

#Bemenet
n, k = map(int, input().split())
array = list(map(int, input().split()))

#Kimenet
print(count_subarrays_with_at_most_k_distinct(n, k, array))
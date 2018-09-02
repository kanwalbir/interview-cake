# Input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# Output: [(0, 1), (3, 8), (9, 12)]


# Time: O(nlogn)
# Space: O(n)

def merge_ranges(times):
    sorted_times = sorted(times, key=lambda tup: tup[0])
    output = [sorted_times[0]]

    for k in range(1, len(sorted_times)):
        if output[-1][1] < sorted_times[k][0]:
            output.append(sorted_times[k])
        else:
            output[-1] = (output[-1][0], max(sorted_times[k][1], output[-1][1]))

    return output


times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
merge_ranges(times)

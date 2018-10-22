# Time: O(n)
# Space: O(n)


def sort_scores(unsorted_scores, H_SCORE):
    
    scores_count = [0] * (H_SCORE + 1)

    for score in unsorted_scores:
        scores_count[score] += 1
    
    sorted_scores = []

    for i in range(H_SCORE - 1, -1, -1):
        for _ in range(scores_count[i]):
            sorted_scores.append(i)

    return sorted_scores


print(sort_scores([37, 89, 41, 65, 91, 53], 100))  # [91, 89, 65, 53, 41, 37]
print(sort_scores([90, 90, 90, 90, 90, 90], 100))  # [90, 90, 90, 90, 90, 90]
print(sort_scores([0, 0, 0, 0, 0, 0], 100))  # [0, 0, 0, 0, 0, 0]
print(sort_scores([20, 10, 30, 30, 10, 20], 100))  # [30, 30, 20, 20, 10, 10]
print(sort_scores([], 100))  # []

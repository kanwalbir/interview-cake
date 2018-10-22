# Time: O(n)
# Space: O(n)

from collections import defaultdict


def can_two_movies_fill_flight(flight_length, movie_lengths):

    lengths = defaultdict(int)
    half_flight = flight_length / 2

    for curr_movie in movie_lengths:
        lengths[curr_movie] += 1
        if flight_length - curr_movie in lengths and curr_movie != half_flight:
            return True
        elif curr_movie == half_flight and lengths[curr_movie] > 1:
            return True

    return False


print(can_two_movies_fill_flight(5.5, []))  # False
print(can_two_movies_fill_flight(5.5, [2.5, 2, 1, 0]))  # False
print(can_two_movies_fill_flight(5.5, [2.5, 3, 1, 0]))  # True
print(can_two_movies_fill_flight(5.0, [2.5, 2.5, 1, 0]))  # True
print(can_two_movies_fill_flight(5.0, [2.5, 1.5, 1, 0]))  # False
print(can_two_movies_fill_flight(5.0, [5.0]))  # False
print(can_two_movies_fill_flight(5.0, [5.0, 0.0]))  # True

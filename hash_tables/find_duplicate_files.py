# Time: O(n) => O(b) where b is related to size of files
# Space: O(n)

import os
import hashlib


def create_file_hash(path):

    hasher = hashlib.sha256()

    with open(path, 'rb') as f:
        hasher.update(f.read())

    return hasher.hexdigest()


def find_duplicate_files(start):
    
    to_visit = [start]
    files_visited = {}
    duplicates = []

    while to_visit:
        curr = to_visit.pop()

        if os.path.isdir(curr):
            for child in os.listdir(curr):
                if child.startswith('.') is False:
                    to_visit.append(curr + '/' + child)
        else:
            file_hash = create_file_hash(curr)
            modified_time = os.path.getmtime(curr)

            if file_hash in files_visited:
                if modified_time > files_visited[file_hash][1]:
                    duplicates.append((curr, files_visited[file_hash][0]))
                else:
                    duplicates.append((files_visited[file_hash][0], curr))
            else:
                files_visited[file_hash] = (curr, modified_time)

    return duplicates


path1 = ''
print(find_duplicate_files(path1))

from collections import defaultdict, deque
import re
import heapq

def build_optimized_adjacency_list(entries):
    word_set = set(entries.keys())
    inverted_index = defaultdict(set)

    for key, definition in entries.items():
        words_in_def = set(re.findall(r'\b[a-z]+\b', definition))
        for w in words_in_def:
            if w in word_set:
                inverted_index[w].add(key)

    adj = defaultdict(list)
    checked = set()

    for w1 in entries:
        for w2 in inverted_index[w1]:
            if w1 == w2 or (w2, w1) in checked:
                continue

            count1 = len(re.findall(rf'\b{re.escape(w2)}\b', entries[w1]))
            count2 = len(re.findall(rf'\b{re.escape(w1)}\b', entries[w2]))
            weight = count1 + count2
            if weight > 0:
                adj[w1].append((w2, weight))
                adj[w2].append((w1, weight))
            checked.add((w1, w2))

    return adj


entries = {}

with open('dict_simplified.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tokens = line.strip().split(maxsplit=1)
        if len(tokens) == 2:
            word, definition = tokens
            entries[word] = definition

adj_list = build_optimized_adjacency_list(entries)


num_vertices = len(adj_list)
num_edges = sum(len(neighbors) for neighbors in adj_list.values()) // 2  # 무방향이므로 나누기 2
print("Answer1:", num_vertices, num_edges)

max_degree_word = max(adj_list.items(), key=lambda x: len(x[1]))
print("Answer2:", max_degree_word[0], len(max_degree_word[1]))

def get_largest_component_size(adj):
    visited = set()
    max_size = 0
    for node in adj:
        if node not in visited:
            stack = [node]
            component = set()
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                component.add(curr)
                stack.extend([nei for nei, _ in adj[curr]])
            max_size = max(max_size, len(component))
    return max_size

print("Answer3:", get_largest_component_size(adj_list))

def words_within_distance_k(adj, start, k):
    result = []
    visited = set()
    q = deque()
    q.append((start, 0.0))

    while q:
        node, dist = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        if dist <= k:
            result.append(node)
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                q.append((neighbor, dist + 1 / weight))
    return result, len(result)

print('Answer4:')
words, count = words_within_distance_k(adj_list, "mountain", 2)
print("\n".join(words))
print(count)

def shortest_path(adj, start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, node, path = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return path, cost
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + 1 / weight, neighbor, path))
    return None, float('inf')

print('Answer5:')
path, dist = shortest_path(adj_list, "parity", "parcel")
print(" <==> ".join(path))
print("Distance:", round(dist, 2))
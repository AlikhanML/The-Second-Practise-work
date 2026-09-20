from collections import deque

network = {
    "Алихан": ["Бекжан", "Дина"],
    "Бекжан": ["Алихан", "Ернар", "Мадина"],
    "Дина": ["Алихан", "Мадина"],
    "Ернар": ["Бекжан"],
    "Мадина": ["Бекжан", "Дина", "Азамат"],
    "Азамат": ["Мадина"],
}


def bfs_algo(network, start, goal):
  queue = deque([(start, [start])])
  visited = {start}
  traversal_order = []  # 1. Барлық тексерілген адамдарды сақтайтын тізім

  while queue:
    current_person, path = queue.popleft()
    traversal_order.append(current_person)  # 2. Тексеріліп жатқан адамды тіркеу

    if current_person == goal:
      return traversal_order, path  # Екеуін де қайтарамыз

    for friend in network.get(current_person, []):
      if friend not in visited:
        visited.add(friend)
        queue.append((friend, path + [friend]))

  return traversal_order, []


start = "Алихан"
goal = "Азамат"

order, result_path = bfs_algo(network, start, goal)

print(f"Start: {start}")
print(f"Main Goal: {goal}\n")

print("1. Traversal Order (Алгоритмнің тексеру реті):")
print(" - ".join(order))

print("\n2. Табылған ең қысқа дос тізбегі (Shortest Path):")
print(" - ".join(result_path))
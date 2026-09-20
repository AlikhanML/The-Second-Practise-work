network = {
    "Алихан": ["Бекжан", "Дина"],
    "Бекжан": ["Алихан", "Ернар", "Мадина"],
    "Дина": ["Алихан", "Мадина"],
    "Ернар": ["Бекжан"],
    "Мадина": ["Бекжан", "Дина", "Азамат"],
    "Азамат": ["Мадина"],
}


def dfs_algo(graph, start, goal):
  stack = [(start, [start])]
  visited = set()
  traversal_order = []

  while stack:
    current_person, path = stack.pop() 

    if current_person not in visited:
      visited.add(current_person)
      traversal_order.append(current_person)

      if current_person == goal:
        return traversal_order, path

      for friend in reversed(graph.get(current_person, [])):
        if friend not in visited:
          stack.append((friend, path + [friend]))

  return traversal_order, []


start = "Алихан"
goal = "Азамат"

order, result_path = dfs_algo(network, start, goal)

print(f"Start: {start}")
print(f"Main Goal: {goal}\n")

print("1. DFS Traversal Order (Алгоритмнің тексеру реті):")
print(" -> ".join(order))

print("\n2. Табылған жол (DFS Path):")
print(" - ".join(result_path))
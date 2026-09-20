import heapq
network = {
    "Алихан": {"Бекжан": 2, "Дина": 5},
    "Бекжан": {"Алихан": 2, "Ернар": 3, "Мадина": 1},
    "Дина": {"Алихан": 5, "Мадина": 2},
    "Ернар": {"Бекжан": 3},
    "Мадина": {"Бекжан": 1, "Дина": 2, "Азамат": 4},
    "Азамат": {"Мадина": 4},
}


def ucs_algo(graph, start, goal):
  pq = [(0, start, [start])]
  visited = set()
  traversal_order = []

  while pq:
    cost, current_person, path = heapq.heappop(pq)

    if current_person not in visited:
      visited.add(current_person)
      traversal_order.append(current_person)

      if current_person == goal:
        return traversal_order, path, cost

      for neighbor, weight in graph.get(current_person, {}).items():
        if neighbor not in visited:
          heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

  return traversal_order, [], float("inf")


start = "Алихан"
goal = "Азамат"

order, result_path, total_cost = ucs_algo(network, start, goal)

print(f"Start: {start}")
print(f"Main Goal: {goal}\n")

print("1. UCS Traversal Order (Тексеру реті):")
print(" -> ".join(order))

print(f"\n2. Табылған ең арзан жол (Жалпы құны / Total Cost: {total_cost}):")
print(" - ".join(result_path))
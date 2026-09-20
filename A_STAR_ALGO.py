import heapq

network = {
    "Алихан": {"Бекжан": 2, "Дина": 5},
    "Бекжан": {"Алихан": 2, "Ернар": 3, "Мадина": 1},
    "Дина": {"Алихан": 5, "Мадина": 2},
    "Ернар": {"Бекжан": 3},
    "Мадина": {"Бекжан": 1, "Дина": 2, "Азамат": 4},
    "Азамат": {"Мадина": 4},
}

heuristic = {"Алихан": 5, "Бекжан": 3, "Дина": 3, "Ернар": 5, "Мадина": 4, "Азамат": 0}


def a_star_algo(graph, h, start, goal):
  pq = [(h[start], 0, start, [start])]
  visited = set()
  traversal_order = []

  while pq:
    f, g, current_person, path = heapq.heappop(pq)

    if current_person not in visited:
      visited.add(current_person)
      traversal_order.append(current_person)

      if current_person == goal:
        return traversal_order, path, g
      for neighbor, weight in graph.get(current_person, {}).items():
        if neighbor not in visited:
          g_new = g + weight  # Жіберілген нақты құн (g)
          h_new = h.get(
              neighbor, 0 )
          f_new = g_new + h_new  # f = g + h

          heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

  return traversal_order, [], float("inf")


start = "Алихан"
goal = "Азамат"
order, result_path, total_cost = a_star_algo(network, heuristic, start, goal)

print(f"Start: {start}")
print(f"Main Goal: {goal}\n")

print("1. A* Traversal Order (Тексеру реті):")
print(" -> ".join(order))

print(f"\n2. A* арқылы табылған ең тиімді жол (Жалпы құны / Total Cost: {total_cost}):")
print(" - ".join(result_path))
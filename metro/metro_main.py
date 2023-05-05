class metro_line:
    def __init__(self, id, hex_color, name, stations) -> None:
        self.id = id
        self.hex_color = hex_color
        self.name = name
        self.stations = stations
    def __str__(self) -> str:
        return self.name

class metro_station:
    def __init__(self, id, name, lat, lng, order, line) -> None:
        self.id = id
        self.name = name
        self.lat = lat
        self.lng = lng
        self.order = order
        self.line = line
    def __str__(self) -> str:
        return self.name

with open('метро спб.json', 'r', encoding="utf-8") as f:
    lines = f.readlines()
metro_stations = []
metro_lines = []
for str in lines:
    spltdstr = str.split('":"|","')
    for w in spltdstr:
    #         c = w.split(':')
    # new_line=metro_line()
    # metro_lines.append(new_line)
        print(w)
# print (lines)
import matplotlib.pyplot as plt
import networkx as nx







# G = nx.Graph()  # создаём объект графа

# # определяем список узлов (ID узлов)
# nodes = [1, 2, 3, 4, 5]

# # определяем список рёбер
# # список кортежей, каждый из которых представляет ребро
# # кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
# edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]

# # добавляем информацию в объект графа
# G.add_nodes_from(nodes)
# G.add_edges_from(edges)

# # рисуем граф и отображаем его
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

import turtle 

class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = [(weight, node1, node2) for node1, node_list in graph.items() for node2, weight in node_list.items()]
    edges.sort()
    nodes = set(node for node_list in graph.values() for node in node_list)
    disjoint_set = DisjointSet(nodes)
    minimum_spanning_tree = []

    for edge in edges: #iterasi
        weight, node1, node2 = edge
        if disjoint_set.find(node1) != disjoint_set.find(node2):
            disjoint_set.union(node1, node2)
            minimum_spanning_tree.append((node1, node2, weight))

    return minimum_spanning_tree

def draw_graph(graph, mst, positions):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title("Algoritma Kruskal - MST")
    
    for frm, neighbors in graph.items():
        for to, weight in neighbors.items():
            if frm < to:
                draw_edge(frm, to, weight, positions, "gray", 1)
    
    for frm, to, weight in mst:
        draw_edge(frm, to, weight, positions, "red", 3)
    
    for node, position in positions.items():
        draw_node(node, position)
    
    turtle.done()

def draw_node(node, position):
    x, y = position
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.pendown()
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y - 10)
    turtle.pendown()
    turtle.write(str(node), align="center", font=("Arial", 12, "bold"))

def draw_edge(frm, to, weight, positions, color, pen_size=1):
    x1, y1 = positions[frm]
    x2, y2 = positions[to]
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.pensize(pen_size)
    turtle.goto(x2, y2)
    turtle.penup() 
    turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
    turtle.pendown()
    turtle.write(str(weight), align="center", font=("Arial", 12, "normal"))

def main1():
    node_count = 7 
    edge_count = 12 

    graph = {
        'A': {'B': 6, 'C': 6, 'D': 6}, 
        'B': {'A': 6, 'D': 3, 'E': 2}, 
        'C': {'A': 6, 'D': 7, 'F': 8}, 
        'D': {'A': 6, 'B': 3, 'C': 7, 'E': 2, 'F': 3, 'G': 4},
        'E': {'B': 2, 'D': 2, 'G': 3},
        'F': {'C': 8, 'D': 3, 'G': 1},
        'G': {'D': 4, 'E': 3, 'F': 1}
    }

    positions = {
        'A': (-50, 87),
        'B': (50, 87),
        'C': (-100, 0),
        'D': (0, 0),
        'E': (100, 0),
        'F': (-50, -87),
        'G': (50, -87)
    }

    minimum_spanning_tree = kruskal(graph) 

    total_distance = 0
    print("Minimum Spanning Tree (MST) untuk Graf 1:")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]}-{edge[1]}: {edge[2]}")
        total_distance += edge[2]

    print("Jarak Total:", total_distance)

    draw_graph(graph, minimum_spanning_tree, positions)

def main2():
    node_count = 10
    edge_count = 15

    graph = { 
        'A': {'B': 7, 'C': 6, 'E': 1},
        'B': {'A': 7, 'D': 12, 'F': 11},
        'C': {'A': 6, 'D': 8, 'J': 5},
        'D': {'B': 12, 'C': 8, 'H': 13},
        'E': {'A': 1, 'F': 2, 'I': 3},
        'F': {'B': 11, 'E': 2, 'G': 15},
        'G': {'F': 15, 'H': 14, 'I': 10},
        'H': {'D':13, 'G': 14, 'J': 9},
        'I': {'E': 3, 'G': 10, 'J': 4},
        'J': {'C': 5, 'H': 9, 'I': 4}
    }

    positions = { 
        'A': (0, 200),
        'B': (0, 100),
        'C': (100, 100),
        'D': (50, 50),
        'E': (-100, 0),
        'F': (-25, -75),
        'G': (50, -75),
        'H': (120, -75),
        'I': (-100, -200),
        'J': (100, -200)
    }

    minimum_spanning_tree = kruskal(graph)

    total_distance = 0
    print("Minimum Spanning Tree (MST) untuk Graf 2:")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]}-{edge[1]}: {edge[2]}")
        total_distance += edge[2]

    print("Jarak Total:", total_distance)

    draw_graph(graph, minimum_spanning_tree, positions)

if __name__ == "__main__":
    main2()
    

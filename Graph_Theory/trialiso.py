import random
import turtle

def create_graph(n):
  """Creates a random Euler graph with n vertices."""
  graph = {}
  for i in range(n):
    graph[i] = []
  for i in range(n - 1):
    u = random.randint(0, n - 1)
    v = random.randint(0, n - 1)
    while u == v or (u, v) in graph[u] or (v, u) in graph[v]:
      u = random.randint(0, n - 1)
      v = random.randint(0, n - 1)
    graph[u].append((v, random.randint(1, 10)))
    graph[v].append((u, random.randint(1, 10)))
  return graph

def draw_graph(graph, turtle_object):
  """Draws the Euler graph."""
  for u in graph:
    for v, weight in graph[u]:
      turtle_object.penup()
      turtle_object.goto(u * 20, 0)
      turtle_object.pendown()
      turtle_object.write(str(u), font=("Arial", 10, "normal"))
      turtle_object.goto(v * 20, 0)
      turtle_object.write(str(v), font=("Arial", 10, "normal"))
      turtle_object.penup()
      turtle_object.goto((u + v) * 20 / 2, -weight)
      turtle_object.pendown()
      turtle_object.circle(weight / 2)

def main():
  n = 10
  graph = create_graph(n)
  turtle_object = turtle.Turtle()
  turtle_object.speed(0)
  draw_graph(graph, turtle_object)
  turtle.done()

if __name__ == "__main__":
  main()

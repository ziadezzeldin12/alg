import heapq

def prim(graph, start):
    # عدد الرؤوس في الرسم البياني
    V = len(graph)
    
    # initializations
    visited = [False] * V
    key = [float('inf')] * V
    parent = [-1] * V
    
    # priority queue (heap)
    pq = [(0, start)]  # (key, vertex)
    key[start] = 0
    
    while pq:
        # get the vertex with the minimum key value
        weight, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        # Mark the vertex as visited
        visited[u] = True
        
        # Process each neighbor of u
        for v, weight in graph[u]:
            if not visited[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))
    
    # Return the parent array that represents the MST
    return parent

# الإدخال من المستخدم
V = int(input("ادخل عدد الرؤوس في الجراف: "))
graph = [[] for _ in range(V)]

# إدخال الحواف من المستخدم
edges_count = int(input("ادخل عدد الحواف: "))
for _ in range(edges_count):
    u, v, weight = map(int, input("ادخل الحافة (الرأس1 الرأس2 الوزن) : ").split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # لأن الجراف غير موجه

start = int(input("ادخل الرقم الذي تريد البدء منه: "))

# تنفيذ خوارزمية Prim
parent = prim(graph, start)

# طباعة النتيجة
print("Parent array for MST:", parent)
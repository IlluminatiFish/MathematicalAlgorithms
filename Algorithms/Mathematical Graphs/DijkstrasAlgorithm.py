# Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# Algorithm to calculate shortest path between two points
def dijkstrasAlgorithm(graph, start, end):
    global length_short_route  # Define the shortest length globally so it can be used outside the algorithm functions scope i.e. in the output outside the function

    inf = float('inf')  # Infinity value
    distance = {}  # Distance dictionary
    previous_vertex = {}  # Dictionary which holds the previous vertex to the vertex being looked at
    route = []  # Shortest route as a list

    for vertex in graph:  # For a vertex in the graph

        distance[vertex] = inf  # Setting the distance of this vertex to infinity

    distance[start] = 0  # Set the value of the starting point to equal 0

    while graph:  # While graph exists, meaning until all the vertices have been passed through

        shortest = None  # Initialize the shortest variable

        for vertex in graph:  # Loop through each vertex in the graph
            if shortest is None:  # If shortest is not set
                shortest = vertex  # Set shortest to the current vertex
            elif distance[vertex] < distance[
                shortest]:  # If the distance of the current vertex is smaller the then distance of the shortest vertex then set the shortest to the vertex thats been worked on
                shortest = vertex  # Set shortest to the current vertex if the condition is met

        for neighbour, length in graph[shortest].items():  # Caluclate the shortest distance of each edge

            # If there is a neighbour to this vertex and check if the legnth of this edge and the shortest distance is less than the distance to the neighbouring vertex
            if neighbour in graph and (length + distance[shortest] < distance[neighbour]):
                distance[neighbour] = length + distance[
                    shortest]  # Add the length of the edge to the distance of the current shortest working path and set it to the distance of the neighbouring vertex
                previous_vertex[
                    neighbour] = shortest  # Set the previous neighbouring vertex to be the current shortest final vertex

        graph.pop(shortest)  # Pop the shortest vertex from the graph so we don't iterate over it again in the algorithm

    vertex = end  # Make the vertex be equal the final vertex
    while vertex != start:  # Check if the start and end vertices aren't the same, if not insert the current working vertex into the first index of the array
        route.insert(0, vertex)
        vertex = previous_vertex[vertex]  # Set the vertex to be the last vertex visited

    route.insert(0, start)  # Else set the first index of the array to be the start vertex
    length_short_route = distance[end]
    return route  # Return the shortest route


# Graph as a dictionary so we can parse it in Python's CLI
graph = {"A": {"B": 4, "C": 3, "D": 2},
         "B": {"A": 4, "E": 4},
         "C": {"A": 3, "D": 1},
         "D": {"A": 2, "C": 1, "F": 2},
         "E": {"B": 4, "G": 2},
         "F": {"D": 2, "G": 5},
         "G": {"E": 2, "F": 5}}

print('Graph Dictionary:', graph)
start_point = input('Start Point: ')
end_point = input('End Point: ')

# Pass the graph dictionary as the @param graph into the algorithm function and calculate the shortest path from @param start_point to @param end_point
print('Shortest Route: ', dijkstrasAlgorithm(graph, start_point, end_point), 'of length {}'.format(length_short_route))

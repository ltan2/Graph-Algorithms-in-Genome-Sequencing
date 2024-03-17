
def eularian_path(graph):
    # we store the graph as in { 3: [2,4] , 1: [0]}
    in_nodes = [0] * (len(graph) + 1)
    out_nodes = [0] * (len(graph) + 1)

    for out_n,in_n in graph.items():
        out_nodes[out_n] += len(in_n)
        for in_node in in_n:
            in_nodes[in_node] += 1
    
    for i in range(0,len(in_nodes)):
        start_node, end_node = 0,0
        if (in_nodes[i] - out_nodes[i] > 1 or out_nodes[i] - in_nodes[i] > 1):
            return Null
        elif (in_nodes[i] - out_nodes[i] == 1):
            start_node = i
        elif (out_nodes[i] - in_nodes[i] == 1):
            end_node = i
    print(out_nodes)
    print(in_nodes)

    #now we have start and end node, we can traverse
    # we can use a stack to keep track, so lifo
    traversed_nodes = []
    traversed_nodes.append(start_node)
    curr_node = start_node
    while(traversed_nodes): # while stack is not empty
        # get next node
        if(out_nodes[curr_node] > 0):
            next_node = graph[curr_node][len(graph[curr_node])- out_nodes[curr_node]]
            out_nodes[curr_node] -= 1
            traversed_nodes.append(next_node)
            curr_node = next_node
        else:
            print(traversed_nodes.pop(), end=" ")
            if(len(traversed_nodes) > 0):
                curr_node = traversed_nodes[-1]
            
mapping_dict = {}
with open("graph.txt", "r") as file:
    for line in file:
        # Split the line by '->' to separate the key and values
        key, values = line.strip().split(' -> ')
        key = int(key)
        values = list(map(int, values.split(',')))
        mapping_dict[key] = values
eularian_path(mapping_dict)            

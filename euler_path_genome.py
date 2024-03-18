from debrujin import debrujin
from eularian_path import eularian_path

def euler_path_genome(filename):
    k, k_mers = 0, []
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                k = int(line.strip())
            else:
                k_mers.append(line.strip())
    
    graph = debrujin(k,k_mers)
    path = eularian_path(graph)
    genome = ""
    i = 0
    while(len(path) > 0):
        if i == 0:
            genome += str(path.pop())
        else:
            # smush overlap
            genome += str(path.pop())[-(k-2):]
        i += 1
    
    print(genome)

def smush_overlap(string_a, string_b):
    overlap = 0
    for i in range(1, min(len(string_a), len(string_b)) + 1):
        if string_a[-i:] == string_b[:i]:
            overlap = i
    return string_a + string_b[overlap:]


euler_path_genome("debrujin_input.txt")


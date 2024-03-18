
def debrujin(k, kmers):
    output = {}

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix in output:
            output[prefix].append(suffix)
        else:
            output[prefix] = [suffix] 
    return output

def read_file(filename):
    k, k_mers = 0, []
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                k = int(line.strip())
            else:
                k_mers.append(line.strip())
        return k, k_mers
    
k, kmers = read_file("debrujin_input.txt")
graph_output = debrujin(k,kmers)
print("graph:", graph_output)


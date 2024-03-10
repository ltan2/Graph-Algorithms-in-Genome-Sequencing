import find_kmer

def debrujin(k, genome):
    output = {}

    # kmers_arr = find_kmer.find_kmer(genome,k)
    kmers_arr = ["CA","CA","CA","CA", "CC","CA"]
    for kmers in kmers_arr:
        prefix = kmers[:-1]
        suffix = kmers[1:]
        if prefix in output:
            output[prefix].append(suffix)
        else:
            output[prefix] = [suffix] 
    return output

graph_output = debrujin(5,"TTTTTTTTTT")
print(graph_output)


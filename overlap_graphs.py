def overlap_graphs(kmers_arr):
    suffix_dict = []
    prefix_dict = []
    ret_cycle = {}

    for kmers in kmers_arr:
        prefix_dict.append(kmers[:-1])
        suffix_dict.append(kmers[1:])

    genome = kmers_arr[0]
    curr_i = 0
    curr_suffix = suffix_dict[0]
    for i in range(0,len(kmers_arr)):
        curr_res = []
        for j, pref in enumerate(prefix_dict):
            if curr_suffix == pref:
                if kmers_arr[j] not in curr_res:
                    curr_res.append(kmers_arr[j])
        if (curr_res != []):
            ret_cycle[genome] = curr_res
        if i+1 < len(kmers_arr):
            genome = kmers_arr[i+1]
            curr_suffix = suffix_dict[i+1]

    return ret_cycle

def read_file(file_path):
    contents = []
    with open(file_path, 'r') as file:
        for line in file:
            contents.append(line.strip())

    return contents

res = overlap_graphs(read_file("kmers_graph.txt"))
print(res)
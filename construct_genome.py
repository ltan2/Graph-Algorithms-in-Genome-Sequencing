def construct_genome(kmers_arr):
    suffix_dict = []
    prefix_dict = []

    for kmers in kmers_arr:
        prefix_dict.append(kmers[:-1])
        suffix_dict.append(kmers[1:])

    genome = kmers_arr[0]
    curr_i = 0
    curr_suffix = suffix_dict[0]
    for i in range(1,len(kmers_arr)):
        for j, pref in enumerate(prefix_dict):
            if curr_suffix == pref and j != curr_i:
                genome += kmers_arr[j][len(kmers_arr[j])-1]
                curr_i = j
                break
        curr_suffix = suffix_dict[curr_i] 
    return genome


def read_file(file_path):
    contents = []
    with open(file_path, 'r') as file:
        for line in file:
            contents.append(line.strip())

    return contents

res = construct_genome(read_file("kmers.txt"))
assert res == "ACCGAAGCT"
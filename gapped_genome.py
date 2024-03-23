def gapped_genome(genome_arr_1, genome_arr_2):
    genome_1 = genome_arr_1[0]
    genome_2 = genome_arr_2[0]
    max = 0

    for i in range(1,len(genome_arr_1)):
        genome_1 += genome_arr_1[i][-1]
    
    # check for first text only reverse
    j = 0
    for i in range(len(genome_2)-1, -1, -1):
        if genome_2[i] == genome_1[-(j+1)]:
            max += 1
        elif max > 0:
            break
        j += 1

    for i in range(1, len(genome_arr_2)):
        genome_2 += genome_arr_2[i][-1]
        if genome_2 == genome_1[-(max+1):]:
            max += 1
    # we get max len
    return genome_1 + genome_2[-(len(genome_2)- max):]

def process_file(file_name):
    p1 = []
    p2 = []
    with open(file_name, "r") as file:
        for line in file:
            p1_str, p2_str = line.strip().split('|')
            p1.append(p1_str)
            p2.append(p2_str)
    return p1, p2
p1 , p2 = process_file("gapped_genome.txt")
print(gapped_genome(p1, p2))
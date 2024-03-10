
def find_kmer(input_file, k):
    input_str = input_file
    kmers = []
    str_len = len(input_file)
    curr_index = 0

    for i in range(0,len(input_str)):
        curr_index = 1
        while curr_index < k and (len(kmers) - curr_index) >= 0:
            if(len(kmers[len(kmers) - curr_index]) + 1  > k):
                break
            kmers[len(kmers) - curr_index] += input_str[i]
            curr_index +=1
        if(len(input_str) - i >= k):
            kmers.append(input_str[i])
    return kmers

kmers = find_kmer("ACGTGTATA",3)
print(kmers)

import os

def split_paired_reads(read_fn, num_files):
    line_length = 100
    output_str = '>Throwawway' + '\n'
    for i in range(num_files):
        output_fn = './split_paired_reads/' + str(i) + '.txt'
        with(open(output_fn, 'w')) as output_file:
            output_file.write(output_str)

    curr_file = 0
    first_line = True
    output_fn = './split_paired_reads/' + str(curr_file) + '.txt'
    with open(read_fn, 'r') as input_file:
        for line in input_file:
            if first_line:
                first_line = False
                continue  # We skip the first line, since it
                # only contains the name of the chromosome the reads
                # came from.
            line = line.strip()
            #print(line)
            with(open(output_fn, 'a')) as output_file:
                output_file.write(line)
                output_file.write('\n')


            curr_file = (curr_file + 1) % num_files
            output_fn = './split_paired_reads/' + str(curr_file) + '.txt'





if __name__ == '__main__':
    filename = "./split_paired_reads/0.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    read_fn = 'hw2grad_M_1/hw2grad_M_1_chr_1.txt'
    split_paired_reads(read_fn, 8)


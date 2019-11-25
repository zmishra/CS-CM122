import os

def split_reads(read_fn, num_files):
    line_length = 100
    output_str = '\n\n' + '-' * (line_length + 6) + '\n'
    for i in range(num_files):
        output_fn = './split_reads/' + str(i) + '.txt'
        with(open(output_fn, 'w')) as output_file:
            output_file.write(output_str)

    curr_file = 0
    line_count = 0
    output_fn = './split_reads/' + str(curr_file) + '.txt'
    with open(read_fn, 'r') as input_file:
        for line in input_file:
            line_count += 1
            line = line.strip()
            if line_count <= 3:  # The first 3 lines need to be skipped
                continue

            with(open(output_fn, 'a')) as output_file:
                output_file.write(line)
                output_file.write('\n')

            if len(line) > 0 and all(x == '-' for x in line):
                curr_file = (curr_file + 1) % num_files
                output_fn = './split_reads/' + str(curr_file) + '.txt'





if __name__ == '__main__':
    filename = "./split_reads/0.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    read_fn = 'hw2b_hasher.txt'
    split_reads(read_fn, 12)


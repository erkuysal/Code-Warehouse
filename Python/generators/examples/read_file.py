def read_large_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line


# Using the generator to read a large file
file_path = 'large_file.txt'
for line in read_large_file(file_path):
    print(line, end='')

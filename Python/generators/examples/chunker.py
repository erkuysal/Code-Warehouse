def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


# Using the chunk data generator
data = list(range(1, 21))  # Example data
chunk_size = 5
chunk_gen = chunk_data(data, chunk_size)
for chunk in chunk_gen:
    print(chunk)
    
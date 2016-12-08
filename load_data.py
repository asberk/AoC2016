def load_data(fn):
    with open(fn, 'r') as fp:
        read_data = fp.read()
    # Format the input data into separate vectors
    data = read_data.split('\n')[:-1]
    return data

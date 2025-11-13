def logger(file_path:str,val):
    with open(file_path, 'w') as f:
        f.write(val)
def reader(file_path,val):
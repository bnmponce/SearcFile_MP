import os
path = "C:\\test_search\\"
file_name = "test.txt"
filepath = os.path.join(path, file_name)
if not os.path.exists(path):
    os.makedirs(path)
f = open(filepath, 'a')
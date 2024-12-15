import os

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace(".txt", ".py")))

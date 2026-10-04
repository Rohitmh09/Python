# Reading a CSV file - needs exact path
with open("../data/Paris_Weather.csv", "r") as file:
    content = file.read()
    print(content)
import csv

with open('users.txt') as f:
    list = []
    for line in f:
        inner_list = [elt.strip() for elt in line.split('/t')]
        list.append(inner_list)

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list)

with open('users.csv') as f:
    list = []
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]
        list.append(inner_list)

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list)
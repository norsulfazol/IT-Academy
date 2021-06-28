import csv

# with open("animals.csv", "w") as f:
#     f.writelines(["type,alias,age\n", "cat,Кузьмич,2\n", "dog,Зефирка,4\n"])

# with open("animals.csv", "r") as f:
#     flag = True
#     for l in f:
#         if flag:
#             flag = not flag
#             continue
#         x = l.split(',')
#         print(f"my animal is {x[0]} named {x[1]} and it {x[2]} years old")


# with open("animals_new.csv", "w", newline='') as f:
#     writer = csv.writer(f, delimiter=';')
#     writer.writerow(["type", "alias", "age"])
#     writer.writerow(["cat", "Tom", "70"])

# with open("animals_new.csv", "r", newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#         print(row)

with open("animals_new.csv", "r", newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    num = 1
    counter = 0
    for row in reader:
        if (counter == num):
            print(row)
            break
        counter += 1
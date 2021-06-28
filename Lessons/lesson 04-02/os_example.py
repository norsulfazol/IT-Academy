import os

print(f"current directory is {os.getcwd()}")
# os.chdir("C:\\Projects\\IT Academy\\Python\\M-PT1-37-21\\Repo\\Lessons\\lesson 03-29")

# print(f"current directory is {os.getcwd()}")
# with open("test_test_test.txt", "w") as f: pass

#d = f"test{os.path.sep}nest"
# d = os.path.join("test", "another test")
# print(d)
#print(os.path.sep)
#os.makedirs(d)

# l = os.listdir(os.getcwd())
# print(l)

#os.remove("test\\New Text Document.txt")

#os.removedirs("test\\nest")

os.rename("test.txt", "new.txt")
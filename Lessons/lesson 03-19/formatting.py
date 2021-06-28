c = "cat"
d = "dog"
p = "parrot"

print("a" + " " + c + "," + " " + "a" + " " + d + "," + " " + "a" + " " + p + ".")

print("a {}, a {}, a {}.".format(c, d, p))
print("a {}, a {}, a {}.".format(d, p, c))
print("a {1}, a {0}, a {2}.".format(c, d, p))
print("a {x}, a {y}, a {z}.".format(z=c, x=d, y=p))
print("a {x}, a {y}, a {0}.".format(c, x=d, y=p))

print(f"a {c}, a {d}, a {p}.")

x = 0
print(f"{x+5}")

#old-fashioned formatting:
print("%s %d" % ('test', 42))
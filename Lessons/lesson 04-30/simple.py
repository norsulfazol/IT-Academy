class Simpleton: pass

s = Simpleton()
Simpleton.name = "test"
print(s.name)
s.name = "new name for s"
print(s.name)
print(Simpleton.name)
Simpleton.name = "default name"
print(s.name)

s.test = "test"
print(s.test)
#print(Simpleton.test)
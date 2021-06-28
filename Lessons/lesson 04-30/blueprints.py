class Blueprint:

    name = "new blueprint"

    def __init__(self, level_count):
        self.level_count = level_count

class HouseProject(Blueprint):

    def __init__(self, level_count, entry_count):
        # super().__init__(level_count)
        Blueprint.__init__(self, level_count)
        self.entry_count = entry_count

class TownHouseProject(Blueprint):
    def __init__(self, entry_count):
        super().__init__(1)
        # Blueprint.__init__(self, 1)
        self.entry_count = entry_count


# hp = HouseProject(25, 4)
# print(hp.level_count, hp.entry_count)
# print(hp.name)
# hp.name = "new house project"
# print(hp.name)

th = TownHouseProject(10)
print(th.entry_count, th.level_count)
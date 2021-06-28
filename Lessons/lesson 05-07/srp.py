class Account:

    def __init__(self, id, first_name, last_name, repo_manager):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__repo_manager = repo_manager

    def get_info(self):
        return self.__first_name, self.__last_name

    def save(self, new_name):
        self.__first_name = new_name
        self.__repo_manager.update_account(self)

class AccountRepo:

    def update_account(self, account):
        pass

class DB_Manager(AccountRepo):

    def update_account(self, account):
        #update db here
        pass

class JSON_Manager(AccountRepo):

    def update_account(self, account):
        #update json here
        pass



db = DB_Manager()

acc = Account("nfjdhg", "ivan", "ivanoff", JSON_Manager())
acc.get_info()
acc.save("petroff")
class Discount:

    __base_discount = 0.95

    def __init__(self, customer):
        self.__customer = customer

    def calculate(self, price):
        return price*self.__base_discount

class VIPDiscount(Discount):

    def __init__(self, customer):
        super().__init__(customer)
        VIPDiscount.__base_discount = Discount.__base_discount - 0.1

    # def calculate(self, price):
    #     return price*self.__base_discount

class PremiumDiscount(Discount):

    def __init__(self, customer):
        super().__init__(customer)
        PremiumDiscount.__base_discount = Discount.__base_discount - 0.05

class Customer:

    def __init__(self, customer_type):
        self.__type = customer_type

    def get_type(self):
        return self.__type

class DiscountManager:

    def getDiscount(self, customer):
        if customer.get_type() == "vip":
            return VIPDiscount(customer)
        if customer.get_type() == "premium":
            return PremiumDiscount(customer)

        return Discount(customer)

a = Customer("vip")
b = Customer("common_vilager")
c = Customer("premium")

dm = DiscountManager()

ad = dm.getDiscount(a)
bd = dm.getDiscount(b)
cd = dm.getDiscount(c)
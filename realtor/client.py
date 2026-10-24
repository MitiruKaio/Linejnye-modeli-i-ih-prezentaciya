class Client:
    default_name = "Ivan"
    default_age = 18

    def __init__(self, name=default_name, age=default_age, bank=None):
        if bank is None:
            raise ValueError("Bank is required")
        self.name = name
        self.age = age
        self.__house = None
        self.__account = bank.add_account(self)

    def info(self):
        print(self)

    def __str__(self):
        return (
            f"Client: {self.name}, age: {self.age}, "
            f"house: {self.__house}, money: {self.__account.amount}"
        )

    @staticmethod
    def default_info():
        print(f"Default name: {Client.default_name}")
        print(f"Default age: {Client.default_age}")

    def __make_deal(self, house, price):
        self.__account -= price
        self.__house = house

    def earn_money(self, amount):
        self.__account += amount

    def buy_house(self, house, discount=0):
        price = house.final_price(discount)

        if self.__account.amount >= price:
            self.__make_deal(house, price)
            print("House bought successfully!")
        else:
            print("Not enough money to buy this house!")

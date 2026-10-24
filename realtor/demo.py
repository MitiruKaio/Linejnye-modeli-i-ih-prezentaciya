from client import Client
from house import SmallHouse
from bank import Bank

green_bank = Bank()
red_bank = Bank()

Client.default_info()

student = Client("Student", 20, green_bank)
teacher = Client("Teacher", 45, red_bank)

student.info()

print(teacher)

house = SmallHouse(100000)

student.buy_house(house)

student.earn_money(150000)

student.buy_house(house)

student.info()

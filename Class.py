class Car():
    def __init__(self, modelname, year, price):
        self.modelname = modelname
        self.year = year
        self.price = price
    def price_inc(self):
        self.price=int(self.price*1.15)

honda = Car('City',2017,1000000)
tata = Car('Bolt',2016,1000000)
honda.cc=1500
print(honda.__dict__)
honda.price_inc()
print(honda.price)

# #INHERITANCE
# class SuperCar(Car):
#     def __init__(self,modelname, year, price,cc):
#         super.__init__(modelname, year, price)
#         self.cc=cc
#
# # OD=SuperCar('abc',2018,7000000)
# print(help(honda))
# print(OD.__dict__)


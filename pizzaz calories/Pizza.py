from Toppings import topping
from Dough import dough

class pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
    def get_dough(self):
        return self.__dough
    def set_dough(self, dough):
        self.__dough = dough
    
    def get_toppings_capacity(self):
        return self.__toppings_capacity
    def set_toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping_object:topping):
        topping_name = topping_object.get_topping_type()
        topping_weight = topping_object.get_weight()

        if(self.__toppings_capacity < len(self.__toppings)):
            raise ValueError("Not enough space for another topping") # phát sinh 1 ngoại lệ/ notice: ValieError: string
        
        # Creating new topping
        self.__toppings[topping_name] = topping_weight

        # Check topping already dict
        if(self.__toppings.get(topping_name, True) != True):
            self.__toppings[topping_name] += topping_weight

    def caculate_total_weight(self):
        sum = self.get_dough().get_weight()
        for i in self.__toppings.values():
            sum += i
        return sum
# add ingredient
tp = topping("cheese", 5)
tp1 = topping("cheese1", 10)
tp2 = topping("cheese1", 15)
tp3 = topping("cheese", 15)

do1 = dough("A1", "donut", 1)
do2 = dough("A2", "doyaraky", 2)

pz = pizza("pizaa1", do2, 2)

pz.add_topping(tp)
pz.add_topping(tp1)
pz.add_topping(tp2)
pz.add_topping(tp3)

print(pz.caculate_total_weight())

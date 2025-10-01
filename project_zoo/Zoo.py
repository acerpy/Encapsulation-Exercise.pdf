from Caretaker import caretaker
from Cheetah import cheetah
from Keeper import keeper
from Lion import lion
from Tiger import tiger
from Vet import vet
class Zoo:
    def __init__(self, name, budget, animals_capacity, workers_capacity):
        #Private
        self.name = name
        self.__budget = budget 
        self.__animals_capacity = animals_capacity
        self.__worker_capacity = workers_capacity
        self.list_animals = []
        self.list_workers = []


    def add_animal(self, animal, price):
        if (self.__budget >= 45 and self.__animals_capacity > 0):
            #get animal type: lion/ tiger/ cheetah
            type_animal = type(animal).__name__ # using access name of  another class 
            #add list animals
            self.list_animals.append(animal)

            self.__budget -= price
            self.__animals_capacity -= 1
            return f"{animal.name}  the  {type_animal}  added  to  the  zoo"

        elif(self.__budget < 45):
            return "Not  enough  budget"
        else:
            return "Not  enough  space  for  animal"
        
    def hire_worker(self, worker):
        if(self.__worker_capacity > 0):
            # get worker type: keeper/ caretake/ vet and add list workers
            type_worker = type(worker).__name__
            self.list_workers.append(worker)

            # Reduce capaticy
            self.__worker_capacity -= 1
            return f"{worker.name}  the  {type_worker}  hired  successfully"
        else:
            return "Not  enough  space  for  workers"
    
    def fire_worker(self, worker_name):
        for i in range(len(self.list_workers)):
            if(self.list_workers[i].name == worker_name):
                self.list_workers.remove(self.list_workers[i])
                return f"{worker_name}  fired  successfully"
        return f"There  is  no  {worker_name}  in  the  zoo"
            
    
    def pay_workers(self):
        sum_workers = 0
        for i in range(len(self.list_workers)):
            sum_workers += self.list_workers[i].salary # access salary of another file
        if(self.__budget >= sum_workers):
            self.__budget -= sum_workers
            return f"You  paid  your  workers.  They  are  happy. Budget  left:  {self.__budget}"
        else:
            return "You  have  no  budget  to  pay  your  workers.  They  are  unhappy"
        
    def tend_animals(self):
        sum_animals = 0
        for i in range(len(self.list_animals)):
            sum_animals += self.list_animals[i].get_needs() # access instance method of another file
        if(self.__budget >= sum_animals):
            self.__budget -= sum_animals
            return f"You  tend  all  the  animals.  They  are  happy. Budget  left:  {self.__budget}"
        else:
            return "You  have  no  budget  to  tend  the  animals.  They  are  unhappy."
    
    def profit(self, amount):
        self.__budget += amount
    
    def animals_status(self):
        lion1 = [a for a in self.list_animals if type(a).__name__ == "lion"] #
        tiger1 = [a for a in self.list_animals if type(a).__name__ == "tiger"]
        cheetah1 = [a for a in self.list_animals if type(a).__name__ == "cheetah"]
        
        amount_of_lions = len(lion1)
        amount_of_tigers = len(tiger1)
        amount_of_cheetahs = len(cheetah1)
        
        lion1 = "\n".join( str(a) for a in lion1)
        tiger1 = "\n".join([str(a) for a in tiger1])
        cheetah1 = "\n".join([ str(a) for a in cheetah1])
        
        return f"""You have {len(self.list_animals)} animals 
----- {amount_of_lions} Lions: 
{lion1} 
----- {amount_of_tigers} Tigers: 
{tiger1} 
----- {amount_of_cheetahs} Cheetahs: 
{cheetah1} """

    def worker_status(self):
        keeper1 = [ b for b in self.list_workers if b.__class__.__name__ == "keeper"]
        caretaker1 = [ b for b in self.list_workers if b.__class__.__name__ == "caretaker"]
        vet1 = [ b for b in self.list_workers if b.__class__.__name__ == "vet"]

        amount_of_keepers = len(keeper1)
        amount_of_caretakers = len(caretaker1)
        amount_of_vetes = len(vet1)

        keeper1 = "\n".join([ str(b) for b in keeper1])
        caretaker1 = "\n".join([ str(b) for b in caretaker1])
        vet1 = "\n".join([ str(b) for b in vet1])
        
        return f"""You have {len(self.list_workers)} workers 
----- {amount_of_keepers} Keepers: 
{keeper1} 
----- {amount_of_caretakers} Caretakers: 
{caretaker1} 
----- {amount_of_vetes} Vets: 
{vet1} """
    

zoo = Zoo("Zootopia", 3000, 5, 8) 

# Animals creation 
animals = [
    cheetah("Cheeto", "Male", 2), cheetah("Cheetia", "Female", 1), 
    lion("Simba", "Male", 4), 
    tiger("Zuba", "Male", 3), tiger("Tigeria", "Female", 1), 
    lion("Nala", "Female", 4)
]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [
    keeper("John", 26, 100), keeper("Adam", 29, 80), keeper("Anna", 31, 95), 
    caretaker("Bill", 21, 68), caretaker("Marie", 32, 105), caretaker("Stacy", 35, 140), 
    vet("Peter", 40, 300), vet("Kasey", 37, 280), vet("Sam", 29, 220)
]

# adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# adding all workers
for i in range(len(workers)):
    worker = workers[i]
    print(zoo.hire_worker(worker))

# Tending animals

print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())



print(zoo.animals_status())
print(zoo.worker_status())

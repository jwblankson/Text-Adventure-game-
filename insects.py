[insects.py](https://github.com/user-attachments/files/23078963/insects.py)
# Classes of Dragonfly
class Dragonfly:
        def __init__(self):
            self.legs = 6
            self.pair_of_wings = 2
            self.species = "Dragonfly"

        def display(self):
            print(f"insec species : {self.species}, it has {self.legs} and {self.pair_of_wings} pair of wings")


#classes of spider

class Spider:
        def __init__(self):
            self.legs = 8
            self.pair_of_wings = 0
            self.species = "Spider"

        def display(self):
                print(f"Insect species : {self.species},it has {self.legs} and {self.pair_of_wings} pair of wings")


 # Classes of cicada

class Cicada:
        def __init__(self):
            self.legs = 6
            self.pair_of_wings = 1
            self.species = "Cicada"


        def display(self):
                print(f'Insect species: {self.species}, it has {self.legs} legs and {self.pair_of_wings} pair of wings')

dragonfly = Dragonfly()
spider = Spider()
cicada = Cicada()

dragonfly.display()
spider.display()
cicada.display()

# classes of insects
class Insect:
        def __init__(self,a,b,c):
            self.legs = a
            self.pair_of_wings = b
            self.species = c

        def display(self):
            print(f'Insect species:{self.species}, it has {self.legs} {self.pair_of_wings} pair of wings')

    
total_num = int(input("Enter total number of insects"))
total_legs = int(input("Enter total number of legs"))
total_pair_of_wings = int(input("Enter total pair of wings"))

def calculate_spider_and_others(dragonfly,spider):
    num_of_other_than_spider = (total_num * spider.legs - total_legs) / (spider.legs - dragonfly.legs)
    return total_num - num_of_other_than_spider, num_of_other_than_spider 
def calculate_dragonfly_and_cicada(other_nunm,  dragonfly, cicada):
        cicada_num = (other_num * dragonfly.pair_of_wings - total_pair_of_wings)/ (dragonfly.pair_of_wings - cicada.pair_of_wings)
        return other_num - cicada_num, cicada_num

dragonfly = Insect(6, 2, "Dragonfly")
spider = Insect(6, 1, "Spider")
cicada = Insect(8, 0, "Cicada")

total_insects = 25
total_legs = 162
total_wings = 31

dragonfly_count = 12
spider_count = dragonfly_count - 6
cicada_count = total_wings - 2 * dragonfly_count

dragonfly.display()
spider.display()
cicada.display()

print("Solution")
print(f"Number of dragonflies: {dragonfly_count}")
print(f"Number of spiders: {spider_count}")
print(f"Number of cicadas: {cicada_count}")




print(f'{dragonfly_num} Dragonflies, {cicada_num} cicadas, and {spider_num} spiders')

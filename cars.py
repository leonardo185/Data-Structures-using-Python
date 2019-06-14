#DSA-Assgn-2

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service:
    def __init__(self, car_list):
        self.__car_list = car_list

    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self,year):
        new_list = []
        for i in range(len(self.__car_list)):
            if(self.__car_list[i].get_year() == year):
                new_list.append(self.__car_list[i].get_model())

        return new_list


    def add_cars(self,car_new_list):
        self.__car_list = self.__car_list + car_new_list
        for i in range(len(self.__car_list)):
            min = i
            for j in range(i+1, len(self.__car_list)):
                if(self.__car_list[min].get_year() > self.__car_list[j].get_year()):
                    min = j

            if(min != i):
                self.__car_list[i],self.__car_list[min] = self.__car_list[min],self.__car_list[i]

        new_list1 = []
        for i in range(len(self.__car_list)):
            new_list1.append(self.__car_list[i].get_year())

        return new_list1

    def remove_cars_from_karnataka(self):
        print(type(self.__car_list))
        new_list = []

        for i in range(len(self.__car_list)):
            car_reg = self.__car_list[i].get_registration_number()
            if(not car_reg.startswith("KA")):
                new_list.append(self.__car_list[i])

        self.__car_list = new_list
        return self.__car_list

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#Create object of Service class, invoke the methods and test your program
cars = Service(car_list)
print(*cars.find_cars_by_year(2014))

car5=Car("Alto",2015,"KL07 4332")
car_list = [car5]
print(*cars.add_cars(car_list))
print(*cars.remove_cars_from_karnataka(), sep = "\n")

import math
class Figure:
    sides_count = 0
    filled = False
    def __init__(self,__color=(0,0,0), *__sides):

        self.__color = __color
        self.__sides =list(self.checking_sides(__sides))
    def checking_sides(self,sides):
        if self.__is_valid_sides(sides):
            return sides
        return [1] * self.sides_count


    def get_color(self):
        return self.__color
    def __is_valid_color(self,r,g,b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))
    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=[r,g,b]
        self.filled=True
    def  __is_valid_sides(self,new_sides):
        if self.sides_count != len(new_sides):
            return False
        for item in new_sides:
            if not isinstance(item, int):
                return False
        return True

    def get_sides(self):
        return list(self.__sides)
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self. __is_valid_sides(new_sides):
         self.__sides = new_sides
class Circle(Figure):
    sides_count = 1
    def __init__(self,__color=(0,0,0),*sides):
        if len(sides) == 1:
            self.set_sides(sides)
        super().__init__(__color,*sides)

    def __radius(self):
        return  self.get_sides() /(2 * math.pi)
    def get_square(self):
        return  self.__radius() ** 2 * math.pi

class Triangle (Figure):
    sides_count = 3
    def __init__ (self,__color=(0,0,0),*sides):

        super().__init__(__color,*sides)
        self.__color = __color



    def get_square(self):
        pp=sum(self.get_sides())/2
        return math.sqrt(pp*(pp-self.get_sides()[0])*(pp-self.get_sides()[1])*(pp-self.get_sides()[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self,__color=(0,0,0),*sides ):
        if len(sides) == 1:
            sides *= self.sides_count
        super().__init__(__color, *sides )
        self.__color=__color



    def get_volume(self):
         return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) 
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())
triangle1 = Triangle((200, 200, 100), 10, 6, 8)
triangle1.set_sides(5, 3, 12, 4, 5)

print(triangle1.get_sides())
print(triangle1.get_square())
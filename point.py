# Класс - точка в двумерном пространстве
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


point1 = Point(2, 7)
point2 = Point(-1, -1)
print("Расстояние между точками:", round(point1.distance_to(point2), 2))
print("Координаты точки 1:", point1.get_coordinates())
point1.set_coordinates(5, 5)
print("Новые координаты точки 1:", point1.get_coordinates())

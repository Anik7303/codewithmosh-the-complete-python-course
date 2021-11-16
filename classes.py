# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# # print(type(point))
# # print(
# #    f"point object is an instance of Point Class: {isinstance(point, Point)}")
# point.draw()
# another = Point(10, 10)
# point.draw()
# # print(point)
# print(point == another)
# print(point > another)
# print(point < another)
# print(point + another)
# print(another - point)

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        name = tag.lower()
        self.__tags[name] = self.__tags.get(name, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add('python')
cloud.add('Python')
cloud.add('python')
cloud.add('javascript')
cloud['python'] = 6
print(cloud['python'])
print(len(cloud))
for tag in cloud:
    print(f"{tag}: {cloud[tag]}")
print(cloud.__dict__)

# Classes is a bluepritnt for creating objects
# Objects are instances of classes


# Class:Human
# Objects:John, Mary, Bob

class Point:

    # default_color = "red"  # class level attrribute

    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}),({self.y})")


# point = Point()
# # False, because point is a class, not an instance
# print(isinstance(point, Point))
point = Point.zero()
point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.draw()
# | Item               | Name      | Type                    |
# | ------------------ | --------- | ----------------------- |
# | `Point`            | Class     | Class                   |
# | `__init__`         | Method    | Constructor             |
# | `draw`             | Method    | Instance method         |
# | `self.x`, `self.y` | Variables | Instance variables      |
# | `count` (if added) | Variable  | Class variable (shared) |

# Just Practicing


class Tagcloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = Tagcloud()
cloud["python"] = 10
len(cloud)
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

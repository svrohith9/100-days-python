###############################
# ....define the Rectangle class here
class Rectangle:

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def getPerimeter(self):
        return 2*(self.height+self.width)

    def getArea(self):
        return self.height*self.width

    def showRectangle(self):
        result = "\n"
        for i in range(self.height):
            for j in range(self.width):
                result += "*"
            result += "\n"
        return result


###############################


def main():
    print("Rectangle Calculator")
    print()

    while True:
        try:
            h = int(input("Height:    "))
            w = int(input("Width:     "))

            if h < 2 or w < 2:
                raise Warning(
                    "Both height and width must be 2 or larger! Try again...")

            rect = Rectangle(h, w)
            print("Perimeter:", rect.getPerimeter())
            print("Area:     ", rect.getArea())
            print(rect.showRectangle())
        except Warning as ex:
            print(ex)
            continue

        again = input("Continue? (y/n): ").lower()
        print()
        if again != "y":
            break

    print("Bye!")


if __name__ == "__main__":
    main()

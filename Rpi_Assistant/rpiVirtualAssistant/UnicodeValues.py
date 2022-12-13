import geocoder


class Point:
    def __init__(self, *args):
        self.__data = args

    def dimension(self):
        return len(self.__data)

    def __str__(self):
        s = [str(x) for x in self.__data]
        return "(" + ",".join(s) + ")"


class ColoredPoint(Point):
    def __init__(self, color, *args):
        super().__init__(*args)
        self.color = color


if __name__ == "__main__":
    x = ColoredPoint("red", 0, 0)
    assert x.dimension() == 2
    assert x.color == "red"


class Letters:
    def __init__(self, *args):
        self.__data = args
        Language = "DevaNagiri"

class DevanagiriLetters(Letters):


   def PrintAllLetters:

       pa = '\u092a'
       pha ='\u092b'
       ba = '\u092c'
       bha = '\u092d'
       ma = '\u092e'
       DevanagiriLetters = [pa,pha,ba,bha,ma]

       for i in DevanagiriLetters:
           print(i)






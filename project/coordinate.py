class Coordinate:
    def __init__(self, x, y, label):
        self.__x = x
        self.__y = y
        self.__label = label

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_label(self):
        return self.__label

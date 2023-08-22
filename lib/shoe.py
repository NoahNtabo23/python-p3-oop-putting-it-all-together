#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand="",size=0):
        self.brand=brand

        if not isinstance(size,int):
            print("size must be an integer")
        else:
            self.size = size

    def cobble(self):
        print("This shoe has been repaired.")
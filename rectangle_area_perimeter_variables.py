#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program calculates the area and the perimeter of the rectangle.


def main():
    # calculates the area and the perimeter

    # input
    width = int(input("Enter the width of the rectangle (mm): "))
    length = int(input("Enter the length of the rectangle (mm): "))

    # process
    area = width * length
    perimeter = 2 * (width+length)

    # output
    print("")
    print("Area is {} mm^2".format(area))
    print("Perimeter is {} mm".format(perimeter))


if __name__ == "__main__":
    main()

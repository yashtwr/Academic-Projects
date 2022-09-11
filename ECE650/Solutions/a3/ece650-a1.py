#!/usr/bin/env python3
import sys
import re
import math


# YOUR CODE GOES HERE
class line(object):
    """A line between two points"""

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.points = []
        self.flag = False
        self.points.append(src)
        self.points.append(dst)

    def __repr__(self):
        return '[' + str(self.src) + '-->' + str(self.dst) + ']'

    def add_point(self, point):
        d1 = math.dist(self.points[0], point)
        inserted = False
        if point not in self.points:
            if (len(self.points) == 2):
                self.points.insert(1, point)
            else:
                for i in range(1, len(self.points)):
                    d = math.dist(self.points[0], self.points[i])
                    if (d > d1):
                        self.points.insert(i, point)
                        break

def intersect(l1, l2):
    """Returns a point at which two lines intersect"""
    x1, y1 = l1.src[0], l1.src[1]
    x2, y2 = l1.dst[0], l1.dst[1]

    x3, y3 = l2.src[0], l2.src[1]
    x4, y4 = l2.dst[0], l2.dst[1]
    a, b, c, d = y2 - y1, x2 - x1, y4 - y3, x4 - x3
    xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
    xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if (xden == 0 or yden == 0):
        return None
    xcoor = xnum / xden
    ycoor = ynum / yden
    if max(x1, x2) >= xcoor >= min(x1, x2) and \
            max(x3, x4) >= xcoor >= min(x3, x4) and \
            max(y1, y2) >= ycoor >= min(y1, y2) and \
            max(y3, y4) >= ycoor >= min(y3, y4):
        return (xcoor, ycoor)
    else:
        return None


def gg(street_names, lines):
    vertices = []
    edges = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            for l1 in lines[i]:
                for l2 in lines[j]:
                    p = intersect(l1, l2)
                    if (p != None):
                        l1.flag = True
                        l2.flag = True
                        l1.add_point(p)
                        l2.add_point(p)
    for street in lines:
        for line in street:
            if (line.flag):
                for coord in line.points:
                    if coord in vertices:
                        continue
                    else:
                        vertices.append(coord)
    for street in lines:
        for line in street:
            if (line.flag):
                for k in range(len(line.points)-1):
                    z = {vertices.index(line.points[k]),vertices.index(line.points[k+1])}
                    edges.append(z)
    print("V",len(vertices))
    print("E {",end="")
    for e in range(len(edges)):
        k = list(edges[e])
        if(e == len(edges) - 1):
            print('<'+str(k[0]+1)+','+str(k[1]+1)+'>',end="")
        else:
            print('<'+str(k[0]+1)+','+str(k[1]+1)+'>,',end="")
    print('}')
def modify_lines(lines):
    for street in lines:
        for line in street:
            src = line.points[0]
            dst = line.points[-1]
            line.points = []
            line.points.append(src)
            line.points.append(dst)
            line.flag = False



def add(name, coord, street_names, lines):
    temp = []
    if name in street_names:
        print("Error: Street name already exists",file = sys.stderr)
    else:
        street_names.append(name)
        for i in range(len(coord) - 1):
            temp.append(line(coord[i], coord[i + 1]))
        lines.append(temp)
        #print("Street name added successfully")


def modify(name, coord, street_names, lines):
    temp = []
    if name in street_names:
        i = street_names.index(name)
        for j in range(len(coord) - 1):
            temp.append(line(coord[j], coord[j + 1]))
        lines[i] = temp
        modify_lines(lines)
        #print("Street Coordinates modified successfully")
    else:
        print("Error: Street name does not exist, please add the street first to modify it",file = sys.stderr)


def main():
    # YOUR MAIN CODE GOES HERE
    street_names = list()
    lines = list()
    name_rx = "\"[a-zA-Z\s]*[a-zA-Z]\""
    num_rx = '-?\d+'
    coord_rx = '\(' + num_rx + ',' + num_rx + '\)'
    input_rx = re.compile('\s' + name_rx + '\s(' + coord_rx + '\s+){1,}' + coord_rx+'$')
    while True:
        #print("enter your input:")
        input_line = sys.stdin.readline()
        if input_line == "":
            break
        if (input_line[0:3] == "add" or input_line[0:3] == "mod"):
            if (input_rx.match(input_line[3:])):
                temp = re.findall(name_rx, input_line)
                if(temp[0][1] == " "):
                    print("Error: There should be no spaces before name",file = sys.stderr)
                else:
                    name = temp[0][1:-1].lower()
                    coord = [tuple([float(num) for num in re.findall(num_rx, coord)]) \
                        for coord in re.findall(coord_rx, input_line)]
                    if (input_line[0:3] == "add"):
                        add(name, coord, street_names, lines)
                    else:
                        modify(name, coord, street_names, lines)

            elif (not (re.compile('\s' + name_rx)).match(input_line[3:])):
                if (re.compile(name_rx).match(input_line[3:])):
                    print("Error: Please enter space between command and street name",file = sys.stderr)
                else:
                    print("Error: Invalid Street name",file = sys.stderr)
            else:
                print("Error: Please enter correct co ordinates, it should be atleast two",file = sys.stderr)



        elif (input_line[0:2] == "rm"):
            if ((re.compile('\s' + name_rx+'$')).match(input_line[2:])):
                name = re.findall(name_rx, input_line)
                if name[0][1:-1].lower() in street_names:
                    i = street_names.index(name[0][1:-1].lower())
                    street_names.pop(i)
                    lines.pop(i)
                    modify_lines(lines)
                    #print("Street name removed successfully")
                else:
                    print("Error: Street name does not exist ",file = sys.stderr)
            elif (not re.compile(name_rx).match(input_line[3:])):
                print("Error: Please enter space between command and street name",file = sys.stderr)
            else:
                print("Error: Ivalid command, please try again",file = sys.stderr)
        elif (input_line[0:2] == "gg"):
            if re.compile('gg$').match(input_line):
                gg(street_names, lines)
            else:
                print("Error: Invalid gg command",file = sys.stderr)
        else:
            print("Error: Please enter the correct command, ensure it is in lower ",file = sys.stderr)
    sys.exit(0)

if __name__ == "__main__":
    main()

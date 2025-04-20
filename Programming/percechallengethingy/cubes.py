def cubeintersectionvolume(cube1, cube2):
    minx1, miny1, minz1, side1 = cube1
    minx2, miny2, minz2, side2 = cube2

    maxx1 = minx1 + side1
    maxy1 = miny1 + side1
    maxz1 = minz1 + side1

    maxx2 = minx2 + side2
    maxy2 = miny2 + side2
    maxz2 = minz2 + side2

    intersectminx = max(minx1, minx2)
    intersectminy = max(miny1, miny2)
    intersectminz = max(minz1, minz2)

    intersectmaxx = min(maxx1, maxx2)
    intersectmaxy = min(maxy1, maxy2)
    intersectmaxz = min(maxz1, maxz2)

    width = max(0, intersectmaxx - intersectminx)
    depth = max(0, intersectmaxy - intersectminy)
    height = max(0, intersectmaxz - intersectminz)

    return width * depth * height

cube1 = [int(input()) for _ in range(4)]
cube2 = [int(input()) for _ in range(4)]

print(cubeintersectionvolume(cube1, cube2))
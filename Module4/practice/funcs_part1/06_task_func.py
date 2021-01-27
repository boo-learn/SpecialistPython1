def distance(x1, y1, x2, y2):
    res = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return res

def point_in_circle(x, y, xc, yc, r):
    point_dist = distance(x, y, xc, xy)
    if point_dist < r:
        return

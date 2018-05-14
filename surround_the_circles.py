# [2017-09-04] Challenge #330 [Easy] Surround the circles
# https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/
INPUT_DATA = [
    (1, 1, 2),
    (2, 2, 0.5),
    (-1, -3, 2),
    (5, 2, 1)
]


class Circle:
    def __init__(self, xcoord, ycoord, radious):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.radious = radious

    def find_corners(self):
        return [
            (self.xcoord - self.radious, self.ycoord + self.radious),
            (self.xcoord - self.radious, self.ycoord - self.radious),
            (self.xcoord + self.radious, self.ycoord - self.radious),
            (self.xcoord + self.radious, self.ycoord + self.radious),
        ]


class Area:
    def __init__(self, points: list):
        self.points = points

    def _get_most_forward_points(self):
        left = sorted(self.points, key=lambda x: x[0])[0][0]
        right = sorted(self.points, key=lambda x: -x[0])[0][0]
        top = sorted(self.points, key=lambda x: x[1])[0][1]
        bottom = sorted(self.points, key=lambda x: -x[1])[0][1]
        return left, right, top, bottom

    def get_coordinates(self):
        left, right, top, bottom = self._get_most_forward_points()
        return (left, top), (left, bottom), (right, top), (right, bottom)


def solution1(data):
    data = [Circle(*c).find_corners() for c in data]
    circles_corners = []
    for e in data:
        circles_corners.extend(e)
    area = Area(circles_corners)
    return area.get_coordinates()


if __name__ == '__main__':
    print(solution1(INPUT_DATA))
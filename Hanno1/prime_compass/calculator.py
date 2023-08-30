#!/usr/bin/python

from math import sqrt


class Calculator:
    xOffset = []
    yOffset = []
    xMid = 0  # Zero instead of None to subtract from X point
    yMid = 0  # Zero instead of None to subtract from Y point
    radius = 0  # Collected but not used data

    def find_offset(self, offsetList):
        if len(self.duplicate_check(offsetList)) == 3:
            try:
                self.xMid, self.yMid = self.findCircle(offsetList)
                self.xOffset.append(self.xMid)
                self.yOffset.append(self.yMid)
            except ZeroDivisionError:
                pass
            finally:
                return self.xMid, self.yMid

    @staticmethod
    def duplicate_check(lst):
        """Check for duplicates and return unique"""
        seen = set()
        uniq = []
        for item in lst:
            if item not in seen:
                uniq.append(item)
                seen.add(item)
        return uniq

    @staticmethod
    def findCircle(lst):
        """Function finds center point and radius
            of a circle given three points"""
        x1, y1 = lst[0]
        x2, y2 = lst[1]
        x3, y3 = lst[2]

        x12 = x1 - x2
        x13 = x1 - x3
        y12 = y1 - y2
        y13 = y1 - y3
        y31 = y3 - y1
        y21 = y2 - y1
        x31 = x3 - x1
        x21 = x2 - x1

        # x1^2 - x3^2
        sx13 = pow(x1, 2) - pow(x3, 2)
        # y1^2 - y3^2
        sy13 = pow(y1, 2) - pow(y3, 2)
        sx21 = pow(x2, 2) - pow(x1, 2)
        sy21 = pow(y2, 2) - pow(y1, 2)

        f = (((sx13) * (x12) + (sy13) *
              (x12) + (sx21) * (x13) +
              (sy21) * (x13)) // (2 *
                                  ((y31) * (x12) - (y21) * (x13))))

        g = (((sx13) * (y12) + (sy13) * (y12) +
              (sx21) * (y13) + (sy21) * (y13)) //
             (2 * ((x31) * (y12) - (x21) * (y13))))

        c = (-pow(x1, 2) - pow(y1, 2) -
             2 * g * x1 - 2 * f * y1)

        # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
        # where centre is (h = -g, k = -f) and
        # radius r as r^2 = h^2 + k^2 - c
        h = -g
        k = -f
        sqr_of_r = h * h + k * k - c

        # r is the radius
        r = sqrt(sqr_of_r)
        return (h, k), r

    @staticmethod
    def avg(lst):
        """Return average of list"""
        try:
            return sum(lst) / len(lst)
        except ZeroDivisionError:
            return 0

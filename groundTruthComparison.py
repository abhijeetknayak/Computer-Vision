import numpy as np


def WGStoCartesian(ptWGS84PointIn):
    ptRefWGS84Point = [48.694359, 9.011282, 0.0]
    ptRefCartPoint = [0.0, 0.0, 0.0]
    ptPointOut = []

    MP_HMHQ_RSM_WGS84_ECC_FLT = 0.0818191908426
    MP_HMHQ_RSM_WGS84_EARTH_RADIUS = 6378137.0

    fLatMid = np.deg2rad(0.5 * (ptWGS84PointIn[0] + ptRefWGS84Point[0]))
    fTemp = np.sqrt(1.0 - np.power((MP_HMHQ_RSM_WGS84_ECC_FLT * np.sin(fLatMid)), 2))
    fREast = MP_HMHQ_RSM_WGS84_EARTH_RADIUS / fTemp

    fRNorth = (MP_HMHQ_RSM_WGS84_EARTH_RADIUS * (1.0 - np.power(MP_HMHQ_RSM_WGS84_ECC_FLT, 2))) / np.power(fTemp, 3)

    ptPointOut.append(fREast * np.cos(fLatMid) * np.deg2rad((ptWGS84PointIn[1] - ptRefWGS84Point[1])) \
                      + ptRefCartPoint[0])

    ptPointOut.append(fRNorth * np.deg2rad((ptWGS84PointIn[0] - ptRefWGS84Point[0])) + ptRefCartPoint[1])

    ptPointOut.append((ptWGS84PointIn[2] / 100.0) - (ptRefWGS84Point[2] / 100.0) + ptRefCartPoint[2])

    return ptPointOut

def findSlope(pt1, pt2):
        return ((pt1[1] - pt2[1]) / (pt1[0] - pt2[0]))


if __name__ == '__main__':
    ptWGS84PointIn = [48.694349, 9.011232, 0.0]  # [48.694359, 9.011282, 0.0]
    pt1 = WGStoCartesian(ptWGS84PointIn)
    ptWGS84PointIn = [48.694340, 9.011186, 0.0]
    pt2 = WGStoCartesian(ptWGS84PointIn)

    leftDist = 1.72
    rightDist = 1.98

    slope = findSlope(pt1, pt2)
    theta = np.rad2deg(np.arctan(slope))
    print(slope, theta)

    ## Moving to the left
    if pt1[0] < pt2[0]:
        if abs(pt1[0] - pt2[0]) > 0.0:
            slope = findSlope(pt1, pt2)
            theta = np.arctan(slope)
            print(slope, theta)
            c1 = pt1[1] - slope * pt1[0]
        else:
            c1 = pt1[1]
            theta = 0.0

        newYLeft = c1 - (leftDist * np.cos(theta))
        newYRight = c1 + (rightDist * np.cos(theta))
        newXLeft =

    ##  Moving to the right
    elif pt1[0] > pt2[0]:
        pass

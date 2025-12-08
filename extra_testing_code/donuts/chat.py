import math
import time
import os
import sys

def donut():
    A = 0.0
    B = 0.0
    # Screen size (columns × rows)
    width = 80
    height = 24

    # Precompute some constants
    R1 = 1     # inner radius of tube
    R2 = 2     # distance from center of tube to center of torus
    K2 = 5     # distance from viewer to torus center (or “depth” constant)
    K1 = width * K2 * 3 / (8 * (R1 + R2))  # scaling factor for projection

    while True:
        # Buffers for this frame
        output = [' '] * (width * height)
        zbuffer = [0] * (width * height)

        cosA = math.cos(A)
        sinA = math.sin(A)
        cosB = math.cos(B)
        sinB = math.sin(B)

        theta = 0.0
        while theta < 2 * math.pi:
            costheta = math.cos(theta)
            sintheta = math.sin(theta)
            phi = 0.0
            while phi < 2 * math.pi:
                cosphi = math.cos(phi)
                sinphi = math.sin(phi)

                # 3D (x, y, z) coordinate before rotation
                circlex = R2 + R1 * costheta
                circley = R1 * sintheta

                # 3D coordinates after rotations A and B
                x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
                y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
                z = K2 + cosA * circlex * sinphi + circley * sinA
                ooz = 1 / z  # "one over z" — used for depth

                # 2D projection
                xp = int(width / 2 + K1 * ooz * x)
                yp = int(height / 2 - K1 * ooz * y)

                # calculate luminance (simple shading)
                L = (cosphi * costheta * sinB
                     - cosA * costheta * sinphi * sinB
                     - sinA * sintheta * sinB)

                # only plot if inbounds and nearer than what we have
                idx = xp + yp * width
                if 0 <= xp < width and 0 <= yp < height and ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    # map luminance to ASCII chars
                    lum_index = int((L + 1) * 5.5)  # adjust to 0..11 roughly
                    chars = ".,-~:;=!*#$@"
                    output[idx] = chars[max(0, min(lum_index, len(chars)-1))]

                phi += 0.07
            theta += 0.02

        # print frame
        sys.stdout.write("\x1b[H")  # move cursor to top-left
        for i in range(height):
            line = ''.join(output[i*width:(i+1)*width])
            sys.stdout.write(line + "\n")

        # update rotation angles
        A += 0.04
        B += 0.02

        # pause a bit
        time.sleep(0.03)

if __name__ == "__main__":
    # clear screen once
    os.system('cls' if os.name == 'nt' else 'clear')
    donut()
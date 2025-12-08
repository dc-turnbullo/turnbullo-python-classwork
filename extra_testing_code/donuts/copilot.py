#!/usr/bin/env python3
"""
ASCII rotating donut (simple Python implementation).
Run with `python rotating_donut.py` for continuous animation,
or `python rotating_donut.py --frames 100` to run a fixed number of frames.
"""
import math
import time
import os
import sys
import argparse

CHARS = " .,-~:;=!*#$@"

def clear_screen():
    # Prefer ANSI cursor home + clear; fall back to cls on Windows if needed
    if os.name == 'nt':
        os.system('cls')
    else:
        sys.stdout.write('\x1b[2J\x1b[H')


def render_frame(A, B, width=80, height=24, R=2.0, r=1.0, k1=15.0):
    """Render a single frame of a torus rotated by angles A and B.
    Returns the string to print to the terminal.
    """
    # z-buffer and output buffer
    size = width * height
    zbuf = [float('-inf')] * size
    out = [' '] * size

    cosA = math.cos(A); sinA = math.sin(A)
    cosB = math.cos(B); sinB = math.sin(B)

    # sampling density (tradeoff quality / speed)
    theta_steps = 90
    phi_steps = 90

    for ti in range(theta_steps):
        theta = 2.0 * math.pi * ti / theta_steps
        cost = math.cos(theta); sint = math.sin(theta)
        for pi in range(phi_steps):
            phi = 2.0 * math.pi * pi / phi_steps
            cosf = math.cos(phi); sinf = math.sin(phi)

            # 3D coordinates of point on torus (before rotation)
            x = (R + r * cost) * cosf
            y = (R + r * cost) * sinf
            z = r * sint

            # surface normal (before rotation)
            nx = cost * cosf
            ny = cost * sinf
            nz = sint

            # rotate around X by A (affects y,z)
            y1 = y * cosA - z * sinA
            z1 = y * sinA + z * cosA
            x1 = x

            # rotate around Z by B (affects x,y)
            x2 = x1 * cosB - y1 * sinB
            y2 = x1 * sinB + y1 * cosB
            z2 = z1

            # rotate normal vector the same way
            ny1 = ny * cosA - nz * sinA
            nz1 = ny * sinA + nz * cosA
            nx1 = nx
            nx2 = nx1 * cosB - ny1 * sinB
            ny2 = nx1 * sinB + ny1 * cosB
            nz2 = nz1

            # perspective projection
            # shift viewer distance to avoid division by zero
            K = 5.0
            if (K + z2) == 0:
                continue
            factor = k1 / (K + z2)
            xp = int(width / 2 + factor * x2)
            yp = int(height / 2 - factor * y2)

            if 0 <= xp < width and 0 <= yp < height:
                idx = xp + yp * width
                if factor > zbuf[idx]:
                    zbuf[idx] = factor
                    # lighting: dot product with light vector (0, 0, 1) => nz2
                    lum = nx2 * 0.0 + ny2 * 0.0 + nz2 * 1.0
                    # normalize lum from [-1,1] to [0,1]
                    lum_norm = max(0.0, min(1.0, (lum + 1.0) / 2.0))
                    cidx = int(lum_norm * (len(CHARS) - 1))
                    out[idx] = CHARS[cidx]

    # join lines
    lines = []
    for row in range(height):
        start = row * width
        lines.append(''.join(out[start:start + width]))
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='ASCII rotating donut')
    parser.add_argument('--frames', '-n', type=int, default=0,
                        help='Number of frames to run (0 = infinite)')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--height', type=int, default=24)
    parser.add_argument('--speed', type=float, default=0.05,
                        help='Seconds per frame')
    args = parser.parse_args()

    width = args.width
    height = args.height
    frames = args.frames
    speed = args.speed

    A = 0.0
    B = 0.0

    try:
        count = 0
        while True:
            s = render_frame(A, B, width=width, height=height)
            clear_screen()
            print(s)
            time.sleep(speed)
            A += 0.07
            B += 0.03
            count += 1
            if frames and count >= frames:
                break
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

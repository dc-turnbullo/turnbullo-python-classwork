import math
import time
import sys
import os

def render_donut():
    """
    Renders a rotating 3D donut using ASCII characters.
    Based on the famous donut.c code by Andy Sloane.
    """
    
    # Constants for the math and rendering
    A = 0
    B = 0
    
    # Screen dimensions
    screen_width = 80
    screen_height = 24
    
    # Character set for luminance (from dark to light)
    chars = ".,-~:;=!*#$@"
    
    # Clear console command based on OS
    clear_console = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_console)

    while True:
        # Initialize the buffers
        # b: The ASCII character buffer (what we see)
        # z: The Z-buffer (depth to handle overlapping)
        b = [' '] * (screen_width * screen_height)
        z = [0] * (screen_width * screen_height)
        
        # Theta goes around the cross-sectional circle of a torus
        # Phi goes around the center of revolution of a torus
        
        # Pre-calculating sines and cosines of rotation angles A and B
        cosA = math.cos(A)
        sinA = math.sin(A)
        cosB = math.cos(B)
        sinB = math.sin(B)
        
        # Loop through theta (j)
        j = 0
        while j < 6.28: # 2*pi
            cosj = math.cos(j)
            sinj = math.sin(j)
            
            # Loop through phi (i)
            i = 0
            while i < 6.28: # 2*pi
                sini = math.sin(i)
                cosi = math.cos(i)
                
                # The math behind the rotation and projection
                # h: calculated distance from the center of the torus tube
                h = cosj + 2 
                
                # D: 1 / z (inverse depth) - used for perspective
                # This formula handles the 3D coordinates calculation
                D = 1 / (sini * h * sinA + sinj * cosA + 5)
                
                # t: temporary variable for y-coordinate calculation
                t = sini * h * cosA - sinj * sinA
                
                # Calculate screen coordinates (x, y)
                # 40 and 12 are offsets to center it on an 80x24 screen
                # 30 and 15 are scale factors for width and height
                x = int(40 + 30 * D * (cosi * h * cosB - t * sinB))
                y = int(12 + 15 * D * (cosi * h * sinB + t * cosB))
                
                # Calculate the memory address (index) in the buffer
                o = x + screen_width * y
                
                # Calculate luminance (L)
                # Determines which ASCII character to use based on lighting
                L = (math.cos(i) * cosj * sinB - cosA * cosj * sini - 
                     sinA * sinj + cosB * (cosA * sini - sinj * sinA * sini))
                
                # If the point is on the screen and closer than previous points
                if 0 <= y < screen_height and 0 <= x < screen_width and D > z[o]:
                    z[o] = D
                    # Pick the character based on luminance
                    # Multiplied by 8 to map the -sqrt(2) to sqrt(2) range to indices
                    idx = int(L * 8)
                    if idx > 0:
                        b[o] = chars[idx if idx < len(chars) else len(chars) - 1]
                
                i += 0.02
            j += 0.07

        # Print the frame
        # \x1b[H moves the cursor to the top-left corner without clearing the
        # whole screen (prevents flickering)
        sys.stdout.write('\x1b[H' + ''.join(b))
        sys.stdout.flush()
        
        # Increment rotation angles
        A += 0.04
        B += 0.02
        
        # Control speed
        time.sleep(0.01)

if __name__ == "__main__":
    try:
        render_donut()
    except KeyboardInterrupt:
        print("\nDonut stopped.")
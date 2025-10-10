import time

w = 24
h = 12

for y in range(0, h):
        num_stars = 2 * y + 1
        


        start_index = (w - num_stars)
        end_index = w

        for x in range(0, w):
                if (start_index <= x <= end_index):
                        print("\033[92m*", end="", flush = True)

                else:
                        print("\033[96m.",end="", flush = True)
                time.sleep(0.01)
        print("\033[0m")

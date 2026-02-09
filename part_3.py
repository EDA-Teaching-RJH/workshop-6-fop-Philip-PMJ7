
try:
    speed = int(input("Enter Motor Speed (0-100): "))
    print(f"Speed set to [{speed}]")
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")


def get_coordinate():
    while True:
        try:
            x_coord = int(input("Enter the x Coordinate: "))
        except ValueError:
            print("Invalid Coordinate.")
        else:
            if x_coord > 100 or x_coord < -100:
                print("Coordinate out of range")
                continue
            else:
                break

get_coordinate()
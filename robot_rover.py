"""
Robot Rover
"""
def faceLeft(current_direction):
    if current_direction == "North":
        current_direction = "West"
    elif current_direction == "West":
        current_direction = "South"
    elif current_direction == "South":
        current_direction = "East"
    else:
        current_direction = "North"
    return current_direction

def faceRight(current_direction):
    if current_direction == "North":
        current_direction = "East"
    elif current_direction == "East":
        current_direction = "South"
    elif current_direction == "South":
        current_direction = "West"
    else:
        current_direction = "North"
    return current_direction

def move(current_direction, current_position):
    if current_direction == "North":
        current_position[1] += 1
    elif current_direction == "West":
        current_position[0] -= 1
    elif current_direction == "East":
        current_position[0] += 1
    else:
        current_position[1] -= 1
    return current_position

greet = "Hello! Robot coming online."
help_message = "Command the robot with:\n\tL - turn left\n\tR - turn right\n\tM - move forward\n\t? - print this message\n\tQ - quit"
print(greet)
print(help_message)

command = ""
current_direction = "North"
current_position = [0, 0]

while command!="Q":
    command = raw_input()
    if command == "L":
        current_direction = faceLeft(current_direction)
        print("Robot at ({}, {}) facing {}".format(current_position[0], current_position[1], current_direction))
    elif command == "R":
        current_direction = faceRight(current_direction)
        print("Robot at ({}, {}) facing {}".format(current_position[0], current_position[1], current_direction))
    elif command == "M":
        current_position = move(current_direction, current_position)
        print("Robot at ({}, {}) facing {}".format(current_position[0], current_position[1], current_direction))
    elif command == "?":
        print(help_message)

print("Robot shutting down.")
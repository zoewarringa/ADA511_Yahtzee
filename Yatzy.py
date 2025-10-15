import random

class Die:
    def __init__(self):
        self.face = random.randint(1, 6)

    def roll(self):
        self.face = random.randint(1, 6)


def main():
    # Setup dice
    num_dice = 2
    dice_list = [Die() for _ in range(num_dice)]

    # Showing first roll
    print("First roll:")
    print(" ".join(str(d.face) for d in dice_list))

    num_dice_counts = [0] * 6
    biggest_value = 0
    die_to_keep = 0

    # Count occurrences and decide which face to keep
    for i in range(6):
        face_val = i + 1
        num_dice_counts[i] = sum(1 for d in dice_list if d.face == face_val)
        print(f"{num_dice_counts[i]} number of {face_val}")

        if num_dice_counts[i] >= 2 and biggest_value <= (num_dice_counts[i] * face_val):
            biggest_value = num_dice_counts[i] * face_val
            die_to_keep = face_val
            print(f"Pair of {die_to_keep} with the value {biggest_value}")
        elif face_val >= biggest_value and num_dice_counts[i] != 0:
            biggest_value = face_val
            die_to_keep = face_val
            print(f"The die to keep is {die_to_keep}")

    print()
    # Reroll any dice that aren't the chosen face
    for d in dice_list:
        if d.face != die_to_keep:
            d.roll()

    print("After reroll:")
    print(" ".join(str(d.face) for d in dice_list))



if __name__ == "__main__":
    main()

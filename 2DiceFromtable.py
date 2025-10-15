import pandas as pd
import random

# Load Table
df_util = pd.read_csv('Data/2Dice_Table.csv')

baseline = 5.0556

def get_decision(dice):
    die1, die2 = dice

    # Look for the exact pair in either order
    row = df_util[
        ((df_util['Die 1'] == die1) & (df_util['Die 2'] == die2)) |
        ((df_util['Die 1'] == die2) & (df_util['Die 2'] == die1))
    ]

    if not row.empty:
        utility = row.iloc[0]['Utility']
    else:
        utility = 0
        print('No such values in table')

    # Decide based on baseline
    if die1 == die2:
        # Keep both of pair if utility above baseline
        if utility > baseline:
            decisions = ['KEEP', 'KEEP']
        else:
            decisions = ['REROLL', 'REROLL']
    else:
        # Keep only the die with highest utility if above baseline
        if die1 > die2:
            decisions = ['KEEP', 'REROLL'] if utility > baseline else ['REROLL', 'REROLL']
        else:
            decisions = ['REROLL', 'KEEP'] if utility > baseline else ['REROLL', 'REROLL']

    utilities = utility
    return decisions, utilities

def roll_die():
    return random.randint(1, 6)

def throws(num_throws=3):
    dice = [roll_die(), roll_die()]
    results = []

    for throw_num in range(1, num_throws + 1):
        # Calculate decisions and utilities for current dice
        decisions, utilities = get_decision(dice)

        # Store results
        throw_result = {
            'Die 1': dice[0],
            'Die 2': dice[1],
            'Decision': decisions,
            'Utility': utilities
        }
        results.append(throw_result)

        # Reroll dice that are not kept
        dice = [die if dec == 'KEEP' else roll_die() for die, dec in zip(dice, decisions)]

    return pd.DataFrame(results)


# Main
def main():
    df_results = throws(3)
    print(df_results)

if __name__ == "__main__":
    main()

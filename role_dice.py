import random
from collections import defaultdict
import matplotlib.pyplot as plt


def roll_dice(num_rolls: int) -> dict:
    """
    Simulates rolling two dice and calculates the sums and their probabilities.

    Args:
        num_rolls (int): The number of times to roll the dice.

    Returns:
        dict: A dictionary with sums as keys and their probabilities as values.
    """
    sums_count = defaultdict(int)

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums_count[die1 + die2] += 1

    # Calculate probabilities
    probabilities = {
        sum_: count / num_rolls for sum_,
        count in sums_count.items()
    }
    return probabilities


def plot_probabilities(probabilities: dict):
    """
    Plots the probabilities of sums when rolling two dice.

    Args:
        probabilities (dict): A dictionary with sums as keys and probabilities as values.
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Sums from Rolling Two Dice')
    plt.xticks(sums)
    plt.ylim(0, max(probs) + 0.05)
    plt.grid(axis='y')
    plt.show()


def main(num_rolls: int = 10000):
    """
    Main function to execute the Monte Carlo simulation for rolling dice.

    Args:
        num_rolls (int): The number of times to roll the dice.
    """
    probabilities = roll_dice(num_rolls)
    plot_probabilities(probabilities)


def test_roll_dice():
    """Tests the roll_dice function."""
    num_rolls = 10000
    probabilities = roll_dice(num_rolls)

    assert all(sum_ in probabilities for sum_ in range(
        2, 13)), "Sums must be between 2 and 12."
    assert sum(probabilities.values()) == 1, "Probabilities must sum up to 1."
    print("Tests passed")


if __name__ == "__main__":
    # Run the test
    test_roll_dice()
    main()

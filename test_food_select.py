

def greedy_algorithm(items, budget):
    """
    Greedy algorithm to maximize calories within a given budget.

    :param items: Dictionary of food items with cost and calories.
    :param budget: Maximum budget allowed.
    :return: List of selected food items.
    """
    # Calculate the value (calories/cost) for each item
    value_items = [
        (name, item['calories'] / item['cost'], item['cost'], item['calories'])
        for name, item in items.items()
    ]
    # Sort items by value in descending order
    value_items.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    for name, value, cost, calories in value_items:
        if total_cost + cost <= budget:
            total_cost += cost
            total_calories += calories
            selected_items.append(name)

    return selected_items


def dynamic_programming(items, budget):
    """
    Dynamic programming algorithm to maximize calories within a given budget.

    :param items: Dictionary of food items with cost and calories.
    :param budget: Maximum budget allowed.
    :return: List of selected food items.
    """
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, data in items.items():
        cost = data['cost']
        calories = data['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b] < dp[b - cost] + calories:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    max_calories = max(dp)
    selected_items = item_selection[dp.index(max_calories)]
    return max_calories, selected_items


def test_food_selection():
    """Tests the food selection algorithms."""
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Test greedy algorithm
    budget = 100
    greedy_selection = greedy_algorithm(items, budget)
    print(f"Greedy selection (Budget: {budget}): {greedy_selection}")

    # Validate greedy selection
    greedy_cost = sum(items[item]['cost'] for item in greedy_selection)
    assert greedy_cost <= budget, "Greedy selection exceeded budget!"

    # Calculate total calories for greedy selection
    greedy_calories = sum(items[item]['calories'] for item in greedy_selection)
    print(f"Total calories from greedy selection: {greedy_calories}")

    # Test dynamic programming
    total_calories, dp_selection = dynamic_programming(items, budget)
    print(f"Dynamic programming selection (Budget: {budget}): {
          dp_selection}, Total calories: {total_calories}")

    # Validate dynamic programming selection
    dp_cost = sum(items[item]['cost'] for item in dp_selection)
    assert dp_cost <= budget, "Dynamic programming selection exceeded budget!"

    # Validate total calories
    dp_calories = sum(items[item]['calories'] for item in dp_selection)
    assert dp_calories == total_calories, "Mismatch in total calories for dynamic programming selection!"

    print("All tests passed!")


# Run the tests
test_food_selection()

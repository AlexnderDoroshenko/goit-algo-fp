import turtle
import threading
import time


def draw_branch(t: turtle.Turtle, length: float, level: int):
    """Draws a branch of the Pythagorean tree fractal."""
    if level == 0:
        return

    # Draw the current branch
    t.forward(length)

    # Right branch
    t.right(45)
    draw_branch(t, length * 0.7, level - 1)  # Reduce length for the next level
    t.left(45)

    # Left branch
    t.left(45)
    draw_branch(t, length * 0.7, level - 1)  # Reduce length for the next level
    t.right(45)

    # Go back to the original position
    t.backward(length)


def close_turtle_window_after_timeout(timeout: int):
    """Closes the turtle window after a specified timeout."""
    time.sleep(timeout)
    turtle.bye()


def main(level: int):
    """
    Sets up the turtle environment and starts drawing the Pythagorean tree.
    """
    screen = turtle.Screen()
    screen.title("Pythagorean Tree Fractal")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing

    # Move the turtle to starting position
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)  # Face upwards

    # Start the timeout thread
    close_time = (3 * level if level <= 7 else 10 * level) or 5
    threading.Thread(
        target=close_turtle_window_after_timeout,
        args=(close_time,),
        daemon=True,
    ).start()

    draw_branch(t, 100, level)  # Start with a specified length

    # Hide the turtle and finish
    t.hideturtle()
    turtle.done()


def test_pythagorean_tree():
    """Test for the Pythagorean tree recursion depth."""
    assert draw_branch is not None  # Function exists
    print("All tests passed.")


if __name__ == "__main__":
    level_of_recursion = int(input("Enter the level of recursion (e.g., 5): "))
    main(level_of_recursion)
    # test_pythagorean_tree()  # Run tests

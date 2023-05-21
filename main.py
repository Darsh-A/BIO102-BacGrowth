"""
This is the main code to generate bacteria growth with parameters defined below

TO RUN:
first install all the required packages: manim, numpy, opencv-python
then run the following command in the terminal:
manim main.py CircleWithDot -pql -s
"""


from manim import *
import random

deviation_of_new_bacteria = 30  # Note this is Inverse check line38
numer_of_bacteria = 200
probability_of_new_colony = 0.35

# Create any random Point inside the Circle
def random_point_in_circle(circle):
    radius = circle.radius
    x, y = random.uniform(-radius, radius), random.uniform(-radius, radius)
    while x**2 + y**2 > radius**2:
        x, y = random.uniform(-radius, radius), random.uniform(-radius, radius)
    return circle.get_center() + np.array([x, y, 0])

def random_point_nearby(dots, circle):
    total_dots = len(dots)
    distances = np.zeros(total_dots)
    for i, dot in enumerate(dots):
        distances[i] = np.linalg.norm(dot.get_center() - circle.get_center())
    weights = 10 / (distances + 0.0001)  # Increase weights for closer dots
    weights /= np.sum(weights)  # Normalize weights to make them probabilities
    selected_dot = random.choices(dots, weights=weights)[0]
    selected_dot_pos = selected_dot.get_center()
    radius = circle.radius
    deviation = radius / deviation_of_new_bacteria  # Adjust the deviation to make dots closer
    new_point = np.array([
        selected_dot_pos[0] + random.uniform(-deviation, deviation),
        selected_dot_pos[1] + random.uniform(-deviation, deviation),
        selected_dot_pos[2]
    ])
    while np.linalg.norm(new_point - circle.get_center()) > radius:
        new_point = np.array([
            selected_dot_pos[0] + random.uniform(-deviation, deviation),
            selected_dot_pos[1] + random.uniform(-deviation, deviation),
            selected_dot_pos[2]
        ])
    return new_point

# MAIN SCENE

class BacteriaGrowth(Scene):
    def construct(self):
        # Create a circle with thickness
        circle = Circle(radius=4, color=BLUE, stroke_width=5)

        # Add the circle to the scene
        self.add(circle)
        num_dots = numer_of_bacteria
        dot_radius = 0.05
        dots = VGroup(*[Dot(color=RED, radius=dot_radius) for _ in range(num_dots)])

        # Create a dot and add to the scene
        for i in range(num_dots):
            new_colony = random.random()
            dot = dots[i]
            if i > 0:
                if new_colony < probability_of_new_colony:
                    dot.move_to(random_point_in_circle(circle))
                else:
                    previous_dots = list(dots[:i])
                    dot.move_to(random_point_nearby(previous_dots, circle))
            else:
                dot.move_to(random_point_in_circle(circle))

            self.add(dot)
            self.wait(0.1)

import turtle
import random
import math

def random_polygon():
    # Random number of sides between 3 and 10
    num_sides = random.randint(3, 10)
    # Random radius between 50 and 150
    radius = random.randint(50, 150)
    
    # Calculate the vertices coordinates
    angle_step = 360 / num_sides
    points = []
    for i in range(num_sides):
        angle_deg = i * angle_step
        angle_rad = math.radians(angle_deg)
        x = radius * math.cos(angle_rad)
        y = radius * math.sin(angle_rad)
        points.append((x, y))
    
    return points

def draw_polygon(points):
    t = turtle.Turtle()
    t.penup()
    t.goto(points[0])
    t.pendown()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])  # Close the polygon
    t.hideturtle()

def main():
    screen = turtle.Screen()
    screen.title("Random Polygon")
    points = random_polygon()
    draw_polygon(points)
    turtle.done()

if __name__ == "__main__":
    main()

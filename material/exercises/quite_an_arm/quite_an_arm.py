"""
Credit - Principles of Physics: A calculus-based text (4th Edition) by Serway & Jewett
Problem - Interactive Example 3.2: That's Quite an Arm

A stone is thrown from the top of a building at an angle of 30.0º to the horizontal and with an initial speed of 20.0 ms, as in the following figure.
[A] If the height of the building is 45.0m, how long is the stone "in flight"?
[B] What is the speed of the stone just before it strikes the ground?
"""

from vpython import *

building_height = 45
building = box(pos=vector(0, building_height/2, 0), length=1, width=1, height=building_height, color=color.blue)
stone = sphere(pos=vector(building.pos.x, building.pos.y+building.height/2, building.pos.z), radius=1, color=color.red)
ground_length = 100
ground = box(pos=vector(building.pos.x+ground_length/2, building.pos.y-building.height/2, building.pos.z), length=ground_length, width=1, height=1, color=color.black)

vel = vector(20*cos(30*pi/180), 20*sin(30*pi/180), 0)
acc = vector(0, -9.8, 0)
t = 0
dt = 0.01

scene.background = color.white
scene.center = vector(ground_length/2, building_height/2, 0)

if __name__ == "__main__":
    while True:
        rate(100)
        vel += acc*dt
        stone.pos += vel*dt
        t += dt
        if stone.pos.y < ground.pos.y:
            print(f"[A] Time in flight: {t} (s).")
            print(f"[B] Speed just before end: {vel.mag} (m/s).")
            break
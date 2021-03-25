"""
This is a sample  program to show how to draw using the Python programming
Language and the Arcade Library.

Multi-line comments are surrounded by three of the double- quote marks.
Single-line comments start with a hash/pound sign. #
"""

# This is a single line comment
import arcade

def red_fish():
    #fish
    arcade.draw_ellipse_filled(300, 300, 200, 60, arcade.csscolor.SALMON)
    arcade.draw_triangle_filled(220, 300, 50, 250, 50, 350, arcade.csscolor.RED)
    arcade.draw_triangle_filled(320, 300, 280, 320, 280, 280, arcade.csscolor.RED)
    arcade.draw_circle_filled(360, 310, 5, arcade.csscolor.BLACK)

def blue_fish():
    #fish
    arcade.draw_ellipse_filled(360, 450, 200, 60, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_triangle_filled(280, 450, 110, 400, 110, 500, arcade.csscolor.BLUE)
    arcade.draw_triangle_filled(380, 450, 340, 470, 340, 430, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(420, 460, 5, arcade.csscolor.BLACK)

def bubble():
    # this is the function to print bubbles
    arcade.draw_circle_outline(100, 200, 15, arcade.csscolor.WHITE)
    arcade.draw_circle_outline(230, 400, 15, arcade.csscolor.WHITE)

def bubbles_two():
    # another set of bubbles!
    arcade.draw_circle_outline(470, 210, 15, arcade.csscolor.WHITE)
    arcade.draw_circle_outline(485, 550, 15, arcade.csscolor.WHITE)

def bubbles_three():
    # final set of bubbles
    arcade.draw_circle_outline(300, 350, 15, arcade.csscolor.WHITE)
    arcade.draw_circle_outline(400, 500, 15, arcade.csscolor.WHITE)

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.LIGHT_SEA_GREEN)

# Get ready to draw
arcade.start_render()

red_fish()

blue_fish()

bubble()

bubbles_two()

bubbles_three()

# seaweed
arcade.draw_lrtb_rectangle_filled(0, 600, 100, 0, arcade.csscolor.SEA_GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

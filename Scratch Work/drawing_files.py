"""
This is a sample  program to show how to draw using the Python programming
Language and the Arcade Library.

Multi-line comments are surrounded by three of the double- quote marks.
Single-line comments start with a hash/pound sign. #
"""

# This is a single line comment
import arcade
# open up a window.
# from the "arcade" library, use a function called "open_window"
# set the window title to "Drawing Example"
# set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.LIGHT_SEA_GREEN)

# Get ready to draw
arcade.start_render()

# full fish
arcade.draw_ellipse_filled(300, 300, 200, 60, arcade.csscolor.SALMON)
arcade.draw_triangle_filled(220, 300, 50, 250, 50, 350, arcade.csscolor.RED)
arcade.draw_triangle_filled(320, 300, 280, 320, 280, 280, arcade.csscolor.RED)
arcade.draw_circle_filled(360, 310, 5, arcade.csscolor.BLACK)
# second fish
arcade.draw_ellipse_filled(360, 450, 200, 60, arcade.csscolor.LIGHT_BLUE)
arcade.draw_triangle_filled(280, 450, 110, 400, 110, 500, arcade.csscolor.BLUE)
arcade.draw_triangle_filled(380, 450, 340, 470, 340, 430, arcade.csscolor.BLUE)
arcade.draw_circle_filled(420, 460, 5, arcade.csscolor.BLACK)

# seaweed
arcade.draw_lrtb_rectangle_filled(0, 600, 100, 0, arcade.csscolor.SEA_GREEN)

#bubbles
arcade.draw_circle_outline(100, 200, 15, arcade.csscolor.WHITE)
arcade.draw_circle_outline(230, 400, 15, arcade.csscolor.WHITE)
arcade.draw_circle_outline(300, 350, 15, arcade.csscolor.WHITE)
arcade.draw_circle_outline(400, 500, 15, arcade.csscolor.WHITE)
arcade.draw_circle_outline(470, 210, 15, arcade.csscolor.WHITE)
arcade.draw_circle_outline(485, 550, 15, arcade.csscolor.WHITE)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

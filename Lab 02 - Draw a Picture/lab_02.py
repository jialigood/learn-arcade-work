import arcade

arcade.open_window(600, 600, "drawing window")
arcade.set_background_color(arcade.color.LIGHT_GRAY)
arcade.start_render()

# DRAWING BOB ROSS
# head
arcade.draw_ellipse_filled(300, 350, 300, 250, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(300, 300, 100, arcade.csscolor.ANTIQUE_WHITE)
# eyes
arcade.draw_circle_filled(260, 325, 10, arcade.csscolor.BLACK)
arcade.draw_circle_filled(340, 325, 10, arcade.csscolor.BLACK)

# shirt
arcade.draw_circle_filled(300, 0, 250, arcade.csscolor.LIGHT_BLUE)
# shirt pocket
arcade.draw_rectangle_filled(225, 150, 60, 60, arcade.csscolor.DARK_CYAN)
arcade.draw_line(195, 180, 225, 155, arcade.csscolor.LIGHT_BLUE)
arcade.draw_line(255, 180, 225, 155, arcade.csscolor.LIGHT_BLUE)

# beard
arcade.draw_ellipse_filled(300, 250, 180, 95, arcade.color.DARK_BROWN)
# mouth
arcade.draw_ellipse_filled(300, 260, 90, 40, arcade.csscolor.ANTIQUE_WHITE)
arcade.draw_ellipse_filled(300, 260, 70, 30, arcade.csscolor.PINK)
arcade.draw_ellipse_filled(300, 265, 70, 25, arcade.csscolor.ANTIQUE_WHITE)

arcade.finish_render()
arcade.run()

import arcade

arcade.open_window(800, 600, "drawing window")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

#rectangle
arcade.draw_rectangle_outline(400, 300, 700, 400, arcade.color.BLUE, 10)
#4 short vertical lines
arcade.draw_line(240, 500, 240, 420, arcade.color.BLUE, 10)
arcade.draw_line(560, 500, 560, 420, arcade.color.BLUE, 10)
arcade.draw_line(240, 100, 240, 180, arcade.color.BLUE, 10)
arcade.draw_line(560, 100, 560, 180, arcade.color.BLUE, 10)
#middle horizontal lines
arcade.draw_line(305, 420, 495, 420, arcade.color.BLUE, 10)
arcade.draw_line(305, 180, 495, 180, arcade.color.BLUE, 10)
#L shaped lines- vertical
arcade.draw_line(115, 420, 165, 420, arcade.color.BLUE, 10)
arcade.draw_line(115, 180, 165, 180, arcade.color.BLUE, 10)
arcade.draw_line(625, 180, 685, 180, arcade.color.BLUE, 10)
arcade.draw_line(625, 420, 685, 420, arcade.color.BLUE, 10)
#L shaped lines- horizontal
arcade.draw_line(115, 420, 115, 325, arcade.color.BLUE, 10)
arcade.draw_line(115, 180, 115, 245, arcade.color.BLUE, 10)
arcade.draw_line(685, 420, 685, 325, arcade.color.BLUE, 10)
arcade.draw_line(685, 180, 685, 245, arcade.color.BLUE, 10)

#middle square thing
arcade.draw_line(305, 245, 495, 245, arcade.color.BLUE, 10)
arcade.draw_line(435, 355, 495, 355, arcade.color.BLUE, 10)
arcade.draw_line(305, 355, 365, 355, arcade.color.BLUE, 10)
arcade.draw_line(495, 355, 495, 245, arcade.color.BLUE, 10)
arcade.draw_line(305, 355, 306, 245, arcade.color.BLUE, 10)

#short horizontal lines
arcade.draw_line(565, 355, 625, 355, arcade.color.BLUE, 10)
arcade.draw_line(175, 355, 235, 355, arcade.color.BLUE, 10)
arcade.draw_line(565, 245, 625, 245, arcade.color.BLUE, 10)
arcade.draw_line(175, 245, 235, 245, arcade.color.BLUE, 10)

#ghost dude
arcade.draw_circle_filled(272, 420, 18, arcade.color.AZURE)
arcade.draw_rectangle_filled(272, 409, 30, 10, arcade.color.AZURE)
arcade.draw_circle_filled(265, 425, 7, arcade.color.WHITE)
arcade.draw_circle_filled(279, 425, 7, arcade.color.WHITE)
arcade.draw_circle_filled(266, 424, 4, arcade.color.BLACK)
arcade.draw_circle_filled(278, 424, 4, arcade.color.BLACK)
#second ghost dude
arcade.draw_circle_filled(207, 140, 18, arcade.color.ORANGE)
arcade.draw_rectangle_filled(207, 129, 30, 10, arcade.color.ORANGE)
arcade.draw_circle_filled(200, 145, 7, arcade.color.WHITE)
arcade.draw_circle_filled(214, 145, 7, arcade.color.WHITE)
arcade.draw_circle_filled(201, 144, 4, arcade.color.BLACK)
arcade.draw_circle_filled(213, 144, 4, arcade.color.BLACK)

arcade.finish_render()
arcade.run()

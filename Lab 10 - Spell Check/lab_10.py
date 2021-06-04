import arcade

percent = 80


# if you get less than 100%
result = f"ALMOST THERE! you got {percent}%"
arcade.open_window(600, 600, "drawing window")
arcade.set_background_color(arcade.color.PISTACHIO)
arcade.start_render()
# bubbles again
bubbles()
# text
arcade.draw_text(result, 20, 400, arcade.color.DARK_GREEN, 38)
arcade.draw_text(result, 22, 402, arcade.color.WHITE, 38)




arcade.finish_render()
arcade.run()
import arcade

window_opening = False



while not window_opening:
    arcade.open_window(600, 600, "drawing window")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    arcade.run()

    def on_mouse_press(button):
        if button == arcade.MOUSE_BUTTON_LEFT:
            window_opening = True

arcade.finish_render()

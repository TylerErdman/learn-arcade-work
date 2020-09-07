import arcade

arcade.open_window(500, 500, "My Cat")

arcade.set_background_color(arcade.color.SEA_BLUE)

arcade.start_render()

# Start with the background
arcade.draw_lrtb_rectangle_filled(0, 500, 100, 0, arcade.color.BITTER_LIME)
arcade.draw_lrtb_rectangle_filled(0, 500, 200, 100, arcade.color.BOTTLE_GREEN)
arcade.draw_lrtb_rectangle_filled(0, 500, 500, 400, arcade.color.SHADOW_BLUE)

# Drawing a rainbow
arcade.draw_arc_outline(250, 0, 750, 750, arcade.color.VIOLET, 0, 180, 30)
arcade.draw_arc_outline(250, 10, 750, 750, arcade.color.INDIGO, 0, 180, 30)
arcade.draw_arc_outline(250, 20, 750, 750, arcade.color.BLUE, 0, 180, 30)
arcade.draw_arc_outline(250, 30, 750, 750, arcade.color.GREEN, 0, 180, 30)
arcade.draw_arc_outline(250, 40, 750, 750, arcade.color.YELLOW, 0, 180, 30)
arcade.draw_arc_outline(250, 50, 750, 750, arcade.color.ORANGE, 0, 180, 30)
arcade.draw_arc_outline(250, 60, 750, 750, arcade.color.RED, 0, 180, 30)

# Then I draw the sun
arcade.draw_circle_filled(325, 350, 50, arcade.color.YELLOW)

# Sun has to have sunglasses
arcade.draw_ellipse_filled(350, 360, 40, 25, arcade.color.BLACK)
arcade.draw_ellipse_filled(300, 360, 40, 25, arcade.color.BLACK)
arcade.draw_line(300, 360, 370, 360, arcade.color.BLACK)

# Cat Body
arcade.draw_ellipse_filled(240, 155, 150, 40, arcade.color.CADET_GREY)

# Cat Legs
arcade.draw_lrtb_rectangle_filled(200, 210, 155, 60, arcade.color.CADET_GREY)
arcade.draw_lrtb_rectangle_filled(215, 225, 155, 60, arcade.color.CADET_GREY)
arcade.draw_lrtb_rectangle_filled(260, 270, 155, 60, arcade.color.CADET_GREY)
arcade.draw_lrtb_rectangle_filled(280, 290, 155, 60, arcade.color.CADET_GREY)

# Cat Tail
arcade.draw_line_strip([[300, 155], [325, 170], [325, 220], [350, 230]], arcade.color.BLACK, 5)

# Start of Cat head
arcade.draw_polygon_filled([[200, 175],
                            [150, 175],
                            [164, 125],
                            [190, 130]], arcade.color.ASH_GREY)
arcade.draw_circle_filled(175, 135, 7, arcade.color.PINK)
arcade.draw_circle_filled(190, 160, 5, arcade.color.BLACK)
arcade.draw_circle_filled(170, 160, 5, arcade.color.BLACK)

# Ears
arcade.draw_triangle_filled(150, 175, 175, 200, 170, 175, arcade.color.BLACK)
arcade.draw_triangle_filled(180, 175, 190, 200, 200, 175, arcade.color.BLACK)

# Whiskers
arcade.draw_line_strip([[145, 125], [165, 130]], arcade.color.BLACK, 2)
arcade.draw_line_strip([[145, 135], [165, 135]], arcade.color.BLACK, 2)
arcade.draw_line_strip([[145, 150], [165, 140]], arcade.color.BLACK, 2)
arcade.draw_line_strip([[190, 150], [210, 160]], arcade.color.BLACK, 2)
arcade.draw_line_strip([[190, 145], [210, 142]], arcade.color.BLACK, 2)
arcade.draw_line_strip([[190, 140], [210, 135]], arcade.color.BLACK, 2)

# Cat feet
arcade.draw_arc_filled(200, 60, 20, 20, arcade.color.BLACK, 0, 180)
arcade.draw_arc_filled(215, 60, 20, 20, arcade.color.BLACK, 0, 180)
arcade.draw_arc_filled(260, 60, 20, 20, arcade.color.BLACK, 0, 180)
arcade.draw_arc_filled(280, 60, 20, 20, arcade.color.BLACK, 0, 180)

arcade.finish_render()

arcade.run()

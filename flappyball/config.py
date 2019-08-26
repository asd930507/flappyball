game_frame = 60
window_size_x = 320
window_size_y = 240
gravity = window_size_y * 5

game_background_color = 211, 211, 211
text_color = 0, 0, 255
ball_color = 238, 0, 0
pipeline_color = 0, 139, 0

ball_radius = int(window_size_y * 0.025)
ball_jump_speed = -ball_radius * 55

pipeline_length = ball_radius * 2
pipeline_free_space_length = ball_radius * 16
pipeline_distance = ball_radius * 22
pipeline_horizontal_speed = -ball_radius * 40

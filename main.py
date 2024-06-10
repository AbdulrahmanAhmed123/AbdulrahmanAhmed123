import turtle

face_one = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100),
             (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20),
             (0, -20)],
            [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
             (170, 100), (170, 200), (130, 230), (70, 260), (40, 120),
             (0, 120)]]

face_two = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
             (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230),
             (-64, -210), (0, -210)],
            [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170),
             (186, -40), (186, -30), (176, 0), (130, -40), (100, -46),
             (50, -40), (40, -30), (0, -30)]]

face_three = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250),
               (-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],
              [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280),
               (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]]
face_four = [[(-200, -250), (100, -40)], [(100, 0), (-200, -250)]]
face_four1 = [[(200, -250), (-120, 10)], [(-120, -20), (200, -250)]]
turtle.hideturtle()
turtle.bgcolor('#3C4E8E')
turtle.setup(500, 600)

first_one_start = (0, 120)
second_one_start = (0, -30)
third_one_start = (0, -220)
fourth_one_start = (-200, -250)
fourth1_one_start = (200, -250)
turtle.speed(2)


def draw_face(face_details_list, start_point, color):
  turtle.penup()
  turtle.goto(start_point)
  turtle.pendown()
  turtle.color(color)
  turtle.begin_fill()
  for i in range(len(face_details_list[0])):
    x, y = face_details_list[0][i]
    turtle.goto(x, y)
  for i in range(len(face_details_list[1])):
    x, y = face_details_list[1][i]
    turtle.goto(x, y)
  turtle.end_fill()


draw_face(face_one, first_one_start, '#566D7E')
draw_face(face_two, second_one_start, '#1C2334')
draw_face(face_three, third_one_start, '#566D7E')
draw_face(face_four, fourth_one_start, '#1C2334')
draw_face(face_four1, fourth1_one_start, '#1C2334')
turtle.mainloop()

import pgzrun
from pygame import Rect
TITLE = "Quiz Master"
W = 800
H = 550
marquee_box = Rect(0,0,800,60)
question_box = Rect(20,80,500,140)
timer_box = Rect(550,80,200,140)
answer_box1 = Rect(20,250,200,140 )
answer_box2 = Rect(250,250,200,140)
answer_box3 = Rect(20,420,200,140)
answer_box4 = Rect(250,420,200,140)
skip_box = Rect(550,250,200,315)
answer_boxes  = [answer_box1,answer_box2,answer_box3,answer_box4]
time_left = 10
def draw():
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.textbox("Welcome To the Quiz Master",marquee_box,color = "yellow")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(timer_box,"light blue")
    screen.draw.textbox(f"{time_left}",timer_box,color="blue",scolor="dim grey",shadow=(0.5,0.5))
    screen.draw.filled_rect(skip_box,"magenta")
    screen.draw.textbox("SKIP",skip_box,angle=90,color="light green",scolor="dim grey",shadow=(0.5,0.5))

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"pink")

def update():
    marquee_box.x -= 2
    if marquee_box.right<0:
        marquee_box.left = W
def game_over():
    global time_left
    time_left=0
def update_time():
    global time_left
    if time_left>0:
        time_left = time_left-1
    else:
        game_over()


clock.schedule_interval(update_time,1)



pgzrun.go()
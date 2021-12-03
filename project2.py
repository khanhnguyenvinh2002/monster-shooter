import turtle
import math
import random
import time
#import pygame
#pygame.init()
#pygame.mixer.init()
#sounda= pygame.mixer.Sound("explosion.wav")
# make Screen
sc = turtle.Screen()
# make background
sc.bgpic("background.gif")
# make area
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, - 300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
# hide
mypen.hideturtle()

player = turtle.Turtle()
image = "anhhung.gif"
sc.addshape(image)
player.shape(image)
player.penup()
# vị trí xất hiện của siêu anh hùng
player.setposition(0, -250)
player.setheading(90)
# thiết lập tốc độ siêu anh hùng
playerspeed = 25
enemy = turtle.Turtle()
image = "quaivat.gif"
sc.addshape(image)
enemy.shape(image)
# thiết lập penup cho quái vật
enemy.penup()
enemy.speed(0)
# vị trí xuất hiện quái vật
enemy.setposition(random.randint(-300, 300), random.randint(-100, 300))
# thiết lập tốc độ
enemyspeed = 3
# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
# thiết lập tốc độ của đạn siêu anh hùng
bulletspeed = 20
# Trạng thái Súng của siêu anh hùng
bulletstate = "ready"
sung = turtle.Turtle()
sung.color("red")
sung.shape("circle")
sung.penup()
sung.speed(0)
sung.setheading(90)
sung.shapesize(0.5, 0.5)
sung.hideturtle()
# thiết lập trạng thái súng và tốc độ đạn
bulletstate_quaivat = "ready"
bulletspeed_quaivat = 20


# vũ khí của siêu anh hùng
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # đặt vũ khí ở phía trước người chơi
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# Vú khí của quái vật
def fire_bullet_quatvat():
    global bulletstate_quaivat
    if bulletstate_quaivat == "ready":
        bulletstate_quaivat = "fire"
        # đặt vũ khí ở phía trước quái vật
        x = enemy.xcor()
        y = enemy.ycor() + 10
        sung.setposition(x, y)
        sung.showturtle()


# Định nghĩa các phím di chuyển
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


# khi nhấn phím
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.listen()


# Hàm kiểm tra các đối tượng có va chạm vào nhau không
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if (distance < 20):
        return True
    else:
        return False


# Hàm kiểm tra va chạm biên
def boundaryChecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < -300 or t.ycor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))


# Ban đầu thiết lập điểm =0
score = 0
# Viết điểm lên background
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Player: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
# Ban đầu thiết lập điểm =0
score_quaivat = 0
# Viết điểm lên background
score_pen_quaivat = turtle.Turtle()
score_pen_quaivat.speed(0)
score_pen_quaivat.color("black")
score_pen_quaivat.penup()
score_pen_quaivat.setposition(200, 280)
scorestring_quaivat = "Enemy: %s" % score_quaivat
score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))
score_pen_quaivat.hideturtle()

# Main game loop
while True:
    # thiết lập di chuyển của quái vật
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    # Gọi hàm khởi tạo vũ khí và sử dụng
    fire_bullet_quatvat()
    # Điểu khiển hướng đi đạn của quái vật
    if (bulletstate_quaivat == "fire"):
        y = sung.ycor()
        y -= bulletspeed_quaivat
        sung.sety(y)
    # kiểm tra đạn vị trí botton, nếu đúng thì ẩn đạn
    if sung.ycor() < -275:
        sung.hideturtle()
        bulletstate_quaivat = "ready"

    # Move the enemy back and down
    if enemy.xcor() > 280:
        # Move all enemies down
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        # Change enemy direction
        enemyspeed *= -1
    if enemy.xcor() < -280:
        # Move all enemies down
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        # Change enemy direction
        enemyspeed *= -1
    # Kiểm tra va chạm giữa đạn của siêu anh hùng và quái vật
    if isCollision(bullet, enemy):
        #sounda.play()
        # Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        # Cập cật điểm
        score += 10
        scorestring = "Player: %s" % score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    # Kiểm tra va chạm giữa đạn của quái vật và siêu anh hùng
    if isCollision(sung, player):
        #sounda.play()
        # Reset the bullet
        sung.hideturtle()
        bulletstate_quaivat = "ready"
        bullet.setposition(0, -400)

        # Reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

        # Cập nhật điểm
        score_quaivat += 10
        scorestring_quaivat = "Enemy: %s" % score_quaivat
        score_pen_quaivat.clear()
        score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))

    # va cham nguoi choi va quai vat
    if isCollision(player, enemy):
        #sounda.play()
        # os.system("afplay explosion.wav&")
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
    # Kiểm tra đạn của siêu anh hùng
    if (bulletstate == "fire"):
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    # Nếu đạn của siêu anh hùng ở di chuyển đến đỉnh thì ẩn đi
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    if score == 100 or score_quaivat == 20:
        break

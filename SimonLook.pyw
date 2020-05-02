# Bethany Cacayorin
# April 7, 2019
# ITN160 - Final Project
# Simon Look!

from guizero import App, Picture, PushButton, Box, Text
import random


widget = []  # list of widget created
quiz = []  # list of generated pics
answers = []  # list of button pressed by the user
monsters = ["monster1.png", "monster2.png", "monster3.png", "monster4.png"]
points = 0  # score counter

# --------------- defined functions ---------------


# displays the monster pics
def dsplyPage(points):
    widget[18].value = points

    widget[4].hide()  # start button
    widget[2].hide()  # simon logo
    widget[1].hide()  # box1
    widget[3].hide()  # box2

    widget[7].hide()  # box4
    widget[9].hide()  # monsterBtn 1
    widget[10].hide()  # monsterBtn 2
    widget[8].hide()  # box5
    widget[11].hide()  # monsterBtn 3
    widget[12].hide()  # monsterBtn 4

    widget[13].hide()  # box6
    widget[14].hide()  # gameoverPic
    widget[15].hide()  # box 7
    widget[16].hide()  # playagainBtn

    widget[17].show()  # box8
    widget[17].width = 350
    widget[17].height = 440
    widget[19].show()  # scoreboard
    widget[18].show()  # score

    # start genrating the pattern
    m = random.randint(0, 3)
    widget[6].image = monsters[m]
    key = widget[6].image
    answers.append(key)

    # changes duplicates
    if len(answers) != 1:
        while answers[len(answers)-2] == answers[len(answers)-1]:
            m = random.randint(0, 3)
            widget[6].image = monsters[m]
            key = widget[6].image
            answers[len(answers) - 1] = key

    timer(0, points)


# checks the score(the higher the point, shorter it will display the image)
def timer(i, points):
    if points in range(0, 14):
        widget[0].after(2000, display, args=[i, points])

    elif points in range(15, 35):
        widget[0].after(1500, display, args=[i, points])

    elif points in range(36, 77):
        widget[0].after(1000, display, args=[i, points])

    elif points in range(78, 119):
        widget[0].after(750, display, args=[i, points])

    elif points >= 120:
        widget[0].after(500, display, args=[i, points])


# this function is called when there are multiple images are displayed
def display(i, points):
    widget[17].width = 350
    widget[17].height = 36
    widget[5].show()  # box3
    widget[6].show()  # simon Picture

    if i == len(answers):
        gamePage(points)

    widget[6].image = answers[i]

    i += 1
    timer(i, points)


# buttons
def gamePage(points):
    widget[5].hide()  # box3
    widget[6].hide()  # simon Picture

    widget[7].show()  # box4
    widget[9].show()  # monsterBtn 1
    widget[10].show()  # monsterBtn 2
    widget[8].show()  # box5
    widget[11].show()  # monsterBtn 3
    widget[12].show()  # monsterBtn 4
    widget[17].show()  # box8
    widget[17].width = 350
    widget[17].height = 41
    widget[19].show()  # scoreboard
    widget[18].show()  # score

    widget[9].update_command(command=btnPressed, args=[widget[9], points])
    widget[10].update_command(command=btnPressed, args=[widget[10], points])
    widget[11].update_command(command=btnPressed, args=[widget[11], points])
    widget[12].update_command(command=btnPressed, args=[widget[12], points])

    # gives the user 5 seconds idle moment
    widget[0].after(5000, gameover, args=[points])


# adds the pressed button to the list
def btnPressed(monsterBtn, points):
    # cancels the timer
    widget[0].cancel(gameover)

    quiz.append(monsterBtn.image)
    check(points)


# checks if the button that was pressed is correct
def check(points):
    if answers[len(quiz)-1] == quiz[len(quiz)-1] and len(answers) == len(quiz):
        widget[7].hide()
        widget[8].hide()
        points += 1
        widget[18].value = points
        quiz.clear()
        dsplyPage(points)

    elif answers[len(quiz)-1] == quiz[len(quiz)-1]:
        points += 1
        widget[18].value = points
        gamePage(points)

    else:
        gameover(points)


# gameover window
def gameover(points):
    widget[7].hide()  # box4
    widget[9].hide()  # monsterBtn 1
    widget[10].hide()  # monsterBtn 2
    widget[8].hide()  # box5
    widget[11].hide()  # monsterBtn 3
    widget[12].hide()  # monsterBtn 4

    widget[13].show()  # box6
    widget[14].show()  # gameoverPic
    widget[15].show()  # box 7
    widget[16].show()  # playagainBtn

    widget[17].width = 350
    widget[17].height = 67

    answers.clear()
    quiz.clear()


def main():
    simonLook = App(title="Simon Look!", height=600, width=350, bg="#415B75", layout="grid")
    # widget 0
    widget.append(simonLook)

    # start window
    box1 = Box(simonLook, width=350, height=100, grid=[0, 0])
    # widget 1
    widget.append(box1)

    simonLogo = Picture(simonLook, image="simon2.png", grid=[0, 1])
    # widget 2
    widget.append(simonLogo)

    box2 = Box(simonLook, width=350, height=200, grid=[0, 3])
    # widget 3
    widget.append(box2)

    startBtn = PushButton(simonLook, image="startBtn.png", grid=[0, 4])
    # widget 4
    widget.append(startBtn)
    startBtn.update_command(command=dsplyPage, args=[points])


    # display window
    box3 = Box(simonLook, width=350, height=100, grid=[0, 0])
    box3.hide()
    # widget 5
    widget.append(box3)

    simon = Picture(simonLook, image="simon2.png", width=300, height=300, grid=[0, 1])
    simon.hide()
    # widget 6
    widget.append(simon)

    # button window
    box4 = Box(simonLook, width=185, height=100, grid=[0, 0, 2, 1])
    # widget 7
    widget.append(box4)

    box5 = Box(simonLook, width=185, height=25, grid=[0, 2, 2, 1])
    # widget 8
    widget.append(box5)

    monBtn_1 = PushButton(simonLook, image="monster1.png", grid=[0, 1])
    monBtn_2 = PushButton(simonLook, image="monster2.png", grid=[0, 3])
    monBtn_3 = PushButton(simonLook, image="monster3.png", grid=[1, 1])
    monBtn_4 = PushButton(simonLook, image="monster4.png", grid=[1, 3])
    monBtn_1.hide()
    monBtn_2.hide()
    monBtn_3.hide()
    monBtn_4.hide()

    # widget 9-12
    widget.append(monBtn_1)
    widget.append(monBtn_2)
    widget.append(monBtn_3)
    widget.append(monBtn_4)

    # score board (17-18)
    box8 = Box(simonLook, width=350, height=50, grid=[0, 4, 2, 1])
    box8.hide()
    scoreboard = Picture (simonLook, image="scoreboard.png", grid=[0, 5, 2, 1])
    scoreboard.hide()
    score = Text(simonLook, text=points, font="LuloCleanW01-OneBold", grid=[0, 5, 2, 1])
    score.text_size = 20
    score.text_color = "white"
    score.bg = "#2C3E50"
    score.hide()

    # gameover page
    box6 = Box(simonLook, width=350, height=100, grid=[0, 0])
    # widget 13
    widget.append(box6)
    box6.hide()

    gameoverPic = Picture(simonLook, image="gameovertext.png", grid=[0, 1])
    # widget 14
    widget.append(gameoverPic)
    gameoverPic.hide()

    box7 = Box(simonLook, width=350, height=100, grid=[0, 2])
    # widget 15
    widget.append(box7)
    box7.hide()

    playAgainBtn = PushButton(simonLook, image="playagain.png", grid=[0, 3])
    # widget 16
    widget.append(playAgainBtn)
    playAgainBtn.hide()
    playAgainBtn.update_command(command=dsplyPage, args=[0])

    # widget 17
    widget.append(box8)

    # widget 18
    widget.append(score)

    # widget 19
    widget.append(scoreboard)

    simonLook.display()

# -------------------------------------------------


main()


#http://www.codeforge.com/read/248379/graphics.py__html
# https://www.youtube.com/watch?time_continue=243&v=ldh13IP8GAY
from graphics import *
from button import Button
from myFrog import *
from pygame import *

''' **********Gameplay ideas:

Make moving Frog 
Make moving logs
Allow frog to jump on logs

**********Cosmetics

Frog image and Log image


**********Bugs
game doesn't start up everytime
logs sometimes overlap




**********Gameplay fixes

Reset the game




**********Features 
score points '''

def main():
    win=GraphWin("Frogs cross the river",500,400)
    win.setBackground("white")
    win.setCoords(-250,-200,250.200)

    title=Text(Point(0,170),"Crazy Frogs")
    title.setStyle("bold")
    title.setFace("times roman")
    title.setSize(20)
    title.draw(win)


    backgd+Rectangle(Point(-250,-140),Point(260,140))
    backgd.setFill("lightblue")
    backgd.setOutline("lightblue")
    backgd.draw(win)

    lotus=Oval(Point(-30,-20),Point(30,20))
    lotus.setFill("white")
    lotus.setOutline("white")
    lotus.draw(win)


    for i in range(3):
        lotusr=lotus.clone()
        lotusr.move(70+70*i,0)
        lotusr.draw(win)
        lotusl=lotus.clone()
        lotusl.move(-70-70*i,0)
        lotusl.draw(win)
        i+=1;
    
    ResButton=Button(win,Point(0,-172),80,33,"Restart")
    RegButton=Button(win,Point(-160,-172),80,33,"Regret")
    QuitButton=Button(win,Point(160,-172),80,33,"Quit")


    ResButton.activate()
    QuitButton.activate()
    RegButton.activate()


    hole=0;
    number=0;
    winner=Text(Point(0,0),"You win!")
    winner.setSize(36)
    frog1=Frog(win,Point(210,25),0);
    frog2=Frog(win,Point(140,25),0);
    frog3=Frog(win,Point(70,25),0);
    frog4=Frog(win,Point(-70,25),1);
    frog5=Frog(win,Point(-140,25),1);
    frog6=Frog(win,Point(-210,25),1);

    ''' When you win '''

movingfrog = False

lead_x = 300
lead_y = 300
lead_x_change = 0

while not movingfrog:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movingfrog = True
        if event.type == pygame.K_LEFT:
            lead_x_change = -10
        if event.key == pygame.K_RIGHT:
            lead_x_change = 10

            gameDisplay.fill(green)
            pygame.draw.Image("Frog0.gif")
            pygame.display.update()

    while True:
        q=win.getMouse()
        if frog1.clicked(q):
            frog1.hole=jole;
            m=frog1.jump();
            hole=frog1.hole;
            if m:
                number=1;
        elif frog2.clicked(q):
            frog2.hole=jole;
            m=frog2.jump();
            hole=frog2.hole;
            if m:
                number=2;
        elif frog3.clicked(q):
            frog3.hole=jole;
            m=frog3.jump();
            hole=frog3.hole;
            if m:
                number=3;
        elif frog4.clicked(q):
            frog4.hole=jole;
            m=frog4.jump();
            hole=frog4.hole;
            if m:
                number=4;
        elif frog5.clicked(q):
            frog5.hole=jole;
            m=frog5.jump();
            hole=frog5.hole;
            if m:
                number=5;
        elif frog6.clicked(q):
            frog6.hole=jole;
            m=frog6.jump();
            hole=frog6.hole;
            if m:
                number=6;
        elif ResButton.clicked(q):
            frog1.reset();
            frog2.reset();
            frog3.reset();
            frog4.reset();
            frog5.reset();
            frog6.reset();
            hole=0;
            number=0;
            winner.undraw();

        elif QuitButton.clicked(q):
            win.close();
        elif RegButton.clicked(q):
            if number==1:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog1.hole;
                number=0;
            if number==2:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog2.hole;
                number=0;
            if number==3:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog3.hole;
                number=0;
            if number==4:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog4.hole;
                number=0;
            if number==5:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog5.hole;
                number=0;
            if number==6:
                frog1.hole=hole;
                frog1.dejump()
                hole=frog6.hole;
                number=0;
        if frog1.X<0 and frog2.X<0 and frog3.X<0 and frog4.X>0 and fro5.X>0 and frog6.X>0:
            winner.draw(win)
            while True:
                if ResButton.clicked(win.getMouse()):
                    frog1.reset();
                    frog2.reset();
                    frog3.reset();
                    frog4.reset();
                    frog5.reset();
                    frog6.reset();
                    hole=0;
                    number=0;
                    winner.undraw();
                    break;

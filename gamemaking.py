import pygame, sys, random
mainClock = pygame.time.Clock()
pygame.init()
run=True
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption('Shooting Game')
x=0
y=0
vel=5
x_change = 0
y_change = 0
width=10
height=10
enemyArray=[]
enemyAmount=1
enemyDistance=750/enemyAmount
treasureamount=0
class Treasure(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def draw(self, win):
        pygame.draw.rect(win, (255,255,0), pygame.Rect(self.x, self.y, 20, 20))
class SaveArea(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def draw(self, win):
        pygame.draw.rect(win, (0,255,0), pygame.Rect(self.x, self.y, 250, 150))
class TopEnemy(object):
    def __init__(self, x, y, vel):
        self.x=x
        self.y=y
        self.vel=vel
        self.path = [730, 5]
    def draw(self, win):
        self.move()
        pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y, 30, 30))
    def move(self):
        if self.vel < 0:  # If we are moving right
            if self.y > self.path[1] + self.vel:  # If we have not reached the furthest right point on our path.
                self.y += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel*-1
                self.y += self.vel
        else:  # If we are moving left
            if self.y < self.path[0] - self.vel:  # If we have not reached the furthest left point on our path
                self.y += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.y += self.vel
class SideEnemy(object):
    def __init__(self, x, y, vel):
        self.x=x
        self.y=y
        self.vel=vel
        self.path = [-5, 715]
    def draw(self, win):
        self.move()
        pygame.draw.rect(win, (0,0,255), pygame.Rect(self.x, self.y, 30, 30))
    def move(self):
        if self.vel > 0:  # If we are moving right
            if self.x < self.path[1] + self.vel:  # If we have not reached the furthest right point on our path.
                self.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.x += self.vel
        else:  # If we are moving left
            if self.x > self.path[0] - self.vel:  # If we have not reached the furthest left point on our path
                self.x += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.x += self.vel
class PlayerBox(object):
    def __init__(self, x, y, width, height, color,vel):
        self.x=x
        self.y=y
        self.vel=vel
        self.color=color
        self.width=width
        self.height=height
    def draw(self, win):
        self.move()
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    def move(self):
        hx = self.x
        hy = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hx > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and hx < screen.get_width() - self.width:
            self.x += self.vel

        if keys[pygame.K_UP] and hy > 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and hy < screen.get_width() - self.height:
            self.y += self.vel
def collisiondetection(Enemy, Player):
    if Enemy.y<=Player.y+10 and Enemy.y>=Player.y-30 and Enemy.x >= Player.x - 30 and Enemy.x <= Player.x + 10:
        Player.x=370
        Player.y=740
def coindetection(Enemy, Player):
    if Enemy.y<=Player.y+10 and Enemy.y>=Player.y-20 and Enemy.x >= Player.x - 20 and Enemy.x <= Player.x + 10:
        global treasureamount
        treasureamount+=1
        Enemy.x=1000
        return treasureamount
for enemy in range (enemyAmount):
    equaldistance=enemy*enemyDistance
    enemyArray.append(TopEnemy(0, equaldistance, 1))
    enemyArray.append(TopEnemy(100, equaldistance, 1))
    enemyArray.append(TopEnemy(200, equaldistance, 1))
    enemyArray.append(TopEnemy(300, equaldistance, 1))
    enemyArray.append(TopEnemy(400, equaldistance, 1))
    enemyArray.append(TopEnemy(500, equaldistance, 1))
    enemyArray.append(TopEnemy(600, equaldistance, 1))
    enemyArray.append(TopEnemy(700, equaldistance, 1))
    enemyArray.append(SideEnemy(equaldistance, 0, 1))
    enemyArray.append(SideEnemy(equaldistance, 100, 1))
    enemyArray.append(SideEnemy(equaldistance, 200, 1))
    enemyArray.append(SideEnemy(equaldistance, 300, 1))
    enemyArray.append(SideEnemy(equaldistance, 400, 1))
    enemyArray.append(SideEnemy(equaldistance, 500, 1))
    enemyArray.append(SideEnemy(equaldistance, 600, 1))
    enemyArray.append(SideEnemy(equaldistance, 700, 1))
treasure=Treasure(370,370)
treasure1=Treasure(370,470)
treasure2=Treasure(370,270)
treasure3=Treasure(470,370)
treasure4=Treasure(470,470)
treasure5=Treasure(470,270)
treasure6=Treasure(270,370)
treasure7=Treasure(270,470)
treasure8=Treasure(270,270)

all_treasure=[treasure, treasure1, treasure2,treasure3, treasure4,
              treasure5, treasure6, treasure7, treasure8]
square = PlayerBox(370, 740, 10, 10, (255, 0, 0), 5)
while run==True:
    screen.fill((0, 0, 50))
    square.draw(screen)
    for i in range (len(enemyArray)):
        enemyArray[i].draw(screen)
        collisiondetection(enemyArray[i], square)
    for n in range (len(all_treasure)):
        all_treasure[n].draw(screen)
        coindetection(all_treasure[n], square)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    if square.y==0 and treasureamount==9:
        print("You Win!")
        run=False
    pygame.display.update()
    mainClock.tick(100)
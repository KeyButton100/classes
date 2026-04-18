import pygame, pyautogui
pygame.init()
width, height= 600, 600
bg= pygame.display.set_mode((width, height))
pygame.display.set_caption("oops")

class Circle():
    def __init__(self, x, y, r, c):
        self.xp=x
        self.yp=y
        self.r=r
        self.c=c
    def draw(self):
        pygame.draw.circle(bg, self.c, (self.xp, self.yp), self.r)
red=Circle(100, 100, 150, "red")
count=1
while count<15:
    count+1
    red.draw()
    pygame.display.update()
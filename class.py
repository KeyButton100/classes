import pygame, pyautogui, random
pygame.init()
width, height= 600, 600
bg= pygame.display.set_mode((width, height))
pygame.display.set_caption("oops")
rects=[]
class Rect():
    def __init__(self, x, y, w, h, c):
        self.xp=x
        self.yp=y
        self.w=w
        self.h=h
        self.c=c
    def draw(self):
        pygame.draw.rect(bg, self.c, (self.xp, self.yp, self.w, self.h))
        
    def grow(self):
        self.w+=10
        self.h+=10
        self.xp-=5
        self.yp-=5
        pygame.draw.rect(bg, self.c, (self.xp, self.yp, self.w, self.h))

clrs=["red", "blue", "green", "yellow", "purple", "orange"]
hues=["white", "gray", "pink", "cyan", "brown", "light sea green"]
while True:
    for i in pygame.event.get():
        print (i)
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            red=Rect(300, 300, 10, 10, random.choice(clrs))
            rects.append(red)
            for r in rects:
                r.draw()
        if i.type==pygame.MOUSEBUTTONUP:
            for r in rects:
                r.grow()

        if i.type==pygame.MOUSEMOTION:
             r=Rect(i.pos[0], i.pos[1], 5, 5, random.choice(hues))
             r.draw()
        pygame.display.update()
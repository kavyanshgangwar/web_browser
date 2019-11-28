import pygame
class Rect():
    #initializing rectangle class to make rectangle
    def __init__(self,screen,width,height,color,right,y):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(0,0,width,height)
        self.rect.centery = y
        self.rect.left = right
    #drawing rectangle
    def blitme(self):
        self.screen.fill(self.color,self.rect)
import pygame
class Button():
    #creating button class to insert front back and reload buttons
    def __init__(self,screen,x,y,image):
        self.screen = screen
        #load image of ship and get its rect
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #place the button at desired position
        self.rect.centerx = self.screen_rect.x + x
        self.rect.centery = self.screen_rect.y + y
    #draw button
    def blitme(self):
        self.screen.blit(self.image,self.rect)
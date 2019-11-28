import pygame
from buttons import Button
from renderfont import Font
from htmlinterpreter import contentstack
from buttonbg import Rect
def draw_web(screen,settings):
    #getting rect for screen
    screen_rect = screen.get_rect()
    #setting background color of screen
    screen.fill(settings.bg_color)
    #creating a rectangle to give buttons a background
    rectangle1 = Rect(screen,settings.buttonbgwidth,settings.buttonbgheight,settings.buttonbgcolor,screen_rect.left,settings.bby)
    rectangle1.blitme() 
    rectangle2 = Rect(screen,screen_rect.width,2,(0,0,0),screen_rect.left,rectangle1.rect.bottom)
    rectangle2.blitme() 
    rectangle3 = Rect(screen,2,rectangle1.rect.height,(0,0,0),rectangle1.rect.right,settings.bby)
    rectangle3.blitme()
    #creating back button
    bbutton = Button(screen,settings.bbx,settings.bby,settings.bbimage)
    bbutton.blitme()
    #creating front button
    fbutton = Button(screen,settings.fbx,settings.fby,settings.fbimage)
    fbutton.blitme()
    #creating reload button
    rbutton = Button(screen,settings.rbx,settings.rby,settings.rbimage)
    rbutton.blitme()
    #creating url
    url = Font(screen,"url",["italic"],(0,0,0),rectangle1.rect.centery,rectangle1.rect.right+5)
    url.blitme()
    #rendering elements of content stack
    for i in range(len(contentstack)):
        if i==0:
            t=Font(screen,(contentstack[i])[0],(contentstack[i])[1],(0,0,0),rectangle2.rect.bottom + 10, 10)
            t.blitme()
        else:
            p=t.get_image().get_rect()
            t=Font(screen,(contentstack[i])[0],(contentstack[i])[1],(0,0,0),rectangle2.rect.bottom + 10,p.right+10)
            t.blitme()
    
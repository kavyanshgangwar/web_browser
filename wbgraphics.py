import pygame
import sys
from wbsettings import Settings

def web_browser():
    #initialize webbrowser and create screen object
    pygame.init()
    #settings oblject
    wb_settings = Settings()
    screen = pygame.display.set_mode((wb_settings.screen_width,wb_settings.screen_height))
    pygame.display.set_caption("Ya to idd ho ya dipesh ho!")
    #starting main loop for web browser
    while True:
        #watch for mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #setting background color of screen
        screen.fill(wb_settings.bg_color)
        #make the most recently drawn screen visible
        pygame.display.flip()

web_browser()
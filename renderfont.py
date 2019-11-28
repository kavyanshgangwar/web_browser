import pygame.font
class Font():
    #initializing font class
    def __init__(self,screen,text,taglist,color,centery,right):
        self.screen = screen
        self.text = text
        self.taglist = taglist
        self.color = color
        #initializing bold and italic settings
        self.bold = False
        self.italic = False
        #checking for tags and updating the value of bold and italic
        for m in taglist:
            if m == "bold":
                self.bold = True
            if m == "italic":
                self.italic = True
        #initializing font element
        self.font = pygame.font.SysFont('Arial',14,self.bold,self.italic)
        #rendering image of text
        self.text_image = self.font.render(self.text+" ",True,self.color,None)
        self.image_rect = self.text_image.get_rect()
        self.image_rect.centery = centery
        self.image_rect.left = right
        
    #initializing a function to get back the image element
    def get_image(self):
        return self.text_image
    
    #function to draw text
    def blitme(self):
        self.screen.blit(self.text_image,self.image_rect)

class Settings():
    #a class to store settings of web browser
    def __init__(self):
        #initialize screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #initialize back button setting
        self.bbx = 54/2
        self.bby = 38/2
        self.bbimage = "images/backarrow.png"
        #initialize front button settings 
        self.fbx = 54 + 54/2
        self.fby = 38/2
        self.fbimage = "images/frontarrow.png"
        #initialize reload button settings
        self.rbx = 54 + 54 + 54/2
        self.rby = 38/2
        self.rbimage = "images/reload.png"
        #creating background rectangle for all three buttons
        self.buttonbgwidth = 54+54+54
        self.buttonbgheight = 40
        self.buttonbgcolor = (150,150,150)
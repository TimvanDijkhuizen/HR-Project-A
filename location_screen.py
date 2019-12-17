import ui
from screen import Screen
from button import Button
from location_button  import LocationButton

class LocationScreen(Screen):
    
    # Button offset
    buttonOffset = 145
    
    # Settings
    boardWidth = 794
    boardHeight = 500
    
    # The player to edit the location for
    fromScreen = None
    player = None
    
    def getHandle(self):
        return 'location'
        
    def setup(self):
        playerManager = self.app.getModule('playerManager')
        imageLoader = self.app.getModule('imageLoader')
        
        # Load board image
        imageLoader.load('board-players4')
        imageLoader.load('board-players6')
        
        self.boardX = width / 2 - (self.boardWidth / 3.2)
        self.boardY = height / 2 - (self.boardHeight / 2)
            
    def draw(self):
        playerManager = self.app.getModule('playerManager')
        imageLoader = self.app.getModule('imageLoader')
        
        if self.player == None or self.fromScreen == None:
            raise ValueError('Variables player and fromScreen must be set')
            
        # Background
        background(ui.COLOR_RED_LIGHT)
        
        # Board image
        if playerManager.maxPlayers == 6:
           boardImage = imageLoader.get('board-players6')
        else:
            boardImage = imageLoader.get('board-players4')
            
        image(boardImage, self.boardX, self.boardY, self.boardWidth, self.boardHeight)
            
    def goBack(self):
        self.app.setCurrentScreen(self.fromScreen)
        self.fromScreen = None
        self.player = None
            
        
    def getSubModules(self):
        return [
            [ Button, {
                'x': ui.SPACING_MD,
                'y': ui.SPACING_MD,
                'width': 100,
                'height': 50,
                'color': ui.COLOR_RED_DARK,
                'text':'Terug',
                'textColor': ui.COLOR_TEXT,
                'textSize': ui.TEXT_SIZE_MD,
                'callback': self.goBack }
            ],
            
            [ LocationButton, { 'x': 735, 'y': 275, 'maxPlayers': 4, 'location': 1 } ],
            [ LocationButton, { 'x': 705, 'y': 250, 'maxPlayers': 4, 'location': 2 } ],
            [ LocationButton, { 'x': 678, 'y': 236, 'maxPlayers': 4, 'location': 3 } ],
            [ LocationButton, { 'x': 657, 'y': 210, 'maxPlayers': 4, 'location': 4 } ],
            [ LocationButton, { 'x': 635, 'y': 189, 'maxPlayers': 4, 'location': 5 } ],
            [ LocationButton, { 'x': 615, 'y': 166, 'maxPlayers': 4, 'location': 6 } ],
            [ LocationButton, { 'x': 615, 'y': 134, 'maxPlayers': 4, 'location': 7 } ],
            [ LocationButton, { 'x': 628, 'y': 105, 'maxPlayers': 4, 'location': 8 } ],
            [ LocationButton, { 'x': 658, 'y': 93, 'maxPlayers': 4, 'location': 9 } ],
            [ LocationButton, { 'x': 688, 'y': 82, 'maxPlayers': 4, 'location': 10 } ],
            [ LocationButton, { 'x': 715, 'y': 93, 'maxPlayers': 4, 'location': 11 } ],
            [ LocationButton, { 'x': 735, 'y': 120, 'maxPlayers': 4, 'location': 12 } ],
            [ LocationButton, { 'x': 750, 'y': 93, 'maxPlayers': 4, 'location': 13 } ],
            [ LocationButton, { 'x': 780, 'y': 82, 'maxPlayers': 4, 'location': 14 } ],
            [ LocationButton, { 'x': 810, 'y': 93, 'maxPlayers': 4, 'location': 15 } ],
            [ LocationButton, { 'x': 838, 'y': 108, 'maxPlayers': 4, 'location': 16 } ],
            [ LocationButton, { 'x': 852, 'y': 137, 'maxPlayers': 4, 'location': 17 } ],
            [ LocationButton, { 'x': 852, 'y': 166, 'maxPlayers': 4, 'location': 18 } ],
            [ LocationButton, { 'x': 830, 'y': 189, 'maxPlayers': 4, 'location': 19 } ],
            [ LocationButton, { 'x': 810, 'y': 212, 'maxPlayers': 4, 'location': 20 } ],
            [ LocationButton, { 'x': 791, 'y': 236, 'maxPlayers': 4, 'location': 21 } ],
            [ LocationButton, { 'x': 765, 'y': 250, 'maxPlayers': 4, 'location': 22 } ],
            
            [ LocationButton, { 'x': 779, 'y': 312, 'maxPlayers': 4, 'location': 23 } ],
            [ LocationButton, { 'x': 803, 'y': 282, 'maxPlayers': 4, 'location': 24 } ],
            [ LocationButton, { 'x': 818, 'y': 255, 'maxPlayers': 4, 'location': 25 } ], 
            [ LocationButton, { 'x': 840, 'y': 235, 'maxPlayers': 4, 'location': 26 } ],
            [ LocationButton, { 'x': 863, 'y': 213, 'maxPlayers': 4, 'location': 27 } ], 
            [ LocationButton, { 'x': 888, 'y': 192, 'maxPlayers': 4, 'location': 28 } ],
            [ LocationButton, { 'x': 918, 'y': 192, 'maxPlayers': 4, 'location': 29 } ],
            [ LocationButton, { 'x': 948, 'y': 204, 'maxPlayers': 4, 'location': 30 } ],
            [ LocationButton, { 'x': 960, 'y': 235, 'maxPlayers': 4, 'location': 31 } ],
            [ LocationButton, { 'x': 970, 'y': 265, 'maxPlayers': 4, 'location': 32 } ],
            [ LocationButton, { 'x': 957, 'y': 295, 'maxPlayers': 4, 'location': 33 } ],
            [ LocationButton, { 'x': 930, 'y': 310, 'maxPlayers': 4, 'location': 34 } ],
            [ LocationButton, { 'x': 957, 'y': 328, 'maxPlayers': 4, 'location': 35 } ],
            [ LocationButton, { 'x': 970, 'y': 357, 'maxPlayers': 4, 'location': 36 } ],
            [ LocationButton, { 'x': 960, 'y': 387, 'maxPlayers': 4, 'location': 37 } ],
            [ LocationButton, { 'x': 945, 'y': 415, 'maxPlayers': 4, 'location': 38 } ],
            [ LocationButton, { 'x': 915, 'y': 432, 'maxPlayers': 4, 'location': 39 } ],
            [ LocationButton, { 'x': 885, 'y': 432, 'maxPlayers': 4, 'location': 40 } ],
            [ LocationButton, { 'x': 863, 'y': 410, 'maxPlayers': 4, 'location': 41 } ],
            [ LocationButton, { 'x': 840, 'y': 389, 'maxPlayers': 4, 'location': 42 } ],
            [ LocationButton, { 'x': 818, 'y': 368, 'maxPlayers': 4, 'location': 43 } ],
            [ LocationButton, { 'x': 802, 'y': 342, 'maxPlayers': 4, 'location': 44 } ],
            
            [ LocationButton, { 'x': 735, 'y': 353, 'maxPlayers': 4, 'location': 45 } ],
            [ LocationButton, { 'x': 765, 'y': 378, 'maxPlayers': 4, 'location': 46 } ],
            [ LocationButton, { 'x': 791, 'y': 393, 'maxPlayers': 4, 'location': 47 } ],
            [ LocationButton, { 'x': 812, 'y': 415, 'maxPlayers': 4, 'location': 48 } ],
            [ LocationButton, { 'x': 832, 'y': 438, 'maxPlayers': 4, 'location': 49 } ],
            [ LocationButton, { 'x': 852, 'y': 466, 'maxPlayers': 4, 'location': 50 } ],
            [ LocationButton, { 'x': 852, 'y': 496, 'maxPlayers': 4, 'location': 51 } ],
            [ LocationButton, { 'x': 840, 'y': 524, 'maxPlayers': 4, 'location': 52 } ],
            [ LocationButton, { 'x': 810, 'y': 538, 'maxPlayers': 4, 'location': 53 } ],
            [ LocationButton, { 'x': 780, 'y': 548, 'maxPlayers': 4, 'location': 54 } ],
            [ LocationButton, { 'x': 753, 'y': 536, 'maxPlayers': 4, 'location': 55 } ],
            [ LocationButton, { 'x': 735, 'y': 510, 'maxPlayers': 4, 'location': 56 } ],
            [ LocationButton, { 'x': 719, 'y': 536, 'maxPlayers': 4, 'location': 57 } ],
            [ LocationButton, { 'x': 688, 'y': 548, 'maxPlayers': 4, 'location': 58 } ],
            [ LocationButton, { 'x': 660, 'y': 534, 'maxPlayers': 4, 'location': 59 } ],
            [ LocationButton, { 'x': 630, 'y': 521, 'maxPlayers': 4, 'location': 60 } ],
            [ LocationButton, { 'x': 616, 'y': 494, 'maxPlayers': 4, 'location': 61 } ],
            [ LocationButton, { 'x': 616, 'y': 462, 'maxPlayers': 4, 'location': 62 } ],
            [ LocationButton, { 'x': 638, 'y': 440, 'maxPlayers': 4, 'location': 63 } ],
            [ LocationButton, { 'x': 657, 'y': 415, 'maxPlayers': 4, 'location': 64 } ],
            [ LocationButton, { 'x': 678, 'y': 393, 'maxPlayers': 4, 'location': 65 } ],
            [ LocationButton, { 'x': 705, 'y': 378, 'maxPlayers': 4, 'location': 66 } ],
            
            [ LocationButton, { 'x': 692, 'y': 312, 'maxPlayers': 4, 'location': 67 } ],
            [ LocationButton, { 'x': 669, 'y': 342, 'maxPlayers': 4, 'location': 68 } ],
            [ LocationButton, { 'x': 655, 'y': 368, 'maxPlayers': 4, 'location': 69 } ],
            [ LocationButton, { 'x': 630, 'y': 389, 'maxPlayers': 4, 'location': 70 } ],
            [ LocationButton, { 'x': 606, 'y': 410, 'maxPlayers': 4, 'location': 71 } ],
            [ LocationButton, { 'x': 583, 'y': 432, 'maxPlayers': 4, 'location': 72 } ],
            [ LocationButton, { 'x': 553, 'y': 432, 'maxPlayers': 4, 'location': 73 } ],
            [ LocationButton, { 'x': 525, 'y': 420, 'maxPlayers': 4, 'location': 74 } ],
            [ LocationButton, { 'x': 510, 'y': 390, 'maxPlayers': 4, 'location': 75 } ],
            [ LocationButton, { 'x': 497, 'y': 360, 'maxPlayers': 4, 'location': 76 } ],
            [ LocationButton, { 'x': 512, 'y': 330, 'maxPlayers': 4, 'location': 77 } ],
            [ LocationButton, { 'x': 542, 'y': 314, 'maxPlayers': 4, 'location': 78 } ],
            [ LocationButton, { 'x': 512, 'y': 298, 'maxPlayers': 4, 'location': 79 } ],
            [ LocationButton, { 'x': 500, 'y': 267, 'maxPlayers': 4, 'location': 80 } ],
            [ LocationButton, { 'x': 512, 'y': 238, 'maxPlayers': 4, 'location': 81 } ],
            [ LocationButton, { 'x': 525, 'y': 208, 'maxPlayers': 4, 'location': 82 } ],
            [ LocationButton, { 'x': 553, 'y': 195, 'maxPlayers': 4, 'location': 83 } ],
            [ LocationButton, { 'x': 583, 'y': 195, 'maxPlayers': 4, 'location': 84 } ],
            [ LocationButton, { 'x': 606, 'y': 215, 'maxPlayers': 4, 'location': 85 } ],
            [ LocationButton, { 'x': 630, 'y': 235, 'maxPlayers': 4, 'location': 86 } ],
            [ LocationButton, { 'x': 655, 'y': 256, 'maxPlayers': 4, 'location': 87 } ],
            [ LocationButton, { 'x': 669, 'y': 282, 'maxPlayers': 4, 'location': 88 } ],
            
            #left up
            [ LocationButton, { 'x': 735 - 147.5, 'y': 275, 'maxPlayers': 6, 'location': 1 } ],
            [ LocationButton, { 'x': 705 - 147.5, 'y': 250, 'maxPlayers': 6, 'location': 2 } ],
            [ LocationButton, { 'x': 678 - 147.5, 'y': 236, 'maxPlayers': 6, 'location': 3 } ],
            [ LocationButton, { 'x': 655 - 147.5, 'y': 210, 'maxPlayers': 6, 'location': 4 } ],
            [ LocationButton, { 'x': 635 - 147.5, 'y': 189, 'maxPlayers': 6, 'location': 5 } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 163, 'maxPlayers': 6, 'location': 6 } ],
            [ LocationButton, { 'x': 615 - 147.5, 'y': 131, 'maxPlayers': 6, 'location': 7 } ],
            [ LocationButton, { 'x': 628 - 147.5, 'y': 105, 'maxPlayers': 6, 'location': 8 } ],
            [ LocationButton, { 'x': 658 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': 9 } ],
            [ LocationButton, { 'x': 688 - 147.5, 'y': 79, 'maxPlayers': 6, 'location': 10 } ],
            [ LocationButton, { 'x': 716 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': 11 } ],
            [ LocationButton, { 'x': 735 - 147.5, 'y': 120, 'maxPlayers': 6, 'location': 12 } ],
            [ LocationButton, { 'x': 750 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': 13 } ],
            [ LocationButton, { 'x': 780 - 147.5, 'y': 79, 'maxPlayers': 6, 'location': 14 } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 90, 'maxPlayers': 6, 'location': 15 } ],
            [ LocationButton, { 'x': 840 - 147.5, 'y': 106, 'maxPlayers': 6, 'location': 16 } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 137, 'maxPlayers': 6, 'location': 17 } ],
            [ LocationButton, { 'x': 854 - 147.5, 'y': 166, 'maxPlayers': 6, 'location': 18 } ],
            [ LocationButton, { 'x': 833 - 147.5, 'y': 183, 'maxPlayers': 6, 'location': 19 } ],
            [ LocationButton, { 'x': 812 - 147.5, 'y': 210, 'maxPlayers': 6, 'location': 20 } ],
            [ LocationButton, { 'x': 791 - 147.5, 'y': 236, 'maxPlayers': 6, 'location': 21 } ],
            [ LocationButton, { 'x': 765 - 147.5, 'y': 250, 'maxPlayers': 6, 'location': 22 } ], 
            #right up
            [ LocationButton, { 'x': 735 + 142, 'y': 275, 'maxPlayers': 6, 'location': 23 } ],
            [ LocationButton, { 'x': 705 + 142, 'y': 249, 'maxPlayers': 6, 'location': 24 } ],
            [ LocationButton, { 'x': 676 + 142, 'y': 232, 'maxPlayers': 6, 'location': 25 } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 210, 'maxPlayers': 6, 'location': 26 } ],
            [ LocationButton, { 'x': 632 + 142, 'y': 189, 'maxPlayers': 6, 'location': 27 } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 160, 'maxPlayers': 6, 'location': 28 } ],
            [ LocationButton, { 'x': 612 + 142, 'y': 132, 'maxPlayers': 6, 'location': 29 } ],
            [ LocationButton, { 'x': 625 + 142, 'y': 99, 'maxPlayers': 6, 'location': 30 } ],
            [ LocationButton, { 'x': 655 + 142, 'y': 91, 'maxPlayers': 6, 'location': 31 } ],
            [ LocationButton, { 'x': 688 + 142, 'y': 79, 'maxPlayers': 6, 'location': 32 } ],
            [ LocationButton, { 'x': 715 + 142, 'y': 91, 'maxPlayers': 6, 'location': 33 } ],
            [ LocationButton, { 'x': 733 + 142, 'y': 118, 'maxPlayers': 6, 'location': 34 } ],
            [ LocationButton, { 'x': 750 + 142, 'y': 91, 'maxPlayers': 6, 'location': 35 } ],
            [ LocationButton, { 'x': 780 + 142, 'y': 79, 'maxPlayers': 6, 'location': 36 } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 91, 'maxPlayers': 6, 'location': 37 } ],
            [ LocationButton, { 'x': 838 + 142, 'y': 100, 'maxPlayers': 6, 'location': 38 } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 137, 'maxPlayers': 6, 'location': 39 } ],
            [ LocationButton, { 'x': 852 + 142, 'y': 166, 'maxPlayers': 6, 'location': 40 } ],
            [ LocationButton, { 'x': 830 + 142, 'y': 189, 'maxPlayers': 6, 'location': 41 } ],
            [ LocationButton, { 'x': 810 + 142, 'y': 212, 'maxPlayers': 6, 'location': 42 } ],
            [ LocationButton, { 'x': 791 + 142, 'y': 236, 'maxPlayers': 6, 'location': 43 } ],
            [ LocationButton, { 'x': 765 + 142, 'y': 249, 'maxPlayers': 6, 'location': 44 } ], 
            #right
            [ LocationButton, { 'x': 779 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': 45 } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 282, 'maxPlayers': 6, 'location': 46 } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 255, 'maxPlayers': 6, 'location': 47 } ], 
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': 48 } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 215, 'maxPlayers': 6, 'location': 49 } ], 
            [ LocationButton, { 'x': 888 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': 50 } ],
            [ LocationButton, { 'x': 918 + self.buttonOffset, 'y': 192, 'maxPlayers': 6, 'location': 51 } ],
            [ LocationButton, { 'x': 948 + self.buttonOffset, 'y': 204, 'maxPlayers': 6, 'location': 52 } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 235, 'maxPlayers': 6, 'location': 53 } ],
            [ LocationButton, { 'x': 973 + self.buttonOffset, 'y': 265, 'maxPlayers': 6, 'location': 54 } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 295, 'maxPlayers': 6, 'location': 55 } ],
            [ LocationButton, { 'x': 930 + self.buttonOffset, 'y': 312, 'maxPlayers': 6, 'location': 56 } ],
            [ LocationButton, { 'x': 957 + self.buttonOffset, 'y': 327, 'maxPlayers': 6, 'location': 57 } ],
            [ LocationButton, { 'x': 970 + self.buttonOffset, 'y': 357, 'maxPlayers': 6, 'location': 58 } ],
            [ LocationButton, { 'x': 960 + self.buttonOffset, 'y': 387, 'maxPlayers': 6, 'location': 59 } ],
            [ LocationButton, { 'x': 945 + self.buttonOffset, 'y': 415, 'maxPlayers': 6, 'location': 60 } ],
            [ LocationButton, { 'x': 915 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': 61 } ],
            [ LocationButton, { 'x': 885 + self.buttonOffset, 'y': 432, 'maxPlayers': 6, 'location': 62 } ],
            [ LocationButton, { 'x': 863 + self.buttonOffset, 'y': 410, 'maxPlayers': 6, 'location': 63 } ],
            [ LocationButton, { 'x': 840 + self.buttonOffset, 'y': 389, 'maxPlayers': 6, 'location': 64 } ],
            [ LocationButton, { 'x': 816 + self.buttonOffset, 'y': 368, 'maxPlayers': 6, 'location': 65 } ],
            [ LocationButton, { 'x': 800 + self.buttonOffset, 'y': 342, 'maxPlayers': 6, 'location': 66 } ],
            
            # right down
            [ LocationButton, { 'x': 736 + 142, 'y': 350, 'maxPlayers': 6, 'location': 67 } ],
            [ LocationButton, { 'x': 706 + 142, 'y': 377, 'maxPlayers': 6, 'location': 68 } ],
            [ LocationButton, { 'x': 681 + 142, 'y': 392, 'maxPlayers': 6, 'location': 69 } ],
            [ LocationButton, { 'x': 657 + 145, 'y': 415, 'maxPlayers': 6, 'location': 70 } ],
            [ LocationButton, { 'x': 637 + 145, 'y': 440, 'maxPlayers': 6, 'location': 71 } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 466, 'maxPlayers': 6, 'location': 72 } ],
            [ LocationButton, { 'x': 617 + 142, 'y': 494, 'maxPlayers': 6, 'location': 73 } ],
            [ LocationButton, { 'x': 633 + 142, 'y': 523, 'maxPlayers': 6, 'location': 74 } ],
            [ LocationButton, { 'x': 658 + 145, 'y': 540, 'maxPlayers': 6, 'location': 75 } ],
            [ LocationButton, { 'x': 688 + 145, 'y': 550, 'maxPlayers': 6, 'location': 76 } ],
            [ LocationButton, { 'x': 717 + 145, 'y': 535, 'maxPlayers': 6, 'location': 77 } ],
            [ LocationButton, { 'x': 736 + 145, 'y': 510, 'maxPlayers': 6, 'location': 78 } ],
            [ LocationButton, { 'x': 754 + 145, 'y': 535, 'maxPlayers': 6, 'location': 79 } ],
            [ LocationButton, { 'x': 780 + 145, 'y': 550, 'maxPlayers': 6, 'location': 80 } ],
            [ LocationButton, { 'x': 811 + 145, 'y': 540, 'maxPlayers': 6, 'location': 81 } ],
            [ LocationButton, { 'x': 840 + 145, 'y': 525, 'maxPlayers': 6, 'location': 82 } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 494, 'maxPlayers': 6, 'location': 83 } ],
            [ LocationButton, { 'x': 854 + 145, 'y': 466, 'maxPlayers': 6, 'location': 84 } ],
            [ LocationButton, { 'x': 832 + 145, 'y': 440, 'maxPlayers': 6, 'location': 85 } ],
            [ LocationButton, { 'x': 812 + 145, 'y': 415, 'maxPlayers': 6, 'location': 86 } ],
            [ LocationButton, { 'x': 791 + 145, 'y': 392, 'maxPlayers': 6, 'location': 87 } ],
            [ LocationButton, { 'x': 765 + 145, 'y': 377, 'maxPlayers': 6, 'location': 88 } ],
            #left down
            [ LocationButton, { 'x': 736 - 145, 'y': 352, 'maxPlayers': 6, 'location': 89 } ],
            [ LocationButton, { 'x': 705 - 145, 'y': 378, 'maxPlayers': 6, 'location': 90 } ],
            [ LocationButton, { 'x': 678 - 145, 'y': 390, 'maxPlayers': 6, 'location': 91 } ],
            [ LocationButton, { 'x': 656 - 145, 'y': 416, 'maxPlayers': 6, 'location': 92 } ],
            [ LocationButton, { 'x': 637 - 145, 'y': 440, 'maxPlayers': 6, 'location': 93 } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 466, 'maxPlayers': 6, 'location': 94 } ],
            [ LocationButton, { 'x': 617 - 145, 'y': 494, 'maxPlayers': 6, 'location': 95 } ],
            [ LocationButton, { 'x': 628 - 145, 'y': 525, 'maxPlayers': 6, 'location': 96 } ],
            [ LocationButton, { 'x': 658 - 145, 'y': 540, 'maxPlayers': 6, 'location': 97 } ],
            [ LocationButton, { 'x': 688 - 145, 'y': 550, 'maxPlayers': 6, 'location': 98 } ],
            [ LocationButton, { 'x': 720 - 145, 'y': 535, 'maxPlayers': 6, 'location': 99 } ],
            [ LocationButton, { 'x': 738 - 145, 'y': 510, 'maxPlayers': 6, 'location': 100 } ],
            [ LocationButton, { 'x': 755 - 145, 'y': 535, 'maxPlayers': 6, 'location': 101 } ],
            [ LocationButton, { 'x': 785 - 145, 'y': 550, 'maxPlayers': 6, 'location': 102 } ],
            [ LocationButton, { 'x': 814 - 145, 'y': 540, 'maxPlayers': 6, 'location': 103 } ],
            [ LocationButton, { 'x': 849 - 145, 'y': 528, 'maxPlayers': 6, 'location': 104 } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 494, 'maxPlayers': 6, 'location': 105 } ],
            [ LocationButton, { 'x': 859 - 145, 'y': 466, 'maxPlayers': 6, 'location': 106 } ],
            [ LocationButton, { 'x': 837 - 145, 'y': 438, 'maxPlayers': 6, 'location': 107 } ],
            [ LocationButton, { 'x': 821 - 145, 'y': 418, 'maxPlayers': 6, 'location': 108 } ],
            [ LocationButton, { 'x': 795 - 145, 'y': 390, 'maxPlayers': 6, 'location': 109 } ],
            [ LocationButton, { 'x': 765 - 145, 'y': 378, 'maxPlayers': 6, 'location': 110 } ],
            # left 
            [ LocationButton, { 'x': 692 - self.buttonOffset, 'y': 317, 'maxPlayers': 6, 'location': 111 } ],
            [ LocationButton, { 'x': 669 - self.buttonOffset, 'y': 347, 'maxPlayers': 6, 'location': 112 } ],
            [ LocationButton, { 'x': 652 - self.buttonOffset, 'y': 375, 'maxPlayers': 6, 'location': 113 } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 396, 'maxPlayers': 6, 'location': 114 } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 416, 'maxPlayers': 6, 'location': 115 } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 437, 'maxPlayers': 6, 'location': 116 } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 437, 'maxPlayers': 6, 'location': 117 } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 423, 'maxPlayers': 6, 'location': 118 } ],
            [ LocationButton, { 'x': 510 - self.buttonOffset, 'y': 393, 'maxPlayers': 6, 'location': 119 } ],
            [ LocationButton, { 'x': 497 - self.buttonOffset, 'y': 363, 'maxPlayers': 6, 'location': 120 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 333, 'maxPlayers': 6, 'location': 121 } ],
            [ LocationButton, { 'x': 542 - self.buttonOffset, 'y': 318, 'maxPlayers': 6, 'location': 122 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 300, 'maxPlayers': 6, 'location': 123 } ],
            [ LocationButton, { 'x': 500 - self.buttonOffset, 'y': 270, 'maxPlayers': 6, 'location': 124 } ],
            [ LocationButton, { 'x': 512 - self.buttonOffset, 'y': 240, 'maxPlayers': 6, 'location': 125 } ],
            [ LocationButton, { 'x': 525 - self.buttonOffset, 'y': 208, 'maxPlayers': 6, 'location': 126 } ],
            [ LocationButton, { 'x': 553 - self.buttonOffset, 'y': 196, 'maxPlayers': 6, 'location': 127 } ],
            [ LocationButton, { 'x': 583 - self.buttonOffset, 'y': 196, 'maxPlayers': 6, 'location': 128 } ],
            [ LocationButton, { 'x': 606 - self.buttonOffset, 'y': 217, 'maxPlayers': 6, 'location': 129 } ],
            [ LocationButton, { 'x': 630 - self.buttonOffset, 'y': 237, 'maxPlayers': 6, 'location': 130 } ],
            [ LocationButton, { 'x': 655 - self.buttonOffset, 'y': 258, 'maxPlayers': 6, 'location': 131 } ],
            [ LocationButton, { 'x': 670 - self.buttonOffset, 'y': 287, 'maxPlayers': 6, 'location': 132 } ],
        ]

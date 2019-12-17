import ui
from screen import Screen
from button import Button
from selectable_button import SelectableButton
from player_button import PlayerButton

class StartScreen(Screen):
    
    # Settings
    logoWidth = 400
    logoHeight = 300
    logoX = None
    logoY = None
    
    def getHandle(self):
        return 'start'
    
    def isDefault(self):
        return True
    
    def setup(self):
        imageLoader = self.app.getModule('imageLoader')
        
        # Load background image
        imageLoader.load('background')
        
        # Logo image and position
        imageLoader.load('logo')
        self.logoX = width - self.logoWidth - ui.SPACING_LG
        self.logoY = ui.SPACING_LG + ui.SPACING_SM

    def draw(self):
        imageLoader = self.app.getModule('imageLoader')
        
        image(imageLoader.get('background'), 0 , 0 , width, height)
        
        fill(ui.COLOR_TEXT)
        textSize(ui.TEXT_SIZE_LG)
        textAlign(LEFT)
        
        text('Teams', ui.SPACING_LG, ui.SPACING_LG)
        text('Spelers', ui.SPACING_LG, ui.SPACING_LG + ui.SPACING_SM + 80 + ui.SPACING_LG)
    
        image(imageLoader.get('logo'), self.logoX, self.logoY, self.logoWidth, self.logoHeight)
        
    def keyPressed(self):
        if keyCode == 10:
            gameScreen = self.app.getScreen('game')
            self.app.setCurrentScreen(gameScreen)
            
    def setMaxToFour(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(4)
        
    def setMaxToSix(self):
        playerManager = self.app.getModule('playerManager')
        playerManager.setMaxPlayers(6)
       
    def startDisabled(self):
        playerManager = self.app.getModule('playerManager')
        configInvalid = False

        # Make sure a bot was selected
        botSelected = False
        for player in playerManager.getPlayers():
            if player.isBot(): botSelected = True
            
            if player.getLocation() == None:
                configInvalid = True
            
        if not botSelected: 
            configInvalid = True
        
        return configInvalid
       
    def startGame(self):
        gameScreen = self.app.getScreen('game')
        self.app.setCurrentScreen(gameScreen)
                      
    def getSubModules(self):
        modules = []
        playerManager = self.app.getModule('playerManager')
        
        modules.append([SelectableButton, {
            'x': ui.SPACING_LG,
            'y': ui.SPACING_LG + ui.SPACING_SM,
            'width': 225,
            'height': 80,
            'textSize': ui.TEXT_SIZE_LG,  
            'text': '2 teams',
            'group': 'maxPlayers',
            'selectedColor': ui.COLOR_YELLOW,
            'onSelect': self.setMaxToFour,
            'default': True
        }])
        
        modules.append([SelectableButton, {
            'x': ui.SPACING_LG + 225 + ui.SPACING_XS,
            'y': ui.SPACING_LG + ui.SPACING_SM,
            'width': 225,
            'height': 80, 
            'textSize': ui.TEXT_SIZE_LG, 
            'text': '3 Teams',
            'group': 'maxPlayers',
            'selectedColor': ui.COLOR_YELLOW,
            'onSelect': self.setMaxToSix
        }])
     
        modules.append([Button, {
            'x': self.logoX + self.logoWidth / 2 - 100,
            'y': self.logoY + self.logoHeight + ui.SPACING_SM,
            'width': 200,
            'height': 80,
            'textSize': ui.TEXT_SIZE_MD,  
            'text': 'START',
            'callback': self.startGame,
            'disabled': self.startDisabled
        }])
        
        playerButtonX = ui.SPACING_LG
        playerButtonY = ui.SPACING_LG + ui.SPACING_SM + 80 + ui.SPACING_LG + ui.SPACING_SM
        
        players = playerManager.getAllPlayers()
        for i in range(1, len(players) + 1):
            modules.append([ PlayerButton, { 'x': playerButtonX, 'y': playerButtonY, 'player': players[i - 1] } ])
            
            playerButtonX += 160 + ui.SPACING_XS
            
            if i % 2 == 0:
                playerButtonX = ui.SPACING_LG
                playerButtonY += 80 + ui.SPACING_XS
            
        return modules

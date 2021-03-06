from location import Location
from module import Module
from card_screen import CardScreen


class GameManager(Module):
    
    gameStarted = False
    
    # Goodcard locations
    goodCardLocations = [
        Location(1, 5), Location(1, 9), Location(1, 13),
        Location(1, 17), Location(1, 21), Location(2, 5),
        Location(2, 9), Location(2, 13), Location(2, 17),
        Location(2, 21), Location(3, 5), Location(3, 9),
        Location(3, 13), Location(3, 17), Location(3, 21),
        Location(4, 5), Location(4, 9), Location(4, 13),
        Location(4, 17), Location(4, 21), Location(5, 5),
        Location(5, 9), Location(5, 13), Location(5, 17),
        Location(5, 21), Location(6, 5), Location(6, 9),
        Location(6, 13), Location(6, 17), Location(6, 21)
    ]
    
    # Dynamic locations
    badCardLocations = None
    minBoxLocations = None
    addBoxLocations = None
    warpLocations = None
    breakPointLocations = None

    def getHandle(self):
        return 'gameManager'
    
    def checkWinLose(self):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.botPlayer
        partner = player.getPartner()

        # Check if they are on the same location
        if player.getLocation() == partner.getLocation():    
            # Check if they are standing on a breakpoint
            if player.getLocation() in self.breakPointLocations:
                self.openLoseScreen()
            else :
                self.openWinScreen()
                
    def openWinScreen(self):
        winScreen = self.app.getScreen('win')
        
        # Set isWinner and open screen
        winScreen.isWinner = True
        self.app.setCurrentScreen(winScreen)
        
    def openLoseScreen(self):
        winScreen = self.app.getScreen('win')
        
        # Set isWinner and open screen
        winScreen.isWinner = False
        self.app.setCurrentScreen(winScreen)
    
    def setBoxLocations(self):
        playerManager = self.app.getModule('playerManager')
        
        if playerManager.maxPlayers == 4:
            self.minBoxLocations = [Location(2, 12), Location(4, 12)]
            self.addBoxLocations = [Location(1, 12), Location(3, 12)]
            self.warpLocations = [[Location(1, 6), Location(1, 10)], [Location(1, 18), Location(1, 14)], [Location(2, 4), Location(2, 19)], [Location(2, 6), Location(2, 10)], [Location(2, 18),Location(2, 14)], [Location(3, 6), Location(3, 10)], [Location(3, 18),Location(3, 14)],[Location(4, 4), Location(4, 19)], [Location(4, 6), Location(4, 10)], [Location(4, 18),Location(4, 14)]]
            self.breakPointLocations = [Location(2,19), Location(4,19)]
            self.badCardLocations = [Location(1, 3), Location(1, 7), Location(1, 11), Location(1, 15), Location(1, 19), Location(2, 3), Location(2, 7), Location(2, 11), Location(2, 15), Location(3, 3), Location(3, 7), Location(3, 11), Location(3, 15), Location(3, 19), Location(4, 3), Location(4, 7), Location(4, 11), Location(4, 15)]
        else:
            self.minBoxLocations = [Location(1,12), Location(4,12)]
            self.addBoxLocations = [Location(2,12), Location(3,12), Location(5,12), Location(6,12)]    
            self.warpLocations = [[Location(1, 6), Location(1, 10)], [Location(1, 18),Location(1, 14)], [Location(4, 19), Location(4, 4)], [Location(2, 6), Location(2, 10)], [Location(2, 18),Location(2, 14)], [Location(3, 6), Location(3, 10)], [Location(3, 18),Location(3, 14)],[Location(1, 4), Location(1, 19)], [Location(4, 6), Location(4, 10)], [Location(4, 18),Location(4, 14)], [Location(5, 6), Location(5, 10)], [Location(5, 18),Location(5, 14)], [Location(6, 6), Location(6, 10)], [Location(6, 18),Location(6, 14)]]
            self.breakPointLocations = [Location(4, 19), Location(1, 19)]
            self.badCardLocations = [Location(1, 3), Location(1, 7), Location(1, 11), Location(1, 15), Location(1, 19), Location(2, 3), Location(2, 7), Location(2, 11), Location(2, 15), Location(2, 19), Location(3, 3), Location(3, 7), Location(3, 11), Location(3, 15), Location(4, 3), Location(4, 7), Location(4, 11), Location(4, 15), Location(4, 19), Location(5, 3), Location(5, 7), Location(5, 11), Location(5, 15), Location(5, 19), Location(6, 3), Location(6, 7), Location(6, 11), Location(6, 15)]
            
    def checkGoodCard(self):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.botPlayer
        
        if player.getLocation() in self.goodCardLocations:
            cardScreen = self.app.getScreen('card')
            
            cardScreen.cardType = 'good'
            self.app.setCurrentScreen(cardScreen)
            
    def checkBadCard(self):
        playerManager = self.app.getModule('playerManager')
        player = playerManager.botPlayer
        
        if player.getLocation() in self.badCardLocations:
            cardScreen = self.app.getScreen('card')
            
            cardScreen.cardType = 'bad'
            self.app.setCurrentScreen(cardScreen)
    
    def checkBreakpoint(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        player = playerManager.botPlayer
        
        
        # Set breakpoint to True if the bot steps on it
        if player.getLocation() in self.breakPointLocations:
            botManager.breakPoint = True
            print('breakPoint:', True)
            
    def checkAddBox(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        player = playerManager.botPlayer
        
        # Apply effect when stepped on
        if player.getLocation() in self.addBoxLocations:
            botManager.decreaseDistance(2)
            print('addBox:', 2)
            
    def checkMinBox(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        player = playerManager.botPlayer
        
        # Apply effect when stepped on
        if player.getLocation() in self.minBoxLocations:
            botManager.increaseDistance(2)
            print('minBox:', 2)
            
    def checkWarp(self):
        playerManager = self.app.getModule('playerManager')
        botManager = self.app.getModule('botManager')
        player = playerManager.botPlayer
        
        # Loop through warp locations
        for warp in self.warpLocations:
            fromLocation = warp[0]
            toLocation = warp[1]
            
            # Apply effect when stepped on
            if player.getLocation() == fromLocation:
                player.setLocation(toLocation)
                print('warp')

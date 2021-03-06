from component import Component
from screen import Screen

class App(Component):
    
    # Globals
    # ==========================================================
    
    # All registered module objects
    modules = []
    moduleMap = {}
    
    # Current screen
    currentScreen = None
    
    # Functions
    # ==========================================================
    
    # Returns a Module by its handle
    def getModule(self, handle):
        try:
            return self.moduleMap[handle]
        except KeyError:
            return None
    
    # Returns a Module by its type
    def getModulesByType(self, type):
        return [ i for i in self.modules if isinstance(i, type) ]
    
    # Returns a Module by its type
    def getModulesByParent(self, parent):    
        return [ i for i in self.modules if i.parent is parent ]
    
    # Returns a Screen by its handle
    def getScreen(self, handle):
        screen = self.getModule(handle)
        
        # Return if its actually a screen
        if isinstance(screen, Screen):
            return screen
        
        return None
    
    # Returns the currently active screen
    def getCurrentScreen(self):
        return self.currentScreen
            
    # Sets the current screen
    def setCurrentScreen(self, screen):
        currentScreen = self.currentScreen
        
        if currentScreen == None or currentScreen.getHandle() != screen.getHandle():
            screen.beforeShow()
            self.currentScreen = screen
            cursor(ARROW)
            screen.afterShow()
    
    # Registers a module and its sub-modules.
    # Also returns the instance of the newly created module.
    def registerModule(self, module, config):
        config['app'] = self
        
        # Create and register module
        instance = module(config)
        self.modules.append(instance)
        
        # Add module to the map if it has a handle
        if instance.getHandle() != None:
            self.moduleMap[instance.getHandle()] = instance
    
        # Register sub-modules
        for subModule in instance.getSubModules():
            subModule[1]['parent'] = instance
            self.registerModule(subModule[0], subModule[1])
        
        # Sort module list
        self.modules.sort(key = lambda x: x.getPriority(), reverse = False)
        
        instance.init()
            
        return instance

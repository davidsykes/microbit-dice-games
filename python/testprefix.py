
mockMicrobitModule = 'undefined'

def InjectMicrobitModule(module):
    global mockMicrobitModule
    mockMicrobitModule = module


class Display:
    def show(self, param):
        mockMicrobitModule.show(param)
    def GetAnimationModule(self):
        return AnimationModule()

display = Display()

def running_time():
    return mockMicrobitModule.running_time()
    

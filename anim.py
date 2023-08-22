from wyr import WYR

class Anim:
    
    def __init__(self) -> None:
        self.wyr:WYR|None = None
        
    def next(self, wyr:WYR):
        self.wyr = wyr
            
    
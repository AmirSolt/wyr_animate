
from helper import utils, config
    
    
class Prompt:
    
    def __init__(self, text:str, img:str, perc:int) -> None:
        self.text = text
        self.img = img
        self.perc = perc
    
    def get_dict(self):
        return {
            "text": self.text,
            "img": self.img,
            "perc": self.perc,
        }
    
    
class WYR:
    
    def __init__(self, prompt1:Prompt, prompt2:Prompt, ) -> None:
        self.prompt1 = prompt1
        self.prompt2 = prompt2
    
    def get_dict(self):
        return {
            "prompt1":self.prompt1.get_dict(),
            "prompt2":self.prompt2.get_dict(),
        }
        
    def save(self, filename:str):
        path = config.WYRS_DIR + filename
        utils.write_json(path, self.get_dict())
        
        
        
WYR(
    Prompt(

    ),
    Prompt(

    ),
)
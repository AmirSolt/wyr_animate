from media import sound, image
from helper import utils, config
from moviepy.editor import AudioFileClip
# from anim import draw_cta, draw_wyr, draw_wyr_conclusion
    





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
    
class Frame:
    
    def save(self):
        pass
    
    def draw_frame(self, index:int)->None:
        pass
    
    def make_sound(self, index:int):
        pass
    
class WYR(Frame):
    
    def __init__(self, prompt1:Prompt, prompt2:Prompt, ) -> None:
        self.prompt1 = prompt1
        self.prompt2 = prompt2
    
    def get_dict(self):
        return {
            "prompt1":self.prompt1.get_dict(),
            "prompt2":self.prompt2.get_dict(),
        }
        
    def save(self, filename:str|None=None):
        """
        just filename
        .json is added by default
        """
        filename = filename if filename else self.__get_auto_filename()
        path = config.WYRS_DIR + filename + ".json"
        utils.write_json(path, self.get_dict())
        
        
    def make_sound(self, index:int):
        file_path = config.TEMP_DIR+f"{index}{config.WYR_SOUND_INDICATOR}" + ".mp3"
        conc_file_path = config.TEMP_DIR+f"{index}{config.WYR_CONCLUSION_SOUND_INDICATOR}" + ".mp3"
        text = f"Would you rather, {self.prompt1.text}, or, {self.prompt2.text}."
        print(f">>>> {text}")
        sound.make_wyr_audio(text, file_path)
        sound.make_wyr_conc_audio(conc_file_path)
        
    def draw_frame(self, index):
        frame_path = config.TEMP_DIR+f"{index}{config.WYR_INDICATOR}.png"
        conclusion_path = config.TEMP_DIR+f"{index}{config.WYR_CONCLUSION_INDICATOR}.png"
        image.draw_wyr(self, frame_path)
        image.draw_wyr_conclusion(self, conclusion_path)
        
    def __get_auto_filename(self):
        files = utils.get_all_files(config.WYRS_DIR)
        return f"{len(files)}"
               
class CTA(Frame):
    # call to action
    
    def __init__(self, text:str) -> None:
        self.text = text
        
    def make_sound(self, index:int):
        file_path = config.TEMP_DIR+f"{index}{config.CTA_SOUND_INDICATOR}" + ".mp3"
        sound.make_cta_adio(file_path)
        
        
    def draw_frame(self, index):
        frame_path = config.TEMP_DIR+f"{index}{config.CTA_INDICATOR}.png"
        image.draw_cta(self, frame_path)    



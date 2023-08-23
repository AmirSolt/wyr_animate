from helper import config, utils
from moviepy.editor import *
from moviepy.editor import ImageClip, concatenate_videoclips, CompositeVideoClip









def draw_video():
    image_files = utils.get_all_files(config.TEMP_DIR)
    image_files = utils.order_files_by_num(image_files)

    clips = []
    for file in image_files:
        clip = None
        
        if config.CTA_INDICATOR in file:
            duration = 4
            fade_duration = 0.5
            clip = ImageClip(file).set_duration(duration).crossfadein(fade_duration)
            
        if config.WYR_INDICATOR in file:
            duration = 5 # dynamic depend on tts
            duration_padding = 3 # other sound effects
            duration += duration_padding
            fade_duration = 0.5
            clip = ImageClip(file).set_duration(duration).crossfadein(fade_duration)
            
        if config.WYR_CONCLUSION_INDICATOR in file:
            duration = 2
            clip = ImageClip(file).set_duration(duration)
            
        if clip:
            clips.append(clip)            
            
    
    video = concatenate_videoclips(clips, method="compose")
    vids = utils.get_all_files(config.VID_DIR)
    index = len(vids)
    video.write_videofile(config.VID_DIR+f"{index}.mp4", fps=12)  
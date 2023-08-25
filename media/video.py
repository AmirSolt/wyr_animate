from helper import config, utils
from moviepy.editor import *
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip




fade_duration = 0.5

       

def generate_video():
    files = utils.get_all_files(config.TEMP_DIR)
    files = utils.order_files_by_num(files)
    image_files = [file for file in files if file.endswith('.png')]
    audio_files = [file for file in files if file.endswith('.mp3')]
    
    
    clips = []
    for image_file, audio_file in zip(image_files, audio_files):
        clip = None
        
        if config.CTA_INDICATOR in image_file:
            audio_clip = AudioFileClip(audio_file)
            clip = ImageClip(image_file).set_duration(audio_clip.duration).fx(transfx.slide_out, duration=fade_duration, side="left")
            clip = clip.set_audio(audio_clip)
            
        if config.WYR_INDICATOR in image_file:
            audio_clip = AudioFileClip(audio_file)
            clip = ImageClip(image_file).set_duration(audio_clip.duration).fx(transfx.slide_out, duration=fade_duration, side="left")
            clip = clip.set_audio(audio_clip)
            
            
        if config.WYR_CONCLUSION_INDICATOR in image_file:
            audio_clip = AudioFileClip(audio_file)
            clip = ImageClip(image_file).set_duration(audio_clip.duration)
            clip = clip.set_audio(audio_clip)
            
            
        if clip:
            clips.append(clip) 

    video = concatenate_videoclips(clips, method="compose")
    music = AudioFileClip(config.STATIC_DIR+"sounds/music.mp3").volumex(0.01)
    
    if video.duration < music.duration:
        music = music.subclip(0, video.duration)
    if video.duration > music.duration:
        loops = int(video.duration // music.duration) + 1
        music_clips = [music]*loops
        music = concatenate_audioclips(music_clips)
        music = music.subclip(0, video.duration)
    
    
    final_audio = CompositeAudioClip([video.audio, music])
    video = video.set_audio(final_audio)
    vids = utils.get_all_files(config.VID_DIR)
    index = len(vids)
    video.write_videofile(config.VID_DIR+f"{index}.mp4", fps=12)  
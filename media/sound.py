
from helper import config, utils
import requests
from moviepy.editor import *
import pydub
from pydub import AudioSegment
import time
from pathlib import PurePath
import numpy as np
from moviepy.audio.AudioClip import AudioArrayClip


API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def silent(duration:float)->AudioArrayClip:
    rate = 44100
    data_mono = np.zeros((int(duration*rate/2), 1))
    return AudioArrayClip(data_mono, fps=rate)

def wait_until_file_exists(temp_tts_filepath, timeout, period=0.5):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if utils.does_file_exist(temp_tts_filepath): return True
        time.sleep(period)
    return False


def generate_tts(text:str, tts_filepath:str):
    utils.wipe_dir(config.TRASH_DIR)
    
    payload = {"inputs": text,}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    temp_tts_filepath = config.TRASH_DIR+"temp_tts.flac"
    with open(temp_tts_filepath, 'wb') as audio:
        audio.write(response.content)
    
    wait_until_file_exists(temp_tts_filepath, 1)
    

    song = AudioSegment.from_file(temp_tts_filepath)
    song.export(tts_filepath, format="mp3")

    

def make_wyr_audio(text:str, filepath:str):
    
    tts_filepath = config.TRASH_DIR+"tts.mp3"
    
    generate_tts(text, tts_filepath)
    
    start_ding_path = config.SOUNDS_DIR + "score.mp3"
    finish_ding_path = config.SOUNDS_DIR + "score2.mp3"
    
    final_audio = concatenate_audioclips([
        AudioFileClip(start_ding_path),
        silent(duration=1),
        AudioFileClip(tts_filepath),
        silent(duration=3),
        AudioFileClip(finish_ding_path),
        AudioFileClip(finish_ding_path),
        AudioFileClip(finish_ding_path),
    ])
    
    final_audio.write_audiofile(filepath)



def make_wyr_conc_audio(filepath:str):
    success_path = config.SOUNDS_DIR + "correct_short.mp3"
    final_audio = concatenate_audioclips([
        AudioFileClip(success_path),
        silent(duration=1.5),
    ])
    final_audio.write_audiofile(filepath)

    
def make_cta_adio(filepath:str):
    success_path = config.SOUNDS_DIR + "correct_short.mp3"
    final_audio = concatenate_audioclips([
        AudioFileClip(success_path),
        silent(duration=4),
    ])
    final_audio.write_audiofile(filepath)

    
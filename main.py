from media import video
from wyr import Frame, WYR, Prompt, CTA
from helper import config, utils


def main():
    
    utils.create_dir_if_not_exist(config.IMGS_DIR)
    utils.create_dir_if_not_exist(config.TEMP_DIR)
    utils.create_dir_if_not_exist(config.WYRS_DIR)
    utils.create_dir_if_not_exist(config.VID_DIR)
    utils.create_dir_if_not_exist(config.DATA_DIR)
    utils.create_dir_if_not_exist(config.TRASH_DIR)
    
    # for frame in frames:
    #     frame.save()

    utils.wipe_dir(config.TEMP_DIR)
    for i, frame in enumerate(frames):
        frame.draw_frame(i)
        frame.make_sound(i)
        print("====================================")
        
    video.generate_video()




frames:list[Frame] = [
    WYR(
        Prompt(
            text="to watch Oppenheimer for the rest of your life",
            img="./data/imgs/oppenheimer.jpg",
        ),
        Prompt(
            text="to watch Barbie for the rest of your life",
            img="./data/imgs/barbie.jpg",
        ),
    ),
    WYR(
        Prompt(
            text="fight a million scorpions",
            img="./data/imgs/scorpion.jpg",
        ),
        Prompt(
            text="get buried alive",
            img="./data/imgs/buried.jpg",
        ),
    ),
    WYR(
        Prompt(
            text="spend a year entirely alone",
            img="./data/imgs/alone.jpg",
        ),
        Prompt(
            text="a year without a home",
            img="./data/imgs/homeless.jpg",
        ),
    ),
    CTA(text="  Duet your \n answers 🥸"),
    WYR(
        Prompt(
            text="only buy used underwear",
            img="./data/imgs/underwear.jpg",
        ),
        Prompt(
            text="only buy used toothbrushes",
            img="./data/imgs/toothbrush.jpg",
        ),
    ),
    WYR(
        Prompt(
            text="lose the ability to read",
            img="./data/imgs/read.jpg",
        ),
        Prompt(
            text="lose the ability to speak",
            img="./data/imgs/speak.jpg",
        ),
    ),
    WYR(
        Prompt(
            text="have a dog that listens to you",
            img="./data/imgs/dog.jpg",
        ),
        Prompt(
            text="have a dog that can speak but doesn't like you",
            img="./data/imgs/dog2.jpg",
        ),
    ),

]

main()
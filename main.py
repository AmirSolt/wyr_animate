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
            text="find true love",
            img="./data/imgs/love.jpg",
            perc=38,
        ),
        Prompt(
            text="win the lottery",
            img="./data/imgs/lottery.jpg",
            perc=62,
        ),
    ),
    WYR(
        Prompt(
            text="be in prison for 5 years",
            img="./data/imgs/prison.jpg",
            perc=65,
        ),
        Prompt(
            text="be in coma for a decade",
            img="./data/imgs/sleep.jpg",
            perc=35,
        ),
    ),
    WYR(
        Prompt(
            text="be a popular comedian",
            img="./data/imgs/mic.jpg",
            perc=29,
        ),
        Prompt(
            text="cure cancer",
            img="./data/imgs/scientist.jpg",
            perc=71,
        ),
    ),
    CTA(text="Follow for more \n\n            :)"),
    WYR(
        Prompt(
            text="have no internet",
            img="./data/imgs/wifi.jpg",
            perc=56,
        ),
        Prompt(
            text="never shower again",
            img="./data/imgs/shower.jpg",
            perc=44,
        ),
    ),
    WYR(
        Prompt(
            text="know the date of your death",
            img="./data/imgs/time.jpg",
            perc=82,
        ),
        Prompt(
            text="know the cause of your death",
            img="./data/imgs/death.jpg",
            perc=18,
        ),
    ),
    WYR(
        Prompt(
            text="Always have to use sandpaper as toilet paper",
            img="./data/imgs/toilet.jpg",
            perc=49,
        ),
        Prompt(
            text="Always have to use hot sauce as eye drops",
            img="./data/imgs/hot_sauce.jpg",
            perc=51,
        ),
    ),
    WYR(
        Prompt(
            text="Climb the tallest mountain",
            img="./data/imgs/mountain.jpg",
            perc=58,
        ),
        Prompt(
            text="Travel to the bottom of the sea",
            img="./data/imgs/ocean.jpg",
            perc=42,
        ),
    ),
]

main()
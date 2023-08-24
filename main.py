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
            img="./data/imgs/test0.png",
            perc=38,
        ),
        Prompt(
            text="win the lottery but never find love",
            img="./data/imgs/test1.png",
            perc=62,
        ),
    ),
    WYR(
        Prompt(
            text="be in prison for 5 years",
            img="./data/imgs/test0.png",
            perc=65,
        ),
        Prompt(
            text="be in coma for a decade",
            img="./data/imgs/test1.png",
            perc=35,
        ),
    ),
    WYR(
        Prompt(
            text="be a popular comedian",
            img="./data/imgs/test0.png",
            perc=29,
        ),
        Prompt(
            text="cure cancer",
            img="./data/imgs/test1.png",
            perc=71,
        ),
    ),
    CTA(text="Follow for more \n\n            :)"),
    WYR(
        Prompt(
            text="have no internet",
            img="./data/imgs/test0.png",
            perc=56,
        ),
        Prompt(
            text="never shower again",
            img="./data/imgs/test1.png",
            perc=44,
        ),
    ),
    WYR(
        Prompt(
            text="know the date of your death",
            img="./data/imgs/test0.png",
            perc=82,
        ),
        Prompt(
            text="know the cause of your death",
            img="./data/imgs/test1.png",
            perc=18,
        ),
    ),
    WYR(
        Prompt(
            text="Always have to use sandpaper as toilet paper",
            img="./data/imgs/test0.png",
            perc=49,
        ),
        Prompt(
            text="Always have to use hot sauce as eye drops",
            img="./data/imgs/test1.png",
            perc=51,
        ),
    ),
    WYR(
        Prompt(
            text="let your parents die",
            img="./data/imgs/test0.png",
            perc=29,
        ),
        Prompt(
            text="have sex with them",
            img="./data/imgs/test1.png",
            perc=71,
        ),
    ),
]

main()
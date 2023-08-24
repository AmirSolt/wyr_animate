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
            text="laugh",
            img="./data/imgs/test0.png",
            perc=70,
        ),
        Prompt(
            text="cry",
            img="./data/imgs/test1.png",
            perc=30,
        ),
    ),
    CTA(text="Follow for more \n\n            :)"),
    WYR(
        Prompt(
            text="laugh",
            img="./data/imgs/test0.png",
            perc=70,
        ),
        Prompt(
            text="cry",
            img="./data/imgs/test1.png",
            perc=30,
        ),
    ),
    # WYR(
    #     Prompt(
    #         text="laugh",
    #         img="./data/imgs/test0.png",
    #         perc=50,
    #     ),
    #     Prompt(
    #         text="cry",
    #         img="./data/imgs/test1.png",
    #         perc=50,
    #     ),
    # ),
    # WYR(
    #     Prompt(
    #         text="laugh",
    #         img="./data/imgs/test0.png",
    #         perc=40,
    #     ),
    #     Prompt(
    #         text="cry",
    #         img="./data/imgs/test1.png",
    #         perc=60,
    #     ),
    # ),
]

main()
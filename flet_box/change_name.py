import os

list_dir = os.listdir(os.getcwd())


for index, _ in enumerate(list_dir):

    basename_text = os.path.splitext(_)

    if not basename_text[1] == ".py":
        rename_text = f"image{index}{basename_text[1]}"
        original = os.path.basename(_)

        os.rename(src=original,dst=rename_text)
import os
import PIL
import PIL.Image as Image

def full_list_dir(input_path, is_dir=False):
    elements = os.listdir(input_path)
    elements = [os.path.join(input_path, e) for e in elements]
    if not is_dir:
        return elements
    else:
        folders = [e for e in elements if os.path.isdir(e)]
        return folders


forward_cameras = list(range(5))
forward_cameras.pop()
horizontal_cameras = list(range(5))

root_folder = '/data/teddy/Datasets/carla_cross'

COLOR_CAMERAS = ['ForwardCamera{}RGB'.format(i) for i in forward_cameras]
COLOR_CAMERAS += ['HorizontalCamera{}RGB'.format(i) for i in horizontal_cameras]

towns = full_list_dir(root_folder, is_dir=True)
list_of_episodes = []
for town in towns:
    for e in full_list_dir(town, True):
        list_of_episodes.append(e)

# Run over each episode and each camera folder apply png to jpeg conversion
for episode in list_of_episodes:
    for col_folder in COLOR_CAMERAS:
        col_path = os.path.join(episode, col_folder)
        imgs_list = full_list_dir(col_path, False)
        for im in imgs_list:
            print(im)
        exit()
        for img in imgs_list:
            if img.endswith('.png'):
                dest_name = img.replace('png', 'jpg')
                im_pil = Image.open(img)
                im_pil.save(filename=dest_name, quality=90)
                im_pil.close()

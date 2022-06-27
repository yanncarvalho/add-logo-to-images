import argparse
from datetime import datetime
from os import path, getcwd, mkdir, listdir, removedirs
from PIL import Image, UnidentifiedImageError

current_datetime = datetime.now().strftime("%d-%m-%Y, %H %M' %S''")
reduction_proportion = 500
margin = 10

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--logo', action='store', dest='logo_path',
                    default=getcwd()+'\\logo.png', required=False,
                    help='Path where it is possible to find a logo')

parser.add_argument('-p', '--path', action='store', dest='imgs_path',
                    default=getcwd(), required=False,
                    help='Path where there are images to add a logo to')

parser.add_argument('-e', '--extension', action='store', dest='imgs_extension',
                    default="jpeg, jpg, jpe, jfif", required=False,
                    help='extensions of the images to add a logo to')

args = parser.parse_args()

imgs_path = args.imgs_path[:- 1] if args.imgs_path.endswith('\\') else args.imgs_path
imgs_extension = tuple(args.imgs_extension.lower().replace(' ','').split(','))
logo_path = args.logo_path

if not path.isdir(imgs_path):
  print(f'ERROR: Path "{imgs_path}" not localized')
  quit()
else:
  base_folder_name = path.basename(imgs_path)
  new_folder_name = f"{base_folder_name} with logo ({current_datetime})"
  new_folder_path = path.join(imgs_path, new_folder_name)

try:
  logo = Image.open(logo_path)
except (FileNotFoundError):
  print(f'ERROR: There is no logo in the path: "{logo_path}"')
  quit()

print(f'Logo will be: "{logo_path}"',
      f'It will only consider images with extension: {imgs_extension} \n',
      f'Creating folder "{new_folder_name}" to save images with logo\n', sep="\n")

mkdir(new_folder_path)

try:
  img = None
  for file in listdir(path=imgs_path):
      file_path = f"{imgs_path}\\{file}"
      if file.lower().endswith(imgs_extension) and (file_path != logo.filename):
        try:
          img = Image.open(file_path)
          print(type(img))
          if img.height > img.width:
              cof_resize = img.height/reduction_proportion
          else:
              cof_resize = img.width/reduction_proportion

          logo_rezided_size = (int(logo.width/cof_resize),
                            int(logo.height/cof_resize))

          logo_rezided = logo.resize(
              logo_rezided_size)

          logo_img_position = (
              (img.width-logo_rezided.width)-margin,
              (img.height-logo_rezided.height)-margin)

          img.paste(logo_rezided, logo_img_position, mask=logo_rezided)

          print(f'Saving image: "{file}"')
          new_file_path = f"{new_folder_path}\\{file}"
          img.save(new_file_path)

        except(UnidentifiedImageError):
           print(f'Not Saving: "{file}" - was not considered a photo')
except(Exception):
  print("Something happening, script could not execute properly")
  img = None
finally:
  if img is None:
      print('\nNo images was added logo -',
              f'Deleting folder "{new_folder_name}" created to save images with logo')
      removedirs(new_folder_path)
  else:
      print("\nAll images were saved with logo successfully!")

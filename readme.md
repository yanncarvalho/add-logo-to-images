# Add Logo to Images #

A simple script in Python for adding logo to images

## Built with ##

- Python 3.9.1
- Pillow 9.1.1

## How it works ##

By default when is executed this script, it will in the current folder search for an archive called "logo.png" and add it to all images with extensions: "jpeg, jpg, jpe, jfif".

### Changing default configurations ###

It is possible to change the default configurations sending some parameters
- -l, --logo __path__ - define the folder where Python will search for the logo image
- -e, --extension "extensions separate by coma" - define the list of extensions whose it will be added logo to
- -p, --path __path__ - define the folder where Python will looking for images to put logo to

### Example ###

``` sh
python add_logo.py -l "c:/some_place/logo_img.any_extension" -e "wepb, png" -p "c:/some_place_else"
```

## Author ##

- Made by [Yann Carvalho](https://www.linkedin.com/in/yann-carvalho-764abab6/)

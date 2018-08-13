# strip-exif
A Python script to strip EXIF data from images.
---

## Dependencies
* [Pillow](https://pillow.readthedocs.io/en/latest/)

This was written with Python 2.7 and has not been tested with any other versions.

## Usage
```
python strip_exif.py file1.jpg file2.jpg dir1/ dir2/ ...
```

Images must be .jpg, .jpeg, or .png for this script to work.

## Examples
```
python strip_exif.py IMG_3258.jpg IMG_3259.jpg IMG_3260.jpg
```
```
python strip_exif.py ImageDirectory/ SomeDirectory/
```
```
python strip_exif.py IMG_3258.jpg IMG_3259.jpg ImageDirectory/
```

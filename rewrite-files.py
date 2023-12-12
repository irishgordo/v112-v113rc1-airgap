import os
import random

def main():
    pictures = os.listdir()
    names = set()
    for pic in pictures:
        if pic.endswith('.png') or pic.endswith('.jpg'):
            print(pic)
            newname = random.randint(1, 1000)
            while newname in names:
                newname = random.randint(1, 1000)
            names.add(newname)
            print(newname)
            if pic.endswith('jpg'):
                os.rename(pic, str(newname) + '.jpg')
            else:
                os.rename(pic, str(newname) + '.png')
            print(pic)
            print(newname)
            print('renamed')
        else:
            print('not a picture')


if __name__ == "__main__":
    main()
import os

# https://raw.githubusercontent.com/irishgordo/v112-rc3-testing/main/RKE1-Test-Artifacts/32.png
def main():
    pictures = os.listdir()
    try:
        os.remove('README.md')
        print(f'removed old readme')
    except OSError as ex:
        pass
    with open("README.md", "w") as readme:
        for pic in pictures:
            # if the pic ends with .png, .jpg, or .jpeg only
            if pic.endswith('.png') or pic.endswith('.jpg') or pic.endswith('.jpeg'):
                if pic != 'make-things.py' and pic != 'README.md':
                    readme.write('\n')
                    sntzepic = pic.replace(' ', '\\ ')
                    mrkdwnpic = (f'![{pic}](https://raw.githubusercontent.com/irishgordo/v112-v113rc1-airgap/main/{pic})')
                    readme.write(mrkdwnpic)
                    readme.write('\n')

if __name__ == "__main__":
    main()
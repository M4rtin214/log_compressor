#-------------------------------------------------------------------------------
# Name:        log_compressor
# Purpose:     Skript projde soubory *.log v "PATH" a zkomprimuje je do gzip
#              souboru, puvodni soubor nahradni prazdnym souborem
#              - musi byt spusteno s pravy pro zapis
#-------------------------------------------------------------------------------

import gzip
import os

PATH = "/var/log"


def convert_to_gzip(file_path):
    with open(file_path, 'rb') as f_in, gzip.open(f"{file_path}.gz", 'wb') as f_out:
        f_out.writelines(f_in)

def main():
    for root, dirs, files in os.walk(PATH):
        for name in files:
            if name.endswith((".log")):
                file_path = f"{root}/{name}"
                convert_to_gzip(file_path)
                with open(file_path, 'w') as f:
                    f.write("")

if __name__ == '__main__':
    main()




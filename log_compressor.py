#-------------------------------------------------------------------------------
# Name:        log_compressor
# Purpose:     Skript projde soubory *.log v "PATH" a zkomprimuje je do gzip
#              souboru, puvodni soubor nahradni prazdnym souborem. Prepise 
#              puvodni gzip soubory.
#              - vyzaduje prava pro zapis (linux)
#-------------------------------------------------------------------------------

import gzip
import os

PATH = "/var/log"


def convert_to_gzip(full_path):
    with open(full_path, 'rb') as f_in, gzip.open(f"{full_path}.gz", 'wb') as f_out:
        f_out.writelines(f_in)

def main():
    for root, dirs, files in os.walk(PATH):
        for name in files:
            if name.endswith((".log")):
                full_path = f"{root}/{name}"
                convert_to_gzip(full_path)
                with open(full_path, 'w') as f:
                    f.write("")

if __name__ == '__main__':
    main()




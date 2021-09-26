import os
import sys
import time
from modules.helpers import check_dir
from modules.banners import print_banner
from modules.pw_microsoft_learn import ms_learn


working_dir = str(os.path.dirname(os.path.abspath(__file__)))

required_folders = {
    "export": "\\export"
}

def main():
    export_dir = working_dir + required_folders["export"]
    print_banner("single", "header-start")

    if check_dir(export_dir):
        print_banner("double", "header-start", "check-dir-pos")
    else:
        print_banner("double", "header-start", "check-dir-neg")

    print_banner("double", "header-start", "user-options")

    selected = input("Please enter one of the above options here: ")

    if selected == "1":
        module_url = input("Please enter the module url below:\n")

        if module_url:
            if ms_learn(module_url, export_dir):
                print_banner("double", "header-start", "export-success")
                time.sleep(5)
                main()
            else:
                print_banner("double", "header-start", "export-fail")
                time.sleep(5)
                main()
        else:
            print_banner("double", "header-start", "url-invalid")
            time.sleep(5)
            main()
    elif selected == "2":
        print_banner("single", "header-stop")
        sys.exit(0)
    else:
        pass

if __name__ == "__main__":
    main()

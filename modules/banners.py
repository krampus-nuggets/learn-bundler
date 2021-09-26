from os import system


banners = {
    "header-start": """
╦  ╔═╗╔═╗╦═╗╔╗╔   ╔╗ ╦ ╦╔╗╔╔╦╗╦  ╔═╗╦═╗
║  ║╣ ╠═╣╠╦╝║║║───╠╩╗║ ║║║║ ║║║  ║╣ ╠╦╝
╩═╝╚═╝╩ ╩╩╚═╝╚╝   ╚═╝╚═╝╝╚╝═╩╝╩═╝╚═╝╩╚═
by: krampus-nuggets
    """,
    "header-stop": """
╔╗ ╦ ╦╔═╗
╠╩╗╚╦╝║╣ 
╚═╝ ╩ ╚═╝
    """,
    "check-dir-pos": "Directory Check: Required directories found, continuing...",
    "check-dir-neg": "Directory Check: Required directories not found, they will be created...",
    "user-options": """
All available options can be found below:

1. Export a MS Learn module | Press 1
2. Close program | Press 2
    """,
    "url-invalid": "ERROR: Invalid URL | Program Reset",
    "export-success": "EXPORT: Successful, file saved to export directory | Program Reset",
    "export-fail": "EXPORT: Failed, something went wrong... | Program Reset"
}

def print_banner(ban_type, *banner):
    if ban_type == "single":
        system("cls")
        print(banners[banner[0]])
    elif ban_type == "double":
        system("cls")
        print(banners[banner[0]])
        print(banners[banner[1]])
    elif ban_type == "no-clear":
        print(banners[banner[0]])
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
    """
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
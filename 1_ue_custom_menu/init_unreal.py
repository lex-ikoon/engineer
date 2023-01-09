import unreal
import importlib
import init_menu
importlib.reload(init_menu)


# ------------ create menu ---------------
if __name__ == '__main__':
    init_menu.create_menu()
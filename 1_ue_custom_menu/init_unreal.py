import unreal
import importlib
import init_menu
importlib.reload(init_menu)


# ------------ create menu ---------------
if __name__ == '__main__':
    init_menu.create_menu()


# ------------ lower idle GPU usage ------------
# ------------   (not to be 100%)   ------------
unreal.SystemLibrary.execute_console_command(None, "t.MaxFPS 60")
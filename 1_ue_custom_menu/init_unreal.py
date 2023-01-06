import unreal
import custom_menu

import imp
imp.reload(custom_menu);

if __name__ == '__main__':
    custom_menu.create_menu()
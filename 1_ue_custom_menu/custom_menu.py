import unreal



# -----------------
# create: level from files
# create: level from name

# select: RenderQueueConfig // apply to: all items in RenderQueue
# select: Camera // apply settings from Houdini file




command_name = "MyCommandName"



entry = unreal.ToolMenuEntry(
    name            = command_name,
    type            = unreal.MultiBlockType.MENU_ENTRY,
    insert_position = [None, unreal.ToolMenuInsertType.DEFAULT],
)
entry.set_label("My Command Verbose Name")
entry.set_string_command(
    type        = unreal.ToolMenuStringCommandType.PYTHON,
    custom_type = command_name,
    string      = "print ("foo")"       #< !! This is where things get interesting
)

# -- Add to the menu made earlier
custom_menu.add_menu_entry(command_name, entry)






def create_menu():
    menus = unreal.ToolMenus.get()

    # Find the "Main" menu, this should not fail,
    # but if we're looking for a menu we're unsure about 'if not'
    # works as nullptr check,
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not main_menu:
        print("Failed to find the 'Main' menu. Something is wrong in the force!")

    entry = unreal.ToolMenuEntry(
                                name="Python.Tools",
                                # If you pass a type that is not supported Unreal will let you know,
                                type=unreal.MultiBlockType.MENU_ENTRY,
                                # this will tell unreal to insert this entry into the First spot of the menu
                                insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
    )
    entry.set_label("YourMenuItemName")
    # this is what gets executed on click
    # entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, custom_type="command_name", string=("from foo import bar;bar.main()"))

    command_name = 'MyCommandName'

    entry.set_string_command(
        type=unreal.ToolMenuStringCommandType.PYTHON,
        custom_type=command_name,
        string='print ("foo")'       #< !! This is where things get interesting
    )

    # entry.set_string_command(1, string=("from foo import bar;bar.main()"))
    # add a new menu called PyTools to the MainMenu bar. You should probably rename the last 3 properties here to useful things for you
    script_menu = main_menu.add_sub_menu(main_menu.get_name(), "PythonTools", "Tools", "PyTools")
    # add our new entry to the new menu
    script_menu.add_menu_entry("Scripts",entry)
    # refresh the UI
    menus.refresh_all_widgets()





# def create_menu() :
#     menus = unreal.ToolMenus.get()

#     # Find the 'edit' menu, this should not fail, 
#     # but if we're looking for a menu we're unsure about 'if not' 
#     # works as nullptr check,
#     edit = menus.find_menu("LevelEditor.MainMenu.Edit")
#     main_menu = menus.find_menu("LevelEditor.MainMenu")
#     if not edit:
#         print("Failed to find the 'Edit' menu")

#     entry = unreal.ToolMenuEntry(
#         name = "MyEntry",
#         type = unreal.MultiBlockType.MENU_ENTRY, # If you pass a type that is not supported Unreal will let you know,
#         insert_position = unreal.ToolMenuInsert("Delete", unreal.ToolMenuInsertType.AFTER) # this will tell unreal to insert this entry after the 'Delete' menu item, if found in section we define later,
#     )

#     entry.set_label("My Entry")
#     entry.set_tool_tip("This is a Tool Menu Entry made in Python!")

#     edit.add_menu_entry("EditMain", entry) # section name, ToolMenuInsert, Unreal will add the section name if it can't find it, otherwise call AddEntry for the found section,

#     my_menu = main_menu.add_sub_menu("My.Menu", "Python", "My Menu", "This is a IKOON")

#     for name in ["Foo", "Bar", "Baz"]:
#         e = unreal.ToolMenuEntry(
#             name = name,
#             type = unreal.MultiBlockType.MENU_ENTRY, # If you pass a type that is not supported Unreal will let you know,
#         )
#         e.set_label(name)
#         my_menu.add_menu_entry("Items", e)

#     menus.refresh_all_widgets()

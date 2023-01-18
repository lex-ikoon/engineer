import unreal


def create_menu():

    entry_names    = []
    entry_labels   = []
    entry_tooltips = []
    entry_commands = []

    # ---------

    entry_names.append(       "create_levels")
    entry_tooltips.append(    "houdini filemarks should be here: Q:/_engine/_json/create")
    entry_labels.append(      "create levels")
    entry_commands.append(    "import ue_level; import importlib; importlib.reload(ue_level); ue_level.find_filemarks_to_create_levels()")

    # ---------

    entry_names.append(       "camera_settings")
    entry_tooltips.append(    "select in outliner: _CAM (Camera)           (applies settings from Houdini file)")
    entry_labels.append(      "update camera settings")
    entry_commands.append(    "import ue_camera; import importlib; importlib.reload(ue_camera); ue_camera.update_camera_settings('MENU')")

    # ---------

    entry_names.append(       "render_job_settings")
    entry_tooltips.append(    "select in outliner: _CONFIG (RenderQueueConfig)           (applies to: all items in RenderQueue")
    entry_labels.append(      "apply render job settings")
    entry_commands.append(    "import ue_render_job; import importlib; importlib.reload(ue_render_job); ue_render_job.apply_selected_RenderQueueConfig()")



    # ------------- backup
    # custom_menu = ue_main_menu.add_sub_menu("My.Menu", "Python", "My Menu", "This is a IKOON")
    # insert_position = unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
    # https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/ToolMenuInsertType.html

    ue_menus  = unreal.ToolMenus.get()
    ue_main_menu = ue_menus.find_menu("LevelEditor.MainMenu")
    if not ue_main_menu:
        print("Failed to find the 'Main' menu. Something is wrong in the force!")

    custom_menu = ue_main_menu.add_sub_menu(ue_main_menu.get_name(), section_name = "ikoon_menu_section_name", name = "ikoon_menu_name", label = "ikoon.py", tool_tip = "Scripts by ikoon")

    # --------------- entries ----------------------

    for i in range(len(entry_names)):

        entry = unreal.ToolMenuEntry(
            name            = entry_names[i],
            type            = unreal.MultiBlockType.MENU_ENTRY,
            insert_position = unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
            # insert_position = [None, unreal.ToolMenuInsertType.DEFAULT],
        )

        entry.set_label(entry_labels[i])
        entry.set_tool_tip(entry_tooltips[i])
        entry.set_string_command(
            type        = unreal.ToolMenuStringCommandType.PYTHON,
            custom_type = entry_names[i],
            string      = entry_commands[i]
        )

        custom_menu.add_menu_entry(entry_names[i], entry)

    # --------------- entries ----------------------


    # refresh the UI
    ue_menus.refresh_all_widgets()
import unreal



def update_camera_settings() :

    # resolution_x      = 150
    # resolution_y      = 150
    # frame_range_start = 1
    # frame_range_start = 150
    # fps               = 30


       
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    a = eas.get_selected_level_actors()

    _cineCameraComponent = a[0].get_cine_camera_component()
    # _cineCameraComponent.set_editor_property("focus_settings",_focusSettings)

    # unreal.LensInfo().sensor_dimensions = unreal.Vector2D(200,100)

    # _cineCameraComponent.filmback.sensor_dimensions = unreal.Vector2D(200,100)
    _cineCameraComponent.filmback.sensor_width = 150
    _cineCameraComponent.filmback.sensor_height = 123
    
    print (_cineCameraComponent.filmback)
    print(a)

    # in ue4, a simple way is hovering the mouse cursor on the object ui in outliner, it will display id name
    # then, use “/Game/your_map_name.your_map_name:PersistentLevel.your_object_id_name”

    # in ue5, you could use eas.get_all_level_actors() 


# [/Script/CinematicCamera.CineCameraActor'"/Game/Main.Main:PersistentLevel.CineCameraActor_1"']
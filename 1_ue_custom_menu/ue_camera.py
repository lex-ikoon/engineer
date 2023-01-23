import json
import unreal


def update_camera_settings(cine_cam_component) :

    if cine_cam_component == "MENU" :
        outliner           = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        selection          = outliner.get_selected_level_actors()
        cine_cam_component = selection[0].get_cine_camera_component()


    # ------------  tag  ----------------

    json_path = cine_cam_component.component_tags[0]
    json_path = str(json_path)

    # ------------  load json ----------------
    # json_path = "Q:/_engine/_json/settings/seq." + hip_name + "." + job_name + ".json"
    # print(json_path)

    with open(json_path, "r") as read_file:
        json_content = json.load(read_file)


        focus_distance = float(      json_content['level_settings']["focus_distance"]     )
        focal_length   = float(      json_content['level_settings']["focal_length"]     )
        resx           = float(      json_content['level_settings']["resx"]     )
        resy           = float(      json_content['level_settings']["resy"]     )

        #  ---------
        
        rangex = float(      json_content['level_settings']["rangex"]     )
        rangey = float(      json_content['level_settings']["rangey"]     )
        fps    = float(      json_content['level_settings']["fps"]     )

        #  ---------
        
        tx = float(      json_content['level_settings']["tx"]     )
        ty = float(      json_content['level_settings']["ty"]     )
        tz = float(      json_content['level_settings']["tz"]     )
        rx = float(      json_content['level_settings']["rx"]     )
        ry = float(      json_content['level_settings']["ry"]     )
        rz = float(      json_content['level_settings']["rz"]     )

        # print(resx, resy, tx, ty, tz, rx, ry, rz)

    read_file.close()

    # -------  location rotation  ---------

    location_cam = unreal.Vector( tx,ty,tz)
    rotation_cam = unreal.Rotator(rx,ry,rz)
    actor_cam    = cine_cam_component.get_outer()

    actor_cam.set_actor_location (location_cam, sweep=False, teleport=True)
    actor_cam.set_actor_rotation (rotation_cam, teleport_physics=True)


    # -------  focus --------

    focus_settings                       = unreal.CameraFocusSettings()
    focus_settings.focus_method          = unreal.CameraFocusMethod.MANUAL
    focus_settings.smooth_focus_changes  = False
    focus_settings.focus_offset          = 0.0
    focus_settings.manual_focus_distance = focus_distance

    # apply
    cine_cam_component.set_editor_property("focus_settings",focus_settings)


    # -------  max focal length --------
    lens_settings                  = unreal.CameraLensSettings()
    lens_settings.min_focal_length = 2
    lens_settings.max_focal_length = 20000
    lens_settings.min_f_stop       = 0.1
    lens_settings.max_f_stop       = 100


    # apply
    cine_cam_component.set_editor_property("lens_settings",lens_settings)

    # lock in viewport
    # actor_cam.editor_lock_location(True)

    # -------  sensor --------
    cine_cam_component.filmback.sensor_width  = resx
    cine_cam_component.filmback.sensor_height = resy
    cine_cam_component.current_focal_length   = focal_length

    #-------------------------------------------

    

# pilot_level_actor(actor_to_pilot
# https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/EditorLevelLibrary.html?highlight=camera%20pilot
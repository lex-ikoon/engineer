import os
import json
import unreal
import importlib


def find_filemarks_to_create_levels() :

    # ------------  find filemarks ----------------    
    directory = "Q:/_engine/_json/create/"

    for file in os.listdir(directory) :
        if file.startswith("create.") & file.endswith(".json") :


            # -----------  split filename ---------------
            hip_name = file.split(".")[1]
            job_name = file.split(".")[2]


            # ------------  create_level ----------------    
            create_level(hip_name, job_name)    


            # ------------  remove file  ----------------
            # os.remove(directory + file)






def create_level(hip_name, job_name) :

    # creates folder (All/Content/job/level)
    # creates level
    # creates sequencer
    # creates camera



    # ------------  create folder -------------
    # (All/Content/hip/job)
    path_folder = "/Game/" + hip_name + "/" + job_name
    unreal.EditorAssetLibrary.make_directory(path_folder)


    # ------------  create level --------------
    path_lev = path_folder + "/" + job_name + "_LEV"
    name_lev = job_name + "_LEV"

    if not unreal.EditorAssetLibrary.does_asset_exist(path_lev):
        asset_name   = name_lev
        package_path = path_folder
        asset_class  = unreal.World
        factory      = unreal.WorldFactory()

        unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, asset_class, factory)

    
    # ------------  create sequencer -----------

    path_seq = path_folder + "/" + job_name + "_SEQ"
    name_seq = job_name + "_SEQ"

    if not unreal.EditorAssetLibrary.does_asset_exist(path_seq):
        asset_name   = name_seq
        package_path = path_folder
        asset_class  = unreal.LevelSequence
        factory      = unreal.LevelSequenceFactoryNew()

        unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, package_path, asset_class, factory)


    # ------------  save all  &  open level ----

    # print(unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages())
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(save_map_packages=True, save_content_packages=True)
    unreal.EditorLevelLibrary.load_level(path_lev)


    # ------------  spawn sequencer -----------

    asset_seq    = unreal.load_asset(path_seq)
    location_seq = unreal.Vector(100, 100, 100)
    rotation_seq = unreal.Rotator(0.0, 0.0, 0.0)
    spawned_seq  = unreal.EditorLevelLibrary.spawn_actor_from_object(asset_seq, location_seq, rotation_seq)


    # ------------  load json ----------------
    json_path = "Q:/_engine/_json/settings/seq." + hip_name + "." + job_name + ".json"

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

    # ------------  sequencer settings ---------

    frame_rate = unreal.FrameRate(numerator = fps, denominator = 1)
    asset_seq.set_display_rate(   frame_rate)
    asset_seq.set_playback_start( rangex)
    asset_seq.set_playback_end(   rangey)


    # ------------  spawn cam ----------------

    class_cam    = unreal.CineCameraActor
    location_cam = unreal.Vector( tx,ty,tz)
    rotation_cam = unreal.Rotator(rx,ry,rz)
    spawned_cam  = unreal.EditorLevelLibrary.spawn_actor_from_class(class_cam, location_cam, rotation_cam)
    spawned_cam.set_actor_label(job_name + "_CAM", mark_dirty=True)



    #-------------------------------------------
    # ------------  camera settings ------------

    cine_cam_component = spawned_cam.get_cine_camera_component()

    # -------  tags   --------
    cine_cam_component.component_tags = [json_path]
    # asset_lev.component_tags = [json_path]

    import ue_camera
    importlib.reload(ue_camera)

    ue_camera.update_camera_settings(cine_cam_component)

    #-------------------------------------------
    #-------------------------------------------

    # add cam to sequencer
    # actor = unreal.EditorLevelLibrary.get_selected_level_actors()[0]
    # actor_binding = asset_seq.add_possessable(spawned_cam)


    # ------------  save everything (again) -------
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(save_map_packages=True, save_content_packages=True)


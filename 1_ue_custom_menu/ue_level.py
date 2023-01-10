import os
import json
import unreal



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

    
    # ------------  load json ----------------


    json_path = "Q:/_engine/_json/settings/seq." + hip_name + "." + job_name + ".json"

    with open(json_path, "r") as read_file:
        json_content = json.load(read_file)

        resx    = json_content['level_settings']["resx"]
        resy    = json_content['level_settings']["resy"]
        tx      = json_content['level_settings']["tx"]
        ty      = json_content['level_settings']["ty"]
        tz      = json_content['level_settings']["tz"]
        rx      = json_content['level_settings']["rx"]
        ry      = json_content['level_settings']["ry"]
        rz      = json_content['level_settings']["rz"]

    read_file.close()
    # print(resx, resy, tx, ty, tz, rx, ry, rz)


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


    # ------------  spawn sequencer -----------

    object_to_use = unreal.load_asset(path_seq)
    location      = unreal.Vector(1000.0, 400.0, 0.0)
    rotation      = unreal.Rotator(90.0, 0.0, 0.0)
    _spawnedActor = unreal.EditorLevelLibrary.spawn_actor_from_object(object_to_use, location, rotation)

    # ------------  create cam ----------------


    actor_class    = unreal.CineCameraActor
    actor_location = unreal.Vector(0.0,0.0,0.0)
    actor_rotation = unreal.Rotator(0.0,0.0,0.0)
    _spawnedActor  = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)



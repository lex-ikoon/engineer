import os
import json
import unreal



def find_filemarks_to_create_levels() :

    directory = "Q:/_engine/_json/create/"

    # ------------  find filemarks ----------------    

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


    # resolution_x      = 150
    # resolution_y      = 150
    # frame_range_start = 1
    # frame_range_start = 150
    # fps               = 30


    
    # ------------  create folder -------------
    # (All/Content/job/level)


    # path = "/Game/" + job_name + "/" + level_name
    # unreal.EditorAssetLibrary.make_directory(path)
    # path += "/"


    
    # ------------  create level --------------


    # if not unreal.EditorAssetLibrary.does_asset_exist(path+level_name):
    #     unreal.AssetToolsHelpers.get_asset_tools().create_asset(level_name, path, unreal.World, unreal.WorldFactory())

    
    # ------------  create sequencer -----------


    # sequence_name = "seq_" + level_name
    # if not unreal.EditorAssetLibrary.does_asset_exist(path+sequence_name):
    #     unreal.AssetToolsHelpers.get_asset_tools().create_asset(sequence_name, path, unreal.LevelSequence, unreal.LevelSequenceFactoryNew())


    
    # ------------  create cam ----------------


    # actor_class = unreal.CineCameraActor
    # actor_location = unreal.Vector(0.0,0.0,0.0)
    # actor_rotation = unreal.Rotator(0.0,0.0,0.0)
    # _spawnedActor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, actor_location, actor_rotation)



def ue_create_levels() :



def ue_create_level(job_name, level_name) :
    # -----------------------------------
    # load json
    resolution_x      = 150
    resolution_y      = 150
    frame_range_start = 1
    frame_range_start = 150
    fps               = 30


    # -----------------------------------
    # create folder (All/Content/job/level)
    path = "/Game/" + job_name + "/" + level_name
    unreal.EditorAssetLibrary.make_directory(path)
    path += "/"


    # -----------------------------------
    # create level
    if not unreal.EditorAssetLibrary.does_asset_exist(path+level_name):
        unreal.AssetToolsHelpers.get_asset_tools().create_asset(level_name, path, unreal.World, unreal.WorldFactory())

    # -----------------------------------
    # create sequencer
    sequence_name = "seq_" + level_name
    if not unreal.EditorAssetLibrary.does_asset_exist(path+sequence_name):
        unreal.AssetToolsHelpers.get_asset_tools().create_asset(sequence_name, path, unreal.LevelSequence, unreal.LevelSequenceFactoryNew())


    # -----------------------------------
    # create cam

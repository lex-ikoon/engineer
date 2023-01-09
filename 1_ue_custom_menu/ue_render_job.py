import unreal


# selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
# asset = selected_assets[0]
# directory_for_asset = unreal.Paths.get_path(asset.get_path_name())



path = '/Game/A/'
name = 'sequence_A'
if not unreal.EditorAssetLibrary.does_asset_exist(path+name):
    unreal.AssetToolsHelpers.get_asset_tools().create_asset(name, path, unreal.LevelSequence, unreal.LevelSequenceFactoryNew())


name = 'level_A'
if not unreal.EditorAssetLibrary.does_asset_exist(path+name):
    unreal.AssetToolsHelpers.get_asset_tools().create_asset(name, path, unreal.World, unreal.WorldFactory())


# levelName = "test1"
# levelLibrary = unreal.EditorLevelLibrary()
# success = levelLibrary.new_level("/Game/A/{}".format(levelName))







def ue_apply_selected_RenderQueueConfig():
    # -------------------------------------
    # asset should be selected
    config_asset = unreal.load_asset( "/Game/JPG" )


    # -------------------------------------
    # resolution from JSON file
    resolution = unreal.IntPoint(123, 123)



    # -------------------------------------
    # 

    subsystem    = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
    render_queue = subsystem.get_queue()


    for job in render_queue.get_jobs():

        # apply selected config
        job.set_configuration(config_asset)
        job_configuration = job.get_configuration().find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)

        # apply resolution
        job_configuration.output_resolution     = resolution

        # rename outputs
        job_configuration.output_directory.path = "Q:/__out/{sequence_name}"
        job_configuration.file_name_format      = "{sequence_name}.{frame_number}"




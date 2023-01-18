import json
import unreal



def apply_selected_RenderQueueConfig():
    # -------------------------------------
    # asset should be selected in Outliner


    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    config_asset    = selected_assets[0]

    subsystem    = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
    render_queue = subsystem.get_queue()


    for job in render_queue.get_jobs():

        seq_asset_path = str(  job.sequence.to_tuple()  )
        # ('/Game/x/abc_text/abc_text_SEQ.abc_text_SEQ',)
        print(seq_asset_path)

        hip_name = seq_asset_path.split("/")[2]
        job_name = seq_asset_path.split(".")[1]
        job_name = job_name.replace(   "_SEQ',)"   ,   ""   )
        json_path = "Q:/_engine/_json/settings/seq." + hip_name + "." + job_name + ".json"

        # ------- resolution from JSON file  ------------
        # 
        with open(json_path, "r") as read_file:
            json_content = json.load(read_file)

            resx           = float(      json_content['level_settings']["resx"]     )
            resy           = float(      json_content['level_settings']["resy"]     )
               
        read_file.close()

        # ------- apply selected config   ------------
        # 
        job.set_configuration(config_asset)
        job_configuration = job.get_configuration().find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)


        # ------- apply resolution ------------------
        resolution                          = unreal.IntPoint(resx, resy)
        job_configuration.output_resolution = resolution


        # ------- rename outputs ----------------------
        job_configuration.output_directory.path = "Q:/__out/" + hip_name + "/" + job_name
        job_configuration.file_name_format      = job_name + "_{frame_number}"




# seq_asset = unreal.load_asset(seq_asset_path)

# outliner           = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
# selection          = outliner.get_selected_level_actors()
# print(selection[0].root_component)
# asset_tools     = unreal.AssetToolsHelpers.get_asset_tools()
# soft_references = asset_tools.find_soft_references_to_object(job.map)
# print (soft_references)
# print(job.shot_info)


# seq_asset.component_tags = ["AHOJ"]
# asset_seq    = unreal.load_asset("/Game/x/abc_text/abc_text_SEQ.abc_text_SEQ")
# /Script/Engine.World'/Game/x/abc_text/abc_text_LEV.abc_text_LEV'

# world       = unreal.EditorLevelLibrary.get_editor_world()
# actor_class = unreal.load_asset("/Game/x/abc_text/abc_text_SEQ.abc_text_SEQ")
# actors      = unreal.GameplayStatics.get_all_actors_of_class(world, actor_class)
def RenderQueue_InPlace(self , sm1_picture_name):
        print("[sequence camera]: render sequence to movie")
        subsystem = unreal.get_editor_subsystem(unreal.MoviePipelineQueueSubsystem)
        pipelineQueue = subsystem.get_queue()
        # pipelineQueue = unreal.new_object(unreal.MoviePipelineQueue)
        job_num = len(pipelineQueue.get_jobs())
        print("[sequence camera]: job_num: "+ str(job_num))
        job_arr = pipelineQueue.get_jobs()
        print("[sequence camera]: job_arr: "+ str(job_arr))
        #
         while(job_num != 0):
            pipelineQueue.delete_job(job_arr[job_num-1])
            job_num = job_num - 1
        newJob = pipelineQueue.allocate_new_job(unreal.MoviePipelineExecutorJob)
        newJob.sequence = unreal.SoftObjectPath(sequence_asset_path)
        newJob.map = unreal.SoftObjectPath(map_path)
        newJob.job_name = str("My_Sequence")
        unreal.log("Validating job " + str(newJob))
        print("[sequence camera]: set a job")
        outputSetting = newJob.get_configuration().find_or_add_setting_by_class(unreal.MoviePipelineOutputSetting)
        outputSetting.output_resolution = unreal.IntPoint(1024,1024)
        outputSetting.file_name_format = sm1_picture_name
         outputSetting.output_directory = unreal.DirectoryPath(Capture_path)
        # alpha:
        renderPass = newJob.get_configuration().find_or_add_setting_by_class(unreal.MoviePipelineDeferredPassBase)
        renderPass.accumulator_includes_alpha = True
        newJob.get_configuration().find_or_add_setting_by_class(unreal.MoviePipelineImageSequenceOutput_PNG)
        newJob.get_configuration().initialize_transient_settings()
        #
         global NewExecutor
        NewExecutor = subsystem.render_queue_with_executor(unreal.MoviePipelinePIEExecutor)
        NewExecutor.on_executor_finished_delegate.add_callable_unique(OnQueueFinishedCallback)
        NewExecutor.on_individual_job_finished_delegate.add_callable_unique(OnIndividualJobFinishedCallback)

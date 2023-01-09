
def hou_create_levels(name) :
   
    save_to_folder = "Q:\uni"

    filename_job = hou.expandString("JOB")
    filename_job = filename_job.split(".")[1]

    for geo in hou.selectedNodes() :

        # -------------------
        # filename
        filename_level = geo
        filename       = "render" +  filename_job + "." + filename_level

        # -------------------
        # path

        # -------------------
        # create file
        path_shelf = hou.getenv("wf_path") + "/toolbar/wf_vex.shelf"
        file_shelf = open( path_shelf, 'w')
        file_shelf.write("item")
        file_shelf.close()

    

import os
import glob
from pgeo.utils.filesystem import get_filename
import shutil
import subprocess
from playground.data_processing.processing import process_layers


process_layer_parameters_3857 = {
    "gdalwarp" : {
        "-overwrite" : "",
        "-multi" : "",
        "-of" : "GTiff",
        "-s_srs" :"EPSG:32629",
        "-t_srs": "EPSG:3857",
        "-srcnodata" : "0",
        "-dstnodata" : "0"
    },
    "gdaladdo" : {
        "parameters" : {
        },
        "overviews_levels" : "2 4 8 16"
    }
}


def process(input_folder, output_folder, process_layer_parameters):
    print "Processing data %s %s %s ", input_folder, output_folder, process_layer_parameters

    if os.path.isdir(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    try:
        input_files = glob.glob(input_folder +"/*.tif")
        for input_file in input_files:
            print input_file

            output_filename = output_folder + "/" + get_filename(input_file) + ".tif"
            print(output_filename)

            # create a geotiff + overviews
            process_layers(input_file, output_filename, process_layer_parameters)

    except Exception, e:
        print e
        pass

input_base_path = "/home/vortex/Desktop/LAYERS/MOROCCO_MICHELA/to_publish/original/"
output_base_path = "/home/vortex/Desktop/LAYERS/MOROCCO_MICHELA/to_publish/3857/"

path = "wheat_seasonal"

input_folder = input_base_path + path
output_folder = output_base_path + path

process(input_folder, output_folder, process_layer_parameters_3857)
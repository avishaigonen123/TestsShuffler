import os

from blender.Logicalscripts.exportPng import output_directory


def test_export_png_output_directory(tests_data_dir):
    pathRoot = os.path.join(tests_data_dir, 'imagesquestion_1.png')
    answersId = ['שאלה מספר', 'א.', 'ב.', 'A']
    output_directory_path = 'blender/images'

    _ = output_directory(pathRoot, answersId, output_directory_path)

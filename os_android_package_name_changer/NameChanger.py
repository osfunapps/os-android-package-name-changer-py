import os
import shutil
import xml.etree.ElementTree as ET
import ostools.FileHandler as fh
import ostools.LoggerHandler as lh


###########################################################################
#
# this module meant to substitute old android package name with a new one
#   Arguments:
#   1) android project path (String)
#   2) new package name (String)
#
###########################################################################


def get_package_name(path):
    android_manifest_file = path + "/app/src/main/AndroidManifest.xml"
    tree = ET.parse(android_manifest_file)
    root = tree.getroot()
    return root.attrib['package']


def change_package_name(path_to_project, old_package_name, new_package_name):
    # run on all of the files and replace all occurrences of old_package_name with new_package_name
    for dname, dirs, files in os.walk(path_to_project):
        for fname in files:
            fpath = os.path.join(dname, fname)
            try:
                with open(fpath) as f:
                    s = f.read()

                s = s.replace(old_package_name, new_package_name)
                with open(fpath, "w") as f:
                    f.write(s)
            except:
                pass

    # clear caches
    gradle_path = path_to_project + "/.gradle"
    if os.path.exists(gradle_path):
        shutil.rmtree(gradle_path)


def check_write_permission(path_to_project):
    # check if necessary files are writable
    for dname, dirs, files in os.walk(path_to_project):
        if '.git' in dname:
            continue
        for fname in files:
            fpath = os.path.join(dname, fname)
            if not fh.is_file_write_permission_granted(fpath):
                raise Exception("ERROR: To change the package name, you need to allow write permission to: " + fpath)


def change_inner_folders_names(path, old_package_name, new_package_name):
    # get the dirs names of inner folders inside the main and tests
    new_package_name = new_package_name.split(".")
    first_new_word = new_package_name[1]
    second_new_word = new_package_name[2]

    old_package_name = old_package_name.split(".")
    first_old_word = old_package_name[1]
    second_old_word = old_package_name[2]

    # change the two inner folders in the main dir
    if fh.is_dir_exists(path + "/app/src/main/java/com/" + first_old_word + "/" + second_old_word):
        shutil.move(path + "/app/src/main/java/com/" + first_old_word + "/" + second_old_word, path + "/app/src/main/java/com/" + first_old_word + "/" + second_new_word)
        shutil.move(path + "/app/src/main/java/com/" + first_old_word, path + "/app/src/main/java/com/" + first_new_word)

    # change the two inner folders in the test dir
    if fh.is_dir_exists(path + "/app/src/test/java/com/" + first_old_word + "/" + second_old_word):
        shutil.move(path + "/app/src/test/java/com/" + first_old_word + "/" + second_old_word, path + "/app/src/test/java/com/" + first_old_word + "/" + second_new_word)
        shutil.move(path + "/app/src/test/java/com/" + first_old_word, path + "/app/src/test/java/com/" + first_new_word)

    # change the two inner folders in the android test dir
    if fh.is_dir_exists(path + "/app/src/androidTest/java/com/" + first_old_word + "/" + second_old_word):
        shutil.move(path + "/app/src/androidTest/java/com/" + first_old_word + "/" + second_old_word, path + "/app/src/androidTest/java/com/" + first_old_word + "/" + second_new_word)
        shutil.move(path + "/app/src/androidTest/java/com/" + first_old_word, path + "/app/src/androidTest/java/com/" + first_new_word)


def run(project_path, new_package_name):
    # setup the logger
    logger = lh.Logger(__file__)

    # the path to the android project
    # project_path = sys.argv[1]

    # the desired package name
    # new_package_name = sys.argv[2]

    # get the old package name
    old_package_name = get_package_name(project_path)

    logger.info("checking write permission in directory")
    # check if write permission granted
    check_write_permission(project_path)

    logger.info("changing package name")
    # change the package name
    change_package_name(project_path, old_package_name, new_package_name)

    logger.info("changing 3 inner dirs (inside src/main)")
    # change the 3 inner folders inside the src/main (/GeneralRemote/app/src/main/java/com/first/second)
    change_inner_folders_names(project_path, old_package_name, new_package_name)

    logger.info("done!")

import os
import os_tools.FileHandler as fh
import os_tools.LoggerHandler as lh
import os_tools.XmlFileHandler as xh
import os_android_package_name_changer.NameChangerBp as bp
###########################################################################
#
# this module meant to substitute old android package name with a new one
#   Arguments:
#   1) android project path (String)
#   2) new package name (String)
#
###########################################################################


def change_package_name(project_path, new_package_name):
    # setup the logger
    logger = lh.Logger(__file__)

    # get the old package name
    old_package_name = get_package_name(project_path)

    logger.info("checking write permission in directory")
    # check if write permission granted
    bp.check_write_permission(project_path)

    logger.info("changing package name")
    # change the package name
    bp.change_package_name(project_path, old_package_name, new_package_name)

    logger.info("changing 3 inner dirs (inside src/main)")
    # change the 3 inner folders inside the src/main (/GeneralRemote/app/src/main/java/com/first/second)
    bp.change_inner_folders_names(project_path, old_package_name, new_package_name)

    logger.info("done!")


# will return a package name from a given project
def get_package_name(project_path):
    app_dir = os.path.join(project_path, 'app')
    android_manifest_file = fh.search_files(app_dir, 'AndroidManifest.xml')[0]
    android_manifest_file_xml = xh.read_xml_file(android_manifest_file)
    root_node = xh.get_root_node(android_manifest_file_xml)
    package_name = xh.get_node_att(root_node, 'package')
    return package_name


def main_entry():
    print("Starting the local workspace sync")
    return 0


def read_config():
    return True


def list_files_to_backup(root_folder, backup_folder):
    print("Going to get the list of files to backup in the folder - " + root_folder)
    print(
        "Preparing the list based on the existing contents in backup folder - "
        + backup_folder
    )
    return list()


def backup_files(files_to_backup):
    print("Going to backup these files - " + str(files_to_backup))
    return True

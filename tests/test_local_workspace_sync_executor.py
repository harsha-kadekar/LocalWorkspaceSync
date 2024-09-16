import local_workspace_sync.local_workspace_sync_executor


class TestLocalWorkspaceSyncExecutor:

    def test_main_entry(self):
        return_value = local_workspace_sync.local_workspace_sync_executor.main_entry()
        assert return_value == 0

    def test_read_config(self):
        return_value = local_workspace_sync.local_workspace_sync_executor.read_config()
        assert return_value

    def test_list_files_to_backup(self):
        return_value = local_workspace_sync.local_workspace_sync_executor.list_files_to_backup("/tmp/test", "/tmp/destination")
        assert len(return_value) == 0

    def test_backup_files(self):
        return_value = local_workspace_sync.local_workspace_sync_executor.backup_files(list())
        assert return_value

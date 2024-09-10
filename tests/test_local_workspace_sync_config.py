import local_workspace_sync.local_workspace_sync_config

class TestLocalWorkspaceSyncConfig:
    def test_main_entry(self):
        return_value = local_workspace_sync.local_workspace_sync_config.main_entry()
        assert return_value == 0

    def test_create_config_file(self):
        return_value = local_workspace_sync.local_workspace_sync_config.create_config_file()
        assert return_value == 0

    def test_update_config_file(self):
        return_value = local_workspace_sync.local_workspace_sync_config.update_config_file()
        assert return_value == 0

    def test_schedule_cron_job(self):
        return_value = local_workspace_sync.local_workspace_sync_config.schedule_cron_job()
        assert return_value == 0


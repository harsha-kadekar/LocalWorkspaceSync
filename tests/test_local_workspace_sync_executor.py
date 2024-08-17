import local_workspace_sync.local_workspace_sync_executor
from local_workspace_sync import main


class TestLocalWorkspaceSyncExecutor:
    def test_add_numbers(self):
        value = main.add_numbers(10, 20)
        assert value == 30

    def test_main_entry(self):
        return_value = local_workspace_sync.local_workspace_sync_executor.main_entry()
        assert return_value == 0

from local_workspace_sync import main


class TestLocalWorkspaceSyncExecutor:
    def test_add_numbers(self):
        value = main.add_numbers(10, 20)
        assert value == 30

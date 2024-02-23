import unittest
from local_workspace_sync import local_workspace_sync_executor


class LocalWorkspaceSyncExecutorTest(unittest.TestCase):

    def test_add_numbers(self):
        value = local_workspace_sync_executor.add_numbers(10, 20)
        self.assertEquals(value, 30)

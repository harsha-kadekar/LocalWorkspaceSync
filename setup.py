from setuptools import setup

setup(
    name='LocalWorkspaceSync',
    version='0.0.1',
    packages=['local_workspace_sync'],
    package_dir={'': 'tests'},
    url='https://github.com/harsha-kadekar/LocalWorkspaceSync',
    license='MIT License',
    author='Anuradha and Harsha',
    author_email='anuradha.k.satish@gmail.com',
    description='A package to sync your workspace to local folder',
    entry_points={
        'console_scripts': [
            'local_workspace_sync_executor = local_workspace_sync:hello_world'
        ]
    }
)

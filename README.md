# LocalWorkspaceSync

[![CI](https://github.com/harsha-kadekar/LocalWorkspaceSync/actions/workflows/python-package.yml/badge.svg)](https://github.com/harsha-kadekar/LocalWorkspaceSync/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/harsha-kadekar/LocalWorkspaceSync/graph/badge.svg?token=47UR4XM9T6)](https://codecov.io/gh/harsha-kadekar/LocalWorkspaceSync)

This is a small tool which will sync the contents of source folders to a destination folder.
This is one directional syncer.


## Development


This is a project written in python. You need have python3, pip3 and virtualenv installed in your system.


For the development purpose use `1-integrate-code-cov` git branch. The commands to get to the branch.

```
# To clone the repo to your machine

git clone https://github.com/harsha-kadekar/LocalWorkspaceSync.git

cd LocalWorkspaceSync

# To checkout 1-integrate-code-cov branch

git checkout 1-integrate-code-cov
```

Once you have done your code changes, do these following steps to prepare for pushing the change to remote repository.

- You will be executing below commands in the virtual environment. To create the virtual environment - 

```
# To create a virtual environment
virtualenv venv

# To start the virtual environment
source venv/bin/activate
```

- Install the necessary dependencies

```
pip install pytest ruff coverage bandit
```


- To run the unit tests

```
pytest tests
```

- To run the code coverage and its report generation. We have set 95% code coverage target.

```
coverage run

coverage report
```

- To format your code

```
ruff format
```

- To run the linter

```
ruff check
```

- To run the security check

```
bandit -r local_workspace_sync
```

- To build the wheel and create the executables of the project i.e. `local-workspace-sync-executor` (the executable will be in location ./venv/bin)

```
pip install .

cd venv/bin

./local-workspace-sync-executable
```


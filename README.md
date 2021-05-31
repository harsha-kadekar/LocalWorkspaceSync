# LocalWorkspaceSync

This is a small tool which will sync the contents of source folders to a destination folder.
This is an one directional syncer.

This will read the configuration from a `$HOME/.config/localworkspacesync/workspaces.config` file.
Simple configuration is a json file - 

```
{
	"destinationLocation": "/myexternaldirve/folderlocation",
	"sourceLocations": [
				{
					"rootDirectory": "/mysourcecode/location",
					"excludeFiles": ["*.txt", ".history"],
					"excludeDirectories": ["build"]
				}
			   ]
}
```

## Install

As part of installation, this will create the configuration file as well as the cron job necessary to execute it.
Git clone this repository, followed by execute the `installapp.sh`. As part of the installation, it will ask for the
time of the day when this script needs to be run as part of cron job.

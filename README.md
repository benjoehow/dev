# dev

This git holds the neccessary code I use to set up minimal development environments.

## Setup

## Initializing the enviornment
[Running setup.sh](setup.sh) makes **local** and **gits** folders. The [.gitignore](.gitignore) file will prevent the contents of these folders from being commited to this git.
- **local** is meant to hold data, scratchpad code, etc..
- **gits** contains other repositories

### Launching the environment 
Running `docker compose up` will launch a jupytr lab development environment with access to the **local** and **gits** folders.


## Dockerfile
The [dockerfile](dockerfile) has three stages:
1. **pybuild** installs a specific python version and other base packages such as gcc
2. **pyprod** builds off of pybuild and installs the python packages specified in [requirements.txt](requirements.txt)
3. **pydev** builds off of pyprod and layers a [jupytr lab](https://jupyter.org/) instance on top of it.

The reasoning for **pyprod** is that package needs may change frequently compared to what is being installed in **pybuild**.

If deploying a container as a web app, the idea is that only **pyprod** is needed as the jupytr lab instance can add a lot of memory requirements to the container.

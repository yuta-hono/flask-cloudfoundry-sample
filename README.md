# Cloud Foundry sample application for Flask
## About this application
This is a sample application to deploy Flask application for Cloud Foundry (CF).

## Environment to run
- Cloud Foundry (Diego) or the version which Buildpack available

## How to run

1. Make sure that you have already logged into CF with [cf_cli](http://docs.cloudfoundry.org/cf-cli/install-go-cli.html "Installing the cf Command Line Interface").
2. Run `$ cf push <yourapp> -b https://github.com/cloudfoundry/python-buildpack`
3. Go to your application URL. `http://yourapp.example.com/` just shows "Hello world", and `http://yourapp.example.com/vars` shows the available environment variables on CF

## Files

### Files to declare runtime envinronment

#### requirements.txt
Pip requirements, this automatically satisfied by CF in a staging phase.

#### runtime.txt
The file specifies Python version to run this application by CF.
See more details at [Python Buildpack](https://docs.cloudfoundry.org/buildpacks/python/index.html "Python Buildpack").

#### manifest.yml
The file specifies about the specs of instance (memory/disk quota, etc).

#### Procfile
The file specify what commands run the application.
This also can specified in a deploy command with `-c` option.
For more details, see at [Binary Buildpack](http://docs.cloudfoundry.org/buildpacks/binary/index.html "Binary Buildpack").

### Web application files

#### hello.py , templates/*
The simple Flask application run on CF.
Important things here are:

- App `host` requires to be set as "0.0.0.0"
  - CF routes the traffic from external in the router, and since all the component is scalable, CF can not restrict the access with source IPs 
- App `port` requires to be set with dynamic value comes from CF envinronmental value
  - Since the port is dynamic value, an application can not specify a static port number. This port number requires to be set with dynamic value also

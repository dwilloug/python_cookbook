# Flask with RESTful interface

This application is the skeleton of an app that I built to manage support agent to ticket connection automation.

As it stands, this application is a minimal initial reconstruction that shows how I build REST API applications in python. Most of the cool parts of this application have been removed and much of the CRUD operations have been left out. The idea is not to provde a full recreation of the original application, but just enough to kickstart a new API in Flask with my preferences.

## Some Considerations

This application is designed for cloud deployments and is designed to fail fast rather than attempt remediation. As an example, without a Postgres DB setup configured and running this application will react as if the new image is experiencing a network failure and exit. The design goal here is to prevent a malformed configuration from being push to the deployment environment that might take the application out of service. Obviously this isn't the ideal scenario for every configuration but it is the target behavior for this app setup.
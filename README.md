# Medical Appointment
This is the document that guide you to install the app.

Check if you have a Docker in your machine. If don't, please install [Docker Engine](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/).

Check if you have a Git in your machine. If don't, please install [Git](https://git-scm.com/downloads).

## Run application
1. First, clone this repository into your local machine:
`git clone git@github.com:medical-appointment/fernando_chimicoviaki.git`
2. Run `make execute` to build and run the application
3. Go! :rocket:

PS: The file `api.env` is for environment values from the application. The default values corresponds to host/port of application and the database pre defined values.

## Test API
You can test the API by [Swagger Documentation](http://localhost:8000/medical-api-docs). This link will works when you run application.

## `Makefile` tips
* `make execute` - This command will execute the following commands:
	* `sudo chown -R $(USER):$(USER) .` - Attribute permisions to this directory for manipulating files of project.
	* `clean` - Clean useless files in the project structure.
	* `stoppsql` - This command will stop the PostgreSQL if it runs in your machine.
	* `build` - It will be build the project container.
	* `startd` - This command will execute the container in background.
* `start` - This command will execute the container and exhibit logs.
* `stop` - This command will stop the container.
* `make html` - This command will generate a HTML report from Coverage.

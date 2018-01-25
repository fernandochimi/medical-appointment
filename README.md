# Medical Appointment
This is the document that guide you to install the app.

Check if you have a Docker in your machine. If don't, please install [Docker Engine](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/).

Check if you have a Git in your machine. If don't, please install [Git](https://git-scm.com/downloads).

## Run application
1. First, clone this repository into your local machine:
`git clone git@github.com:medical-appointment/fernando_chimicoviaki.git`
2. Run `make execute to build and run the application
3. In your browser, access `http://localhost:8000` to see the project

## `Makefile` tips
* `make execute` - This command will execute the following commands:
	* `sudo chown -R $(USER):$(USER) .` - Attribute permisions to this directory for manipulating files of project.
	* `clean` - Clean useless files in the project structure.
	* `build` - It will be build the project container.
	* `start` - This command will execute the container in background.
	* `test` - This command will check if exist a errors in the project.
	* `report` - This command will generate a report from test.
* `make html` - This command will generate a HTML report from Coverage.

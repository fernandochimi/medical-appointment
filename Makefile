PROJECT_ID := medical-appointment
DCMP = docker-compose

build:
		${DCMP} build

start:
		${DCMP} up

startd:
		${DCMP} up -d

stoppsql:
		sudo service postgresql stop

stop:
		${DCMP} stop

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

execute:
		sudo chown -R $(USER):$(USER) .
		${MAKE} stoppsql
		${MAKE} clean
		${MAKE} build
		${MAKE} startd

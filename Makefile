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
		find . -name "__pycache__" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

execute:
		sudo chown -R $(USER):$(USER) .
		${MAKE} stoppsql
		${MAKE} clean
		${MAKE} build
		${MAKE} startd

html:
		${DCMP} -p $(PROJECT_ID) run web coverage html
		# Uncomment open ... if you use Mac
		# open htmlcov/index.html
		xdg-open htmlcov/index.html

PROJECT_ID := medical_appointment
DCMP = docker-compose

build:
		${DCMP} build

start:
		${DCMP} up -d

stop:
		${DCMP} stop

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

test:
		${DCMP} -p $(PROJECT_ID) run web coverage run \
			--source="src" \
			--omit="../../**migrations**, ../../**tests**" \
			--failfast

report:
		${DCMP} -p $(PROJECT_ID) run web coverage report -m

execute:
		sudo chown -R $(USER):$(USER) .
		${MAKE} clean
		${MAKE} build
		${MAKE} start
		${MAKE} test
		${MAKE} report

html:
		${DCMP} -p $(PROJECT_ID) run web coverage html
		# Uncomment open ... if you use Mac
		# open htmlcov/index.html
		xdg-open htmlcov/index.html

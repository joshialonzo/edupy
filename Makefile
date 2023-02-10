all:
	$(error please pick a target)

env:
	# Create venv directory if not exist
	test -d venv || python3.10 -m venv venv
	./venv/bin/python -m pip install --upgrade pip	
	./venv/bin/python -m pip install -r requirements.txt

dev-env: env
	./venv/bin/python -m pip install -r requirements-dev.txt

test:
	find . -name '*.pyc' -exec rm -f {} \;
	./venv/bin/flake8 edu tests
	./venv/bin/ruff edu tests
	./venv/bin/isort edu tests
	./venv/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    edu tests

package:
	python setup.py sdist

clean:
	rm -rf build dist edu.egg-info

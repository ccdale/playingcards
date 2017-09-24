test:
	python -xm unittest discover

clean:
	rm -f *.pyc

local:
	pip install -e ./ --user

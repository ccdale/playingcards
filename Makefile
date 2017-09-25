scripts=setup.py playingcards.py

all: clean local test

test:
	python3 -xm unittest discover

clean:
	rm -f *.pyc
	rm -rf dist/

local:$(scripts)
	pip3 install -e ./ --user


dist:$(scripts)
	python3 setup.py sdist

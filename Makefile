scripts=setup.py playingcards.py

all: clean local test dist

test:
	python -xm unittest discover

clean:
	rm -f *.pyc

local:$(scripts)
	pip install -e ./ --user


dist:$(scripts)
	python setup.py sdist

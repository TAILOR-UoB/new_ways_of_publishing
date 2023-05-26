install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e lib/data-science-python/

build:
	jupyter-book build booksource

clean:
	jupyter-book clean booksource

cleanbuild: clean build

buildbook:
	jupyter-book build booksource/ --builder pdfhtml

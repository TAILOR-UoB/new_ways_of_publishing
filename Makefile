install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e lib/book-python/

install-r:
	./install_irkernel.r

create-kernel:
	pip install ipykernel
	python -m ipykernel install --user --name data-science

build:
	jupyter-book build booksource

clean:
	jupyter-book clean booksource

clean-build: clean build

build-pdf:
	jupyter-book build booksource/ --builder pdfhtml
	cp booksource/_build/pdf/book.pdf booksource/assets/documents/nwop_book.pdf

serve:
	python -m http.server 9000 -d booksource/_build/html/

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e lib/book-python/

install_r:
	./install_irkernel.r

build:
	jupyter-book build booksource

clean:
	jupyter-book clean booksource

cleanbuild: clean build

buildbook:
	jupyter-book build booksource/ --builder pdfhtml
	cp booksource/_build/pdf/book.pdf booksource/assets/documents/nwop_book.pdf

serve:
	python -m http.server 9000 -d booksource/_build/html/

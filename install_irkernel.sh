#!/bin/bash

mkdir -p R_libs
Rscript -e "install.packages('IRkernel', lib='R_libs/')" \
        -e "IRkernel::installspec()"

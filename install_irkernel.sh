#!/bin/bash

mkdir -p R_libs
Rscript -e "install.packages('IRkernel', lib='R_libs/')"
Rscript -e "IRkernel::installspec()"

#!bin/bash/
set -e

#formating code
echo "formatting code using black"
poetry run black .


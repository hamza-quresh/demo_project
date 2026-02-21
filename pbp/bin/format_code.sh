#!bin/bash/
#build wheel.sh file that simply executes poetry build
set -e
set o

#formating code
echo "formatting code using black"
poetry run black .


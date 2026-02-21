#!bin/bash/
#build wheel.sh file that simply executes poetry build
set -e
set o


echo "cleaning dist folder"
rm -rf dist

#build wheel
echo "starting build wheel.sh and executing poetry build"
poetry build

echo "build wheel.sh completed successfully"
ls dist/*.whl
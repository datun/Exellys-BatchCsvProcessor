#!/bin/bash

apt-get update
if ![ which python ]
then
	echo Python installation not found, installing.
	apt-get install python
else
	echo Python installation is found!
fi

if ![ which pip ]
then
	echo pip installation is not found, installing.
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py
	rm -f get-pip.py
else
	echo pip installation was found! Updating pip!
	python -m pip install --upgrade pip
fi

echo Installing Numpy!
pip install numpy
echo Installing Pandas!
pip install pandas

read -rsp $'Press any key to continue...\n' -n1 key

@echo off


:start 
cls

if not where python(
	echo Python is not installed or it is not defined in Windows PATH
	echo Please install Python through this link: https://www.python.org/
	echo or repair the python installation to include Windows Path

	echo Press any key to exit...
	pause
	exit
)else(
	echo Python is found, checking if pip is installed!
	if not where pip(
		echo Pip is not installed, installing pip!
		curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
		python get-pip.py
		del "get-pip.py"
		setx PATH “%PATH%; %HOME%\pip\pip.ini
	)
)


echo Installing numpy
pip install numpy

echo Installing pandas
pip install pandas

echo Press any key to exit...
pause
exit

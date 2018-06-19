SET PYTHON=c:\tools\Python36\python.exe

IF EXIST ".venv" (
    rmdir /q /s .venv
)

%PYTHON% -m venv .venv

IF NOT EXIST ".venv" (
	echo Python virtual environment faild to create.
	pause
	exit 1
)

call .venv\scripts\activate.bat

pip install pyaudio
pip install pyserial
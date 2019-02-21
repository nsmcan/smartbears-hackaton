@echo off
::: Launch a Python script in the project's virtual environment

::: Name of the virtual environment
set py_venv=venv

setlocal enabledelayedexpansion

::: Splitting the first argument from the rest, preserving quotes in the arguments if any
::: https://stackoverflow.com/a/49040793/9921853
set therest=;;;;;%*
set therest=!therest:;;;;;%1=!

::: Activate the virtual environment
call %~dp0%py_venv%\Scripts\activate
::: Execute the python script with its arguments
python %1 %therest%

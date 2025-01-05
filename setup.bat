@echo off
REM Configuración
echo Instalando dependencias.
pip install -r requirements.txt

echo Configurando...
setx PATH "%~dp0;%PATH%"

echo Terminado.
pause

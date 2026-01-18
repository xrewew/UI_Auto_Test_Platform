@echo off
chcp 65001 >nul

:menu
cls
echo =====================================
echo        Pytest 测试运行器
echo =====================================
echo.
echo 1. 运行 login 和 hcc 标记的测试
echo 2. login 标记的测试
echo 3. hcc 标记的测试
echo 4. 所有测试
echo 5. 退出
echo.

getchoice:
set choice=
set /p choice=请输入您的选择 (1-5):

if "%choice%"=="1" goto run1
if "%choice%"=="2" goto run2
if "%choice%"=="3" goto run3
if "%choice%"=="4" goto run4
if "%choice%"=="5" goto exit

echo 无效的选择，请重新输入！
echo.
goto getchoice

:run1
echo 正在运行 login 和 hcc 标记的测试...
echo.
pytest -sv test_mark.py -m "login and hcc"
echo.
pause
goto menu

:run2
echo 正在运行所有 login 标记的测试...
echo.
pytest -sv test_mark.py -m login
echo.
pause
goto menu

:run3
echo 正在运行所有 hcc 标记的测试...
echo.
pytest -sv test_mark.py -m hcc
echo.
pause
goto menu

:run4
echo 正在运行所有测试...
echo.
pytest -sv test_mark.py
echo.
pause
goto menu

:exit
echo 感谢使用测试运行器！
echo.
pause
exit
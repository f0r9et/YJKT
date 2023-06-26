@echo off

echo off
rem RunP.bat
rem 同時並行執行多個程式
set cmd1=call me
set cmd2=call they
start %cmd1%
start %cmd2%
start http://localhost:8000/yj.html
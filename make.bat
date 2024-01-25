@echo off

if "%1" == "build" (
    flit build
    goto end
)

if "%1" == "doc" (
    call pandoc --from=markdown --to=rst --output=README.rst README.md
    call .\doc\source\make.bat html
    goto end
)

:help
echo 사용 가능한 명령:
echo   make build - build with flit
echo   make doc   - build doc with sphinx
goto end

:end

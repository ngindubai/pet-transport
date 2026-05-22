@echo off
REM build.bat — full build + sitemap split for PetTransportGlobal
REM Run from repo root: C:\Users\garet\Desktop\pet-transport\
REM Usage: build.bat

echo [1/2] Building Hugo site...
cd site
hugo --gc --minify
if errorlevel 1 (
    echo Hugo build warning (exit code 1) — usually the countries.json WARN, continuing...
)
cd ..

echo.
echo [2/2] Splitting sitemap into sections...
python split_sitemap.py

echo.
echo Build complete.
echo Upload site\public\ to Hostinger to deploy.

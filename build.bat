@echo off
REM build.bat — full build + sitemap split for PetTransportGlobal
REM Run from repo root: C:\Users\garet\Desktop\pet-transport\
REM Usage: build.bat

echo [1/3] Rebuilding internal link graph...
python rebuild_link_graph_v3.py
if errorlevel 1 (
    echo WARNING: link graph rebuild failed — check output above
)

echo.
echo [2/3] Building Hugo site...
cd site
hugo --gc --minify
if errorlevel 1 (
    echo Hugo build warning (exit code 1) — usually the countries.json WARN, continuing...
)
cd ..

echo.
echo [3/3] Splitting sitemap into sections...
python split_sitemap.py

echo.
echo Build complete.
echo Upload site\public\ to Hostinger to deploy.

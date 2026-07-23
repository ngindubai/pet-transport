@echo off
setlocal

echo [1/5] Validating source...
python scripts\validate_site.py || goto :fail

echo [2/5] Rebuilding internal link graph...
python rebuild_link_graph_v3.py || goto :fail

echo [3/5] Building Hugo site...
hugo --gc --minify --cleanDestinationDir --source site || goto :fail

echo [4/5] Splitting sitemap...
python split_sitemap.py || goto :fail

echo [5/5] Auditing rendered site...
python scripts\audit_build.py || goto :fail

echo Build and quality gates passed. Production deploys only through the live-branch workflow.
exit /b 0

:fail
echo Build failed. Review the error above; no production deployment was made.
exit /b 1

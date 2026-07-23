# PetTransportGlobal — Build Makefile
# Used by build-to-live.yml CI workflow (Linux/macOS)
# Also usable locally: make build

.PHONY: build validate links hugo sitemap audit

build: validate links hugo sitemap audit

validate:
	@echo "[1/5] Validating source..."
	python3 scripts/validate_site.py

links:
	@echo "[2/5] Rebuilding internal link graph..."
	python3 rebuild_link_graph_v3.py

hugo:
	@echo "[3/5] Building Hugo site..."
	hugo --gc --minify --cleanDestinationDir --source site

sitemap:
	@echo "[4/5] Splitting sitemap..."
	python3 split_sitemap.py

audit:
	@echo "[5/5] Auditing rendered site..."
	python3 scripts/audit_build.py

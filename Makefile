# PetTransportGlobal — Build Makefile
# Used by build-to-live.yml CI workflow (Linux/macOS)
# Also usable locally: make build

.PHONY: build links hugo sitemap

build: links hugo sitemap

links:
	@echo "[1/3] Rebuilding internal link graph..."
	python3 rebuild_link_graph_v3.py

hugo:
	@echo "[2/3] Building Hugo site..."
	cd site && hugo --gc --minify

sitemap:
	@echo "[3/3] Splitting sitemap..."
	python3 split_sitemap.py

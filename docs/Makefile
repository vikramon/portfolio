# Minimal Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = bdm_porfolio
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help clean html

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clean:
	@rm -rf "$(BUILDDIR)"/*

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)


deploy: html 
	@echo "Deploying to GitHub Pages..."
	@ghp-import -n -p -f $(BUILDDIR)/html
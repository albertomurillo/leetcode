CC := gcc
CLANGFORMAT := clang-format

SOURCEDIR = src
BUILDDIR = build
SOURCES := $(wildcard $(SOURCEDIR)/*.c)
TEST_SOURCES := $(wildcard $(SOURCEDIR)/*_test.c)
TEST_BINARIES := $(patsubst $(SOURCEDIR)/%.c, $(BUILDDIR)/%.bin, $(TEST_SOURCES))

.PHONY: all format test clean

all: format test

format: $(SOURCES)
	@$(CLANGFORMAT) -i $(SOURCES)

test: $(TEST_BINARIES)

$(BUILDDIR)/%.bin: $(BUILDDIR) $(SOURCEDIR)/%.c
	@$(CC) $(SOURCEDIR)/$*.c -o $@
	./$@

$(BUILDDIR):
	@mkdir -p $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)

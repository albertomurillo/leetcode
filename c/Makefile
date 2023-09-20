CC := gcc
CFLAGS := --coverage -g -O0
CLANGFORMAT := clang-format

SOURCEDIR := src
BUILDDIR := build
SOURCES := $(wildcard $(SOURCEDIR)/*.c)
TEST_SOURCES := $(wildcard $(SOURCEDIR)/*_test.c)
TEST_BINARIES := $(patsubst $(SOURCEDIR)/%.c, $(BUILDDIR)/%.bin, $(TEST_SOURCES))

COVDIR := htmlcov

.PHONY: all format test clean

all: format test

format: $(SOURCES)
	@$(CLANGFORMAT) -i $(SOURCES)

test: $(TEST_BINARIES)
	gcovr

coverage: test $(COVDIR)
	gcovr -r . --html --html-details -o htmlcov/index.html
	open htmlcov/index.html

$(BUILDDIR)/%.bin: $(BUILDDIR) $(SOURCEDIR)/%.c
	$(CC) $(CFLAGS) $(SOURCEDIR)/$*.c -o $@
	@./$@

$(BUILDDIR):
	@mkdir -p $(BUILDDIR)

$(COVDIR):
	@mkdir -p $(COVDIR)

clean:
	rm -rf $(BUILDDIR) $(COVDIR) *.gcda *.gcno

ANTLR_VERSION=4.12.0
ANTLR_JAR_NAME=antlr-$(ANTLR_VERSION)-complete.jar
ANTLR_JAR_URL=https://www.antlr.org/download/$(ANTLR_JAR_NAME)
GRAMMAR_FILE=dnf.g4

.PHONY: all 

all: install_antlr build_grammar

install_antlr: 
	@wget -P ./parser $(ANTLR_JAR_URL)

build_grammar:
	go generate ./...


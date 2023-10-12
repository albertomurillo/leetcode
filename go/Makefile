.PHONY: all
all: format test

.PHONY: format
format:
	goimports -w .

.PHONY: lint
lint:
	golangci-lint run

.PHONY: test
test:
	go test -coverprofile=coverage.out ./...
	go tool cover -func coverage.out

.PHONY: coverage
coverage: test
	go tool cover -html=coverage.out

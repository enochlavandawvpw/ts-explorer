.PHONY: build test clean run

build:
	@echo "Building ts-explorer..."
	go build -o bin/ts-explorer ./cmd/...

test:
	go test ./... -v -cover

clean:
	rm -rf bin/ dist/

run: build
	./bin/ts-explorer

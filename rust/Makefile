.PHONY: all format lint test coverage clean
all: format lint test

format:
	find src -name "*.rs" -exec rustfmt {} \;

lint:
	cargo clippy

test:
	cargo test

coverage:
	CARGO_INCREMENTAL=0 RUSTFLAGS='-Cinstrument-coverage' LLVM_PROFILE_FILE='cargo-test-%p-%m.profraw' cargo test
	grcov . --binary-path ./target/debug/deps/ -s . -t html --branch --ignore-not-existing --ignore '../*' --ignore "/*" -o target/coverage
	open target/coverage/html/index.html

clean:
	rm -rf target
	rm -rf *.profraw

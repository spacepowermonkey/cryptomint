clean:
	- rm -rf __pycache__
	- rm -rf output/*

wallets:
	python -m main --currency $(CURRENCY) --count $(COUNT)
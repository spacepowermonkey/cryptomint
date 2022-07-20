clean:
	- rm -rf __pycache__
	- rm -rf output/*

wallets:
	python3 -m main --currency $(CURRENCY) --count $(COUNT)
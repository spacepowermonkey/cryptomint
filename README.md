WARNING: Currently in BETA! Use at your own risk!



# CryptoMint

This is a framework for producing paper crypto-currency products, such as wallets and checks.

![](/docs/cryptobars.jpeg)


## Supported Currencies
Support for different currencies is via the `CURRENCY` environment variable.

Symbol | Name | Support Wallets?
--- | --- | ---
BTC | Bitcoin | Yes
DOGE | Dogecoin | Yes
ETH | Ethereum | Yes


## Commands
Here's a quick reference guide to commands.

Command | Usage
--- | ---
`make clean` | Deletes everything in the output folder.
`CURRENCY=[SYMBOL] COUNT=[N] make wallets` | Generates N wallets for the chosen currency.

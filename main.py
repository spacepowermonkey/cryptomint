import argparse
import os



from render import render_wallets_to_pdf
from wallets import wallet_from_symbol



def main(symbol, count):
    os.makedirs("output/imgs", exist_ok=True)

    wallets = []
    for i in range(count):
        wallets.append( wallet_from_symbol(symbol) )

    render_wallets_to_pdf(wallets)

    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate paper crypto products')
    parser.add_argument('--currency', dest='cur', metavar='CUR', type=str, help='Set currency of the products.')
    parser.add_argument('--count', dest='count', metavar='N', type=int, help='Set number to produce.')
    args = parser.parse_args()

    main(args.cur, args.count)

import qrcode
import subprocess



def render_qr(data, path):
    qr_obj = qrcode.QRCode(version=1, box_size=10, border=2, error_correction=qrcode.ERROR_CORRECT_H)
    qr_obj.add_data(data)
    qr_obj.make()
    qr_obj.make_image().save(path)
    return




def render_wallets_to_pdf(wallets):
    tex = ''
    with open('form/preamble.txt', 'r') as infile:
        tex += infile.read()

    for wallet in wallets:
        address_qr_path = f"output/imgs/{wallet.name}-address.png"
        secret_qr_path = f"output/imgs/{wallet.name}-secret.png"
        render_qr(wallet.address, address_qr_path)
        render_qr(wallet.secret, secret_qr_path)

        with open('form/note.txt', 'r') as infile:
            note_tex = infile.read()

        secret_in_chunks = ' '.join([wallet.secret[i: i + 8] for i in range(0, len(wallet.secret), 8)])
        address_in_chunks = ' '.join([wallet.address[i: i + 8] for i in range(0, len(wallet.address), 8)])

        note_tex = note_tex.replace('NOTE-NAME-TEXT', wallet.name)
        note_tex = note_tex.replace('CURRENCY-NAME-TEXT', wallet.CURRENCY_NAME)
        note_tex = note_tex.replace('CURRENCY-LOGO-PATH', wallet.LOGO_PATH)
        note_tex = note_tex.replace('PUBKEY-TEXT', address_in_chunks)
        note_tex = note_tex.replace('PUBKEY-QR-PATH', address_qr_path)
        note_tex = note_tex.replace('PRIVKEY-TEXT', secret_in_chunks)
        note_tex = note_tex.replace('PRIVKEY-QR-PATH', secret_qr_path)

        tex += note_tex

    with open('form/closing.txt', 'r') as infile:
        tex += infile.read()


    with open('output/wallets.tex', 'w') as outfile:
        outfile.write(tex)
    
    subprocess.check_call([
        'pdflatex', 
        '-output-directory=output/',
        'output/wallets.tex'
    ])

    return

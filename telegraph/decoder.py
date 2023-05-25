from telegraph.telegraph import Telegraph


def decode():
    t = Telegraph(swap=True)
    return t.decoder

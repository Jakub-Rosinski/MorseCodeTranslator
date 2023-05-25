from telegraph.telegraph import Telegraph


def encode():
    t = Telegraph(swap=False)
    return t.encoder

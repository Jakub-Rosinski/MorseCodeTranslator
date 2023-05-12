from telegraph import Encoder, Decoder


def main() -> None:

    e = Encoder("I'm Kuba and I'm from Poland")
    msg = e.encode()
    print(msg)

    d = Decoder(".. __ / _._ .._ _... ._ / ._ _. _.. / .. __ / .._. ._. ___ __ / .__. ___ ._.. ._ _. _..")
    msg = d.decode()
    print(msg)


if __name__ == '__main__':
    main()

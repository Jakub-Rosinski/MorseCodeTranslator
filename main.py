from translator.translator import Translator
from coding import Encoder, Decoder


def main() -> None:

    e = Encoder("I'm Kuba and I'm from Poland")
    msg = Translator(e)
    print(msg.translate())

    d = Decoder(".. __ / _._ .._ _... ._ / ._ _. _.. / .. __ / .._. ._. ___ __ / .__. ___ ._.. ._ _. _..")
    msg = Translator(d)
    print(msg.translate())


if __name__ == '__main__':
    main()

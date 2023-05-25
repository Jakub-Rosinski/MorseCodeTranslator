import argparse

from translator.translator import Translator
from coding import Encoder, Decoder


def parser():
    parse = argparse.ArgumentParser(prog="Morse Code Translator",
                                    description='Translate Morse Code')
    parse.add_argument("-e",
                       "--encode",
                       type=str,
                       help="encode message")
    parse.add_argument("-d",
                       "--decode",
                       type=str,
                       help="decode message")

    args = parse.parse_args()
    return args


def main() -> None:

    args = parser()
    if text := args.encode:
        e = Encoder(text)
        msg = Translator(e)
        print(f"Original message: {text}")
        print(f"Morse code translation: {msg.translate()}")

    if text := args.decode:
        d = Decoder(text)
        msg = Translator(d)
        print(f"Original message: {text}")
        print(f"Morse code translation: {msg.translate()}")


if __name__ == '__main__':
    main()

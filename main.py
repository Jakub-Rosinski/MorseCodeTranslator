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


def print_original_and_translation(message: str, translation: str) -> None:
    print(f"Original message: {message}")
    print(f"Morse code translation: {translation}")


def encode_message(message: str) -> None:
    e = Encoder(message)
    msg = Translator(e)
    print_original_and_translation(message=message, translation=msg.translate())


def decode_message(message: str) -> None:
    d = Decoder(message)
    msg = Translator(d)
    print_original_and_translation(message=message, translation=msg.translate())


def main() -> None:

    args = parser()

    if text := args.encode:
        encode_message(text)

    if text := args.decode:
        decode_message(text)


if __name__ == '__main__':
    main()

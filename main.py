from telegraph import Telegraph, Encoder


def main() -> None:
    e = Encoder("I'm Kuba and I'm from Poland")
    msg = e.encode()
    print(msg)


if __name__ == '__main__':
    main()

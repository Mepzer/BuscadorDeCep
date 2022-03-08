from screen import build_screen


def main():
    dim = width, height = 500, 500
    app = build_screen(dimension=dim)

    app.init_ui()


if __name__ == '__main__':
    main()

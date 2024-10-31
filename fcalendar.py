import argparse

def main():
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(
        prog="fcalendar",
        description="fcalendar: CLI to manage fictional calendar data"
    )

    # Mensaje de ayuda personalizado para --help
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='fcalendar 1.0',
        help="shows the app version"
    )

    # Parsear los argumentos proporcionados por el usuario
    args = parser.parse_args()

    # Puedes incluir el código que se ejecutará al llamar a fcalendar (opcional)
    print("Welcome to fcalendar. Use '--help' to see the available options.")

if __name__ == "__main__":
    main()

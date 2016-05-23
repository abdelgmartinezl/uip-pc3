from modules.timeutil import minutes, hours, days

if __name__ == "__main__":
    # Ejemplo "Transformar segundos a minutos, horas o dias" muestra el uso simple de Decorator para `type casting`
    # un valor numerico decimal retorna por las operaciones de distintas funciones.

    # Mas sobre Decorator https://docs.python.org/3/library/functools.html?highlight=wraps#functools.wraps
    try:
        _seconds = int(input("Ingrese los segundos a transformar: "))

        if not (_seconds is None or _seconds == ""):
            _minutes = minutes(_seconds)
            _hours = hours(_minutes)
            _days = days(_hours)
            print("\nResultado de %d segundos:\n\tDias(%d) \n\tHoras(%d) \n\tMinutos(%d)" % (
                _seconds,
                _days,
                _hours,
                _minutes
            ))

    except IOError as error:
        print(error)

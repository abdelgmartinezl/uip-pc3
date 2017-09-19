"""
Ej. 28

Autor: Zahir Gudiño
Email: zahir.gudino@gmail.com
Descripcion:
    Demostrar uso sencillo del hilo-individual event loop comunmente empleaod programacion asincronas. Tenga en cuenta
    este un ejemplo muy artificial sólo para demostrar el patrón común. asyncio ofrece muchisimas funcionalidades
    --ej. parallel execution, coroutine cancellation, etc...-- que pertenecen a otros temas.

    Ver (https://docs.python.org/3.6/library/asyncio.html#module-asyncio).
"""
import asyncio


async def ticker(delay, to):
    """Yield numero en rango cero a x, `to`, cada y, `@delay`, segundos"""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def main():
    my_list = []

    print("Async Loop (ejecutando...)")
    # Iterar por cada yield de manera asincrona...
    async for x in ticker(1, 5):
        my_list.append(x)

    print(my_list, "\n")

    print("Async Comprehensions List (ejecutando...)")
    # otra manera, via Async Comprehensions
    print([x async for x in ticker(1, 5)], "\n")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

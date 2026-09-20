# Python Projects 🐍

Este es mi repo para ir guardando los proyectos y ejercicios que voy haciendo
mientras aprendo Python. Todavía es chiquito pero lo voy a ir llenando poco a
poco.

## Proyectos

### Calculadora — [calculate.py](calculate.py)

Mi primera calculadora de consola. Nada muy elaborado, pero ya soporta:

- Suma (`+`), resta (`-`), multiplicación (`*`, `×`, `•`)
- División (`/`, `÷`) y módulo (`%`), ambas protegidas contra división entre cero
- Potencia (`**`, `^`)

También valida que lo que escribas sea un número, no te deja meter un operador
que no reconozca, y te deja encadenar varias operaciones seguidas sin volver a
correr el script (con `1`, `si` o `sí` para seguir).

**Para correrla:**

```bash
python calculate.py
```

**Changelog**

- Quité el `float()` redundante: `numero()` ya devuelve un float, así que
  `num1 = float(numero(...))` pasó a `num1 = numero(...)`.
- Agregué `'sí'` (con acento) a las respuestas para continuar.
- Conecté `%` a la función `zero()`, porque antes `num1 % num2` tronaba con
  `ZeroDivisionError`.
- Bug que introduje con ese cambio: `zero()` siempre hacía `num1 / num2`, sin
  importar el operador. Lo arreglé con un tercer parámetro, `zero(num1, num2, op)`,
  que decide si divide o saca el módulo.

**Qué practiqué:** funciones anidadas, `try/except`, validación de entrada con
`while True`.

### Mazmorra — [mazmorra/mazmorra.py](mazmorra/mazmorra.py)

Un mini juego de exploración en la terminal. Genera un mapa cuadrado
aleatorio (tamaño entre 7x7 y 16x16) con paredes 🧱, cofres 🧰 y casillas
libres, y te pone a mover a tu personaje 😎 con `w`, `a`, `s`, `d` para
recorrerlo. No te deja atravesar paredes ni salirte del mapa.

**Para correrlo:**

```bash
python mazmorra/mazmorra.py
```

**Changelog**

- Versión inicial: mapa aleatorio como matriz y movimiento con `w`, `a`, `s`, `d`.
- Refactor: la generación del mapa ahora vive en `terreno()`, y los 4 bloques
  `if/elif` de movimiento se reemplazaron por diccionarios de direcciones y
  límites.
- Ahora acepta las teclas en mayúscula (`.lower()`).

**Qué practiqué:** matrices (listas de listas), funciones que devuelven varios
valores, diccionarios para quitar código repetido.

**Pendiente:** condición de victoria (por ejemplo, llegar al cofre 🧰).

### Encuentra mi número — [encuentra_mi_numero.py](encuentra_mi_numero.py)

Un juego de adivinar el número. La computadora piensa un número del 0 al 100
y tú le vas atinando; te dice si tu número está abajo o arriba del que pensó
hasta que lo encuentras. Si escribes algo que no es número, te lo vuelve a
pedir, y si te sales del rango 0-100 también te avisa.

**Para correrlo:**

```bash
python encuentra_mi_numero.py
```

**Changelog**

- Versión inicial: número aleatorio del 0 al 100 con pistas de arriba/abajo.
- Agregué un contador de intentos: al ganar te dice en cuántos lo lograste.

**Qué practiqué:** `random`, validación de entrada con `try/except ValueError`,
ciclos con condiciones anidadas.

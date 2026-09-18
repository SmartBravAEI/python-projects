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

## Changelog

- Quité el `float()` redundante — cambié `num1 = float(numero(...))` por
  `num1 = numero(...)`, ya que `numero()` ya devuelve un float.
- Agregué `'sí'` a la condición de continuar — antes solo `'si'` o `'1'`
  seguían el bucle; ahora también acepta la versión con acento.
- Conecté el operador `%` a la función `zero()` — antes `%` calculaba
  `num1 % num2` directo (sin protección), ahora pasa por `zero()` igual que
  la división, para evitar que truene con `ZeroDivisionError`.
- Arreglé el bug que ese cambio introdujo — al conectar `%` a `zero()`,
  la función siempre devolvía `num1 / num2` sin importar el operador. Le
  agregué un tercer parámetro `op` a `zero(num1, num2, op)`, con un
  `if op == "/"` / `else` para que calcule división o módulo según
  corresponda, y actualicé las dos llamadas (`zero(num1, num2, "/")` y
  `zero(num1, num2, '%')`) para pasar el operador correcto.

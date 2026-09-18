# Python Projects

A collection of small Python projects and exercises.

## Projects

### Calculadora ([calculate.py](calculate.py))

A command-line calculator that supports basic arithmetic operations:

- Addition (`+`), subtraction (`-`), multiplication (`*`, `×`, `•`)
- Division (`/`, `÷`) and modulo (`%`), both with divide-by-zero handling
- Exponentiation (`**`, `^`)

It validates numeric input, rejects unsupported operators, and lets the user
chain multiple calculations in a loop (accepts `1`, `si`, or `sí` to continue).

**Run it:**

```bash
python calculate.py
```

## Changelog

- Quitaste el `float()` redundante — cambiaste `num1 = float(numero(...))` por
  `num1 = numero(...)`, ya que `numero()` ya devuelve un float.
- Agregaste `'sí'` a la condición de continuar — antes solo `'si'` o `'1'`
  seguían el bucle; ahora también acepta la versión con acento.
- Conectaste el operador `%` a la función `zero()` — antes `%` calculaba
  `num1 % num2` directo (sin protección), ahora pasa por `zero()` igual que
  la división, para evitar que truene con `ZeroDivisionError`.
- Corregiste el bug que ese cambio introdujo — al conectar `%` a `zero()`,
  la función siempre devolvía `num1 / num2` sin importar el operador. Le
  agregaste un tercer parámetro `op` a `zero(num1, num2, op)`, con un
  `if op == "/"` / `else` para que calcule división o módulo según
  corresponda, y actualizaste las dos llamadas (`zero(num1, num2, "/")` y
  `zero(num1, num2, '%')`) para pasar el operador correcto.

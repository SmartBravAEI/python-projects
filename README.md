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

- Reused the divide-by-zero guard for the modulo operator, removed redundant
  `float()` conversions, and accepted `sí` (with accent) to continue.

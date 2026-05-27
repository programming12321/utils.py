```md
# MyUtils

A custom Python utility library.

Inspired by:
- Python
- JavaScript
- Scratch
- Lua
- TI-BASIC

---

# Installation

```python
import myutils
```

or

```python
from myutils import *
```

---

# String Utilities

## startsWith

```python
startsWith("hello", "he")
```

```python
True
```

---

## endsWith

```python
endsWith("hello", "lo")
```

```python
True
```

---

## reverseString

```python
reverseString("hello")
```

```python
"olleh"
```

---

## toBinary

```python
toBinary(10)
```

```python
"1010"
```

---

## fromBinary

```python
fromBinary("1010")
```

```python
10
```

---

## toHex

```python
toHex(255)
```

```python
"ff"
```

---

## fromHex

```python
fromHex("ff")
```

```python
255
```

---

## removeSpaces

```python
removeSpaces("hello world")
```

```python
"helloworld"
```

---

# Math Utilities

## isPrime

```python
isPrime(7)
```

```python
True
```

---

## toRoman

```python
toRoman(2025)
```

```python
"MMXXV"
```

---

## fromRoman

```python
fromRoman("MMXXV")
```

```python
2025
```

---

# List Utilities

## reverseList

```python
reverseList([1, 2, 3])
```

```python
[3, 2, 1]
```

---

## removeDuplicates

```python
removeDuplicates([1, 1, 2, 3, 3])
```

```python
[1, 2, 3]
```

---

# JSON Utilities

## readJSON

```python
readJSON("data.json")
```

```python
{
    "name": "John"
}
```

---

## writeJSON

```python
writeJSON("data.json", {"name": "John"})
```

---

# Time Utilities

## wait

```python
wait(2)
```

---

## currentTime

```python
currentTime()
```

```python
"21:35:12"
```

---

## currentDate

```python
currentDate()
```

```python
"2026-05-27"
```

---

# Example

```python
from myutils import *

print(reverseString("Python"))
print(isPrime(13))
print(toRoman(100))
print(currentTime())
```

---

# Planned Features

```python
randomInt()
randomFloat()
factorial()
fibonacci()
clamp()
lerp()
flatten()
shuffleList()
bigNumberFormat()
typeWriter()
fakeHack()
```

---

# License

```text
MIT License

Free to use, modify, and distribute.
```

---

# Features

```startsWith```, ```enssWith```, ```reverseString```, etc.
```

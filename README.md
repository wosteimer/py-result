A python implementation of the Result type, based on the rust language

## Installation

```bash
pip install py_result
```
or
```bash
poetry install py_result
```

## Usage Example

```python
def div(x: float, y: float) -> Result[float, ZeroDivisionError]:
	if y == 0:
		return Err(ZeroDivisionError("Ops"))

	return Ok(x / y)

result = div(10, 2)


match result:
	case Ok(v):
		print(v)

	case Err(e):
		# handle error here
		...
```

# Maybe-Boolean

The `Maybe` type from the `maybe_boolean` package creates a new boolean-like value that could could be true OR false when evaluated. Once it is evaluated to a boolean value, it keeps its identity. Install the library with `pip install maybe-bool`.

Short Example
```py
from maybe_boolean import Maybe

val = Maybe()

if val:
	print(val) # prints `True`
else:
	print(val) # prints `False`

```
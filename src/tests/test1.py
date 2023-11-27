from maybe_boolean import Maybe

val = Maybe()

if val:
	print(val) # prints `True`
else:
	print(val) # prints `False`

	if val:
		print("impossible")
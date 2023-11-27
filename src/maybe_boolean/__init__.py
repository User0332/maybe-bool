import random

class Maybe(int):
	def __bool__(self) -> bool:
		try: return getattr(self, "_val")
		except AttributeError:
			self._val = bool(random.randint(0, 1))

			return self._val
		
	def __repr__(self) -> str:
		return str(bool(self))
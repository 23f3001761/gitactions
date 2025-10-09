import math

def factorial(n):
  """
  Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.

  Raises:
    ValueError: If n is a negative integer.
  """
  if not isinstance(n, int) or n < 0:
    raise ValueError("Factorial is not defined for non-integers or negative integers.")
  return math.factorial(n)

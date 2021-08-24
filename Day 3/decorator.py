# Assignment - Implement a decorator mod_div() which assures that the numerator is always greater than the denominator
# e.g. if a = 2, b = 4, then div(a, b) should return 2.0 as the output and not 0.5

def mod_div(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)   

  return inner

@mod_div
def div(a, b):
  print(a / b)

div(2, 4)
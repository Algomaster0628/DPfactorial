memo = {} # Calculates factorial using memoization and dynammic programming.
def DPfact(N):
  if N in memo:
    return memo[N]
  if N == 0 or N == 1:
    return 1
    memo[N] = 1
  else:
    factorial = N*DPfact(N - 1)
  memo[N] = factorial
  return factorial
x = DPfact(90)
print(x)
print(memo)

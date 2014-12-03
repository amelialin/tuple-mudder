def permutations(prefix, remainder=None, all_permutations=None):
  if remainder is None:
    all_permutations = []
    permutations("", prefix, all_permutations)
    return all_permutations

  if len(remainder) == 1:
    all_permutations.append(prefix + remainder)
  else:
    for i, element in enumerate(remainder):
      permutations(prefix + element,
                   remainder[:i] + remainder[i + 1:],
                   all_permutations)

if __name__ == "__main__":
  from sys import argv
  script, string = argv
  print permutations(string)

# my version uses default arguments
# to detect the "starting" case
# to avoid a helper function
# 11:15
# Me
# i don't know what that means
# 11:15
# Keir Mierle
# if you want look it up
# python default arguments
# basically
# my function can get invoked either as
# permutation(x)
# permutation(x, y)
# permutation(x, y, z)
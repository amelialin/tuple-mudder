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

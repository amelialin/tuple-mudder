Jeffreyer = "%r %r %r %r"

print Jeffreyer % (1, 2, 3, 4)
print Jeffreyer % ("one", "two", "three", "four")
print Jeffreyer % (True, False, False, True)
print Jeffreyer % (Jeffreyer, Jeffreyer, Jeffreyer, Jeffreyer)
print Jeffreyer % (
    "I had this thing.",
    "That you couldn't type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Note that when there's a contraction in your string, the outer quotes change to double quotes (lines 9 and 10).

progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
print(progname)
x = 0
for i in range(len(progname)):
  prog = progname[i]
  if prog == (" "):
    x += 1
print("There are", x, "spaces in this code")

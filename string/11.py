s = ["flower", "flow", "flight"]


preflix = s[0]

for word in s[1:]:
      while not word.startswith(preflix):
            preflix = preflix[:-1]

print("Longest preflix: ", preflix)

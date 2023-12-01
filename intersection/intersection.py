def intersection(a, b):
  res = []
  vals = set()
  for c in a:
    vals.add(c)
  for c in b:
    if c in vals:
      res.append(c)
  return res
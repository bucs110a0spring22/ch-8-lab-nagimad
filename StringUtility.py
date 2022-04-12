class StringUtility:
  def __init__(self, string = ''):
    self.original = string
  
  def __str__(self):
    return self.original
  
  def vowels(self):
    return ("many" if (sum([self.original.count(i) for i in "aeiouAEIOU"])>= 5) else str(sum([self.original.count(i) for i in "aeiouAEIOU"])))
  
  def bothEnds(self):
    return '' if (len(self.original) <= 2) else (self.original[0:2] + self.original[-2:])
  
  def fixStart(self): 
    return self.original if len(self.original)<=1 else self.original[0]+ (self.original.replace(self.original[0], "*"))[1:]
  
  def asciiSum(self):
    return sum([ord(i) for i in self.original])
  
  def cipher(self):
    cipherString = ''
    for i in self.original:
      newOrd = ord(i) + len(self.original)
      if ord('a')<=ord(i)<=ord('z'):
        for x in range(ord('a'),ord('z')+1):
          if (newOrd-x)%26==0:
            cipherString = cipherString + chr(x)
      elif ord('A') <= ord(i) <= ord('Z'):
        for x in range(ord('A'),ord('Z')+1):
          if (newOrd-x)%26==0:
            cipherString = cipherString + chr(x)
      else:
        cipherString = cipherString + i
    return cipherString
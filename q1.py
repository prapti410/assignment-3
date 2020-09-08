def panagram(string1):
      alphabets = "abcdefghijklmnopqrstuvwxyz"
      for char in alphabets:
          if char not in string1.lower():
              return (print("not a pangram string"))
              print("panagram string")

    panagram("The quick brown fox jumps over the lazy dog")
    panagram("Hello there")

def sample(n):
    d={"UPPER":0, "LOWER":0}
    for c in n:
        if c.isupper():
           d["UPPER"]+=1
        elif c.islower():
           d["LOWER"]+=1
        else:
           pass
    print ("Original String : ", n)
    print ("No. of Upper case characters : ", d["UPPER"])
    print ("No. of Lower case Characters : ", d["LOWER"])

sample('The quick Brow Fox')
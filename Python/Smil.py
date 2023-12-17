def smile(list:list):
    di = set()
    for i  in range(len(liste)):
        for j in range(len(liste)-1):
            if (liste[j] == ":" or liste[j] == ";") and ((liste[j+1] == ")") or (liste[j+1] == "-" and liste[j+2] == ")") ):
                di.add(j)

    return di
           
              




liste = [ord for ord in input()]

a = smile(liste)
for i in sorted(a):
    print(i)

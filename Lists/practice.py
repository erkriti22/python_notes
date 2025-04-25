nested_list = [1, [2, [30, 4], [5, 16]], 7, [8, [90, [10]]]]

for i in nested_list:
        if isinstance(i, list):
           for a in i:
               if isinstance(a, list):
                    for x in a:
                         print(x,"printlist")
                         if isinstance(x,list):
                             for z in x:
                                  print(z,"last")
                         else:
                              print(x,"err")
               else:
                    print(a,"else")
        else:
           print(i,"else1")
        
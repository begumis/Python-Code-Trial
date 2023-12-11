import timeit

demet = (10,20,30,40,50)
demet_zaman = timeit.timeit('demet[3]', globals=globals(), number=1000000000)

liste = [10,20,30,40,50]
liste_zaman = timeit.timeit('liste[3]',globals=globals(),number=1000000000)





print("Demet zaman :",demet_zaman)
print()
print("Liste zaman :",liste_zaman)
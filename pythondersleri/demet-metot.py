tuple = ("Ankara", "İstanbul", "İzmir", "Ankara","Ankara")
tuple2 = ("Konya", "Adana")
tuple += tuple2
print(tuple.index("İzmir"))
print(tuple.count("Ankara"))
print(tuple)
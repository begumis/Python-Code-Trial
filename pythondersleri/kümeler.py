küme = {"Battal", "Koç", 12, 15, 18, 20, 12, "Battal"}
print(küme)
list = [12345, 67891, 3543162, 35625]
küme2 = set(list)
print(küme2)
küme3 = set("begum")
print(küme3)

banned_identities = {12, 23, 62}
entered_identities = {12, 1, 2, 5, 62}

union =banned_identities.union(entered_identities)
print(union)

difference = banned_identities.difference(entered_identities)
print(difference)

difference1 = entered_identities.difference(banned_identities)
print(difference1)

banned_identities.add(32)
print(banned_identities)
banned_identities.remove(12)
print(banned_identities)
common_set = banned_identities.intersection(entered_identities)
if bool(common_set) == True:
    print("Banned identity has entered the site.")
    print(common_set)
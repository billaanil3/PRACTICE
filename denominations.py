from collections import OrderedDict
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = int(input("Enter a number:"))
res_notes = OrderedDict()
for note in notes:
    if amount % note:
        if amount // note > 0:
            res_notes[note] = amount // note
        amount = amount % note
print res_notes

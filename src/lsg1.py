#
# LOESUNG CODING CHALLANGE #1
#


def steuer(gehalt):
    if gehalt > 4000:
        return gehalt * 0.26
    elif gehalt >= 2500 and gehalt <= 4000:
        return gehalt * 0.22
    else:
        return gehalt * 0.18


gehalt = eval(input("Gehalt: "))
steuern = steuer(gehalt)
print(("Du zahlst: ", steuern))

rsm = []
rsm.append(["2.88","7.2","-30+sh"])

rsm.append(["0.8928","-7.2","-30+sh"])

rsm.append(["0.045","1.5","-45+sh"])

rsm.append(["0.015","-1.5","-45+sh"])

for r in rsm:
    rate, scale, midpoint = r
    vmv = "(v - (%s))"%midpoint

    exp = 'expr_form="generic" expr="%s == 0 ? %s : %s * (%s / %s) /(1 - exp((-1 * %s)/%s))"' % (vmv, rate, rate, vmv, scale, vmv, scale)

    print
    print exp
    print
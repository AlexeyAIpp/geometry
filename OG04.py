def ravenstvo_po_dvum_storonam_i_uglu(a1, b1, ugol1, a2, b2, ugol2):
    if a1 == a2 and b1 == b2 and ugol1 == ugol2:
        print("Треугольники равны по двум сторонам и углу между ними.")
    else:
        print("По данному признаку равенство треугольников не доказано.")


def ravenstvo_po_storone_i_dvum_uglam(storona1, ugol1a, ugol1b,
                                      storona2, ugol2a, ugol2b):
    if storona1 == storona2 and ugol1a == ugol2a and ugol1b == ugol2b:
        print("Треугольники равны по стороне и двум прилежащим к ней углам.")
    else:
        print("По данному признаку равенство треугольников не доказано.")


def ravenstvo_po_trem_storonam(a1, b1, c1, a2, b2, c2):
    if a1 == a2 and b1 == b2 and c1 == c2:
        print("Треугольники равны по трём сторонам.")
    else:
        print("По данному признаку равенство треугольников не доказано.")


ravenstvo_po_dvum_storonam_i_uglu(5, 7, 60, 5, 7, 60)
ravenstvo_po_storone_i_dvum_uglam(8, 45, 70, 8, 45, 70)
ravenstvo_po_trem_storonam(3, 4, 5, 3, 4, 5)


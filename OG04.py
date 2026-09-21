def ravenstvo_po_storone_i_dvum_uglam(storona1, ugol1a, ugol1b,
                                      storona2, ugol2a, ugol2b):
    if storona1 == storona2 and ugol1a == ugol2a and ugol1b == ugol2b:
        print("Треугольники равны по стороне и двум прилежащим к ней углам.")
    else:
        print("По данному признаку равенство треугольников не доказано.")

ravenstvo_po_storone_i_dvum_uglam(8, 45, 70, 8, 45, 70)
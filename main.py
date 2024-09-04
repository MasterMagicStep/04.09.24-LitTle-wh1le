#
My_List = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
gar = 0
#
while gar < len(My_List):
#
    if My_List[gar] < 0:
        break
#
    if My_List[gar] > 0:
        print(My_List[gar])
#
    gar += 1
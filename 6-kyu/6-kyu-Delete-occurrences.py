def delete_nth(order, max_e):
    order.reverse()
    temp = order.copy()
    for e in order:
        count_e = temp.count(e)
        if count_e > max_e:
            temp.remove(e)
    temp.reverse()
    return temp

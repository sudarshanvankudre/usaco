"""
ID: svankudre
TASK: mixmilk
LANG: PYTHON3
"""


with open('mixmilk.in', 'r') as fin:
    c0, m0 = map(int, fin.readline().split())
    c1, m1 = map(int, fin.readline().split())
    c2, m2 = map(int, fin.readline().split())

def pour(sending):
    """Pour from sending bucket"""
    global c0, c1, c2, m0, m1, m2
    receive_bucket = (sending + 1) % 3
    r0 = False
    r1 = False
    r2 = False
    if receive_bucket == 0:
        sending_amount = m2
        receive_capacity = c0 - m0
        r0 = True
    elif receive_bucket == 1:
        sending_amount = m0
        receive_capacity = c1 - m1
        r1 = True
    else:
        sending_amount = m1
        receive_capacity = c2 - m2
        r2 = True

    if r0:
        if sending_amount <= receive_capacity:
            m2 -= sending_amount
            m0 += sending_amount
        else:
            m0 = c0
            m2 -= receive_capacity
    elif r1:
        if sending_amount <= receive_capacity:
            m0 -= sending_amount
            m1 += sending_amount
        else:
            m1 = c1
            m0 -= receive_capacity
    else:
        if sending_amount <= receive_capacity:
            m1 -= sending_amount
            m2 += sending_amount
        else:
            m2 = c2
            m1 -= receive_capacity

for i in range(100):
    sending = i % 3
    pour(sending)

with open('mixmilk.out', 'w') as fout:
    for m in [m0, m1, m2]:
        fout.write(str(m) + "\n")

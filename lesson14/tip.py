def total_calc(bill_amount, tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("please pay",total)
total_calc(180,20)
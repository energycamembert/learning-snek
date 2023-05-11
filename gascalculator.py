def main():

    #calculate gas prices
    
    total_cost = 0.0
    gasprice = 1.8
    distance = 100.0

    #equal to small car
    consumption = 5

    gasprice = float(input("Current gas price: "))
    distance = float(input("Kilometers to drive: "))

    total_cost = consumption * gasprice * distance / 100.0
    print("Gas costs are (median): €", round(total_cost, 2))
    print("Gas costs are (fast driving): €", round(total_cost*1.2, 2))
    print("Gas costs are (economic driving): €", round(total_cost*0.8, 2))

main()
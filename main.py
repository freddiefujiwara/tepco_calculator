#!/usr/bin/env python3
"""main.py"""
import tepco_calculator

def main():
    """Main function"""
    # input
    capacity = int(input("Contracted capacity (A):"))
    usage = int(input("Amount of electricity used (kWh):"))

    # calculate
    price = tepco_calculator.total_calc(capacity, usage)

    # output
    print("The electric bill is ", price, "JPY.")
    print("-----------------------------")
    print("Basic cost =", round(tepco_calculator.basic_charge_calc(capacity)), "JPY")
    print("Power cost  =", round(tepco_calculator.power_charge_calc(usage)), "JPY")
    print("Fuel cost  =", round(tepco_calculator.fuel_cost_calc(usage)), "JPY")
    print("Renewable cost  =", round(tepco_calculator.renewable_energy_calc(usage)), "JPY")


# Using the special variable
# __name__
if __name__=="__main__":
    main()

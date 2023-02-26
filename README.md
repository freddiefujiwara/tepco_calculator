# Tepco Calculator

This is a calculator for Tepco electricity charges in Japan.

## Usage

1. Install Python3.
2. Run `main.py`.
3. Enter the contracted capacity and amount of electricity used.
4. The program will calculate the total charges and print the breakdown of each charge.

Note: The fuel cost adjustment and renewable energy surcharge prices are based on March 2021 rates.

# Functions
The following functions are included in this program:

+ basic_charge_calc(capacity): calculates the basic charge (per month) based on the contracted capacity in amps.
+ power_charge_calc(usage): calculates the electricity charges (per month) based on the amount of electricity used in kilowatt-hours.
+ fuel_cost_calc(usage): calculates the fuel cost adjustment (per month) based on the amount of electricity used in kilowatt-hours.
+ renewable_energy_calc(usage): calculates the renewable energy surcharge (per month) based on the amount of electricity used in kilowatt-hours.
+ total_calc(capacity, usage): calculates the total electric bill (per month) based on the contracted capacity in amps and the amount of electricity used in kilowatt-hours.

## Dependencies

- `decimal`
- `math`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

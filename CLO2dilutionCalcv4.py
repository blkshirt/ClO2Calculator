#CLO2 dilution calc v4 by BlkShirt

def convert_volume_to_ml(volume, unit):
    """Convert volume to milliliters based on the unit."""
    unit = unit.lower()
    if unit in ["gallons", "gal", "g"]:
        return volume * 3785.41  # 1 gallon = 3785.41 ml
    elif unit == "oz":
        return volume * 29.5735  # 1 ounce = 29.5735 ml
    elif unit == "ml":
        return volume
    else:
        raise ValueError("Unsupported unit. Use gallons, ml, or oz.")

def convert_ml_to_unit(volume_ml, unit):
    """Convert milliliters to the specified unit."""
    unit = unit.lower()
    if unit in ["gallons", "gal", "g"]:
        return volume_ml / 3785.41  # Convert ml to gallons
    elif unit == "oz":
        return volume_ml / 29.5735  # Convert ml to ounces
    elif unit == "ml":
        return volume_ml
    else:
        raise ValueError("Unsupported unit. Use gallons, ml, or oz.")

def calculate_concentrate_volume(V_f_ml, C_initial, C_final):
    """Calculate the volume of concentrate needed in ml to achieve the desired ppm."""
    if C_final >= C_initial:
        raise ValueError("Final concentration must be less than the initial concentration.")
    return (C_final * V_f_ml) / C_initial

def main():
    while True:
        print("Enter the initial concentration of the concentrate and the desired final concentration in ppm.")
        C_initial = float(input("Concentrate initial concentration (ppm): "))
        C_final = float(input("Desired final concentration (ppm): "))

        print("Choose the unit of volume: gallons (gal), milliliters (ml), or ounces (oz).")
        unit = input("Unit of volume: ").strip()
        V_f = float(input(f"Final total volume of the solution in {unit}: "))

        V_f_ml = convert_volume_to_ml(V_f, unit)
        V_c_ml = calculate_concentrate_volume(V_f_ml, C_initial, C_final)
        V_c = convert_ml_to_unit(V_c_ml, unit)
        
        print(f"You need to add {V_c:.2f} {unit} of concentrate to achieve the desired concentration of {C_final} ppm.")
        print("----------------------------")

if __name__ == "__main__":
    main()

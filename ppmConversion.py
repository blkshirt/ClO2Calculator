##############################
#                            #
#      ppm calculator        #
#                            #
#     written by nickal      #
#                            #
##############################


print("Welcome to the PPM Dilution Calculator")

def calculate_dilution_volume(initial_concentration, target_concentration, volume):
    dilution_factor = initial_concentration / target_concentration
    dilution_volume = volume / dilution_factor
    return dilution_volume

def convert_ml_to_oz(ml):
    return ml * 0.033814

def convert_ml_to_gal(ml):
    return ml * 0.000264172

def display_help():
    print("\nUsage:")
    print("Enter the volume unit (ml, oz, or gal).")
    print("Abbreviations like ('g','o','m') will also work.")

def main():
    try:
        display_help()

        while True:
            initial_concentration = float(input("\nEnter the initial concentration of ClO2 in ppm: "))
            if initial_concentration == 0:
                print("Initial concentration cannot be zero. Please enter a valid value.")
                continue

            target_concentration = float(input("Enter the target concentration of ClO2 in ppm: "))
            volume_unit = input("Enter the volume unit (ml, oz, or gal): ").lower()
            volume = float(input("Enter the volume amount: "))

            if volume_unit == "help":
                display_help()
                continue

            if volume_unit not in ["ml","g","gals","gallons","gallon","o","ounce","ounces","milli","millimeter","m" "oz", "gal"]:
                print("Invalid volume unit. Please enter ml, oz, or gal.")
                continue

            if volume_unit == "oz":
                volume_ml = volume / 0.033814  # Convert oz to ml
            elif volume_unit == "gal":
                volume_ml = volume / 0.000264172  # Convert gal to ml
            else:
                volume_ml = volume

            dilution_volume_ml = calculate_dilution_volume(initial_concentration, target_concentration, volume_ml)
            dilution_volume_oz = convert_ml_to_oz(dilution_volume_ml)
            dilution_volume_gal = convert_ml_to_gal(dilution_volume_ml)

            print("\nDilution Results:")
            print(f"Dilution needed: {dilution_volume_ml:.2f} ml")
            print(f"Dilution needed: {dilution_volume_oz:.2f} oz")
            print(f"Dilution needed: {dilution_volume_gal:.6f} gal")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

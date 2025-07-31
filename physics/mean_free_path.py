import math

def mean_free_path_from_volume(
    diameter_nm,
    volume_cm3,
    mols
):
    pi = math.pi
    N_A = 6.022e23
    k_B = 1.380649e-23

    # Convert to SI units
    diameter_m = diameter_nm * 1e-9
    volume_m3 = volume_cm3 * 1e-6

    # Calculate number density
    N_particles = mols * N_A
    n = N_particles / volume_m3  # particles per m³

    # Mean free path: λ = 1 / (√2 * π * d² * n)
    lambda_m = 1 / (math.sqrt(2) * pi * diameter_m**2 * n)
    lambda_nm = lambda_m * 1e9

    return lambda_nm

def get_input(prompt, default):
    user_input = input(f"{prompt} [{default}]: ").strip()
    return float(user_input) if user_input else default

def main():
    print("\n🔬 Mean Free Path Calculator (Volume-based)\n")

    diameter_nm = get_input("Molecular diameter (nm)", 0.3)
    volume_cm3  = get_input("Gas volume (cm³)", 1.0)
    mols        = get_input("Moles of gas in volume", 1.0 / 22400)  # STP mol in 1cm³

    result = mean_free_path_from_volume(diameter_nm, volume_cm3, mols)

    print("\n📊 Results:")
    print(f"  Molecular diameter: {diameter_nm} nm")
    print(f"  Volume:             {volume_cm3} cm³")
    print(f"  Moles of gas:       {mols:.6e} mol")
    print(f"  → Mean Free Path:   {result:.2f} nm\n")

if __name__ == "__main__":
    main()

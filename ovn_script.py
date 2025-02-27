def main():
    print("Velkommen til ovnindstillings-scriptet, Søster-let-på-tå!")
    
    # 1) Forskudt start
    delayed_start_hours = float(input(
        "Hvor lang tid (i timer) for forskudt start? (0 = ingen): "
    ))
    
    # 2) Starttemperatur
    current_temp = float(input("Indtast starttemperatur (°C): "))
    
    # 3) Antal steps
    num_steps = int(input("Hvor mange steps vil du indtaste? "))

    # For at gemme data til outputfil
    schedule_data = []

    total_time = 0.0

    # -- Forskudt start (hvis større end 0) --
    if delayed_start_hours > 0:
        # Linjer for forskudt start:
        # 1) 9999
        # 2) 3
        # 3) forsinkelse i minutter
        schedule_data.append(9999)
        schedule_data.append(3)
        schedule_data.append(delayed_start_hours * 60)
        
        # Læg forsinkelsen til total_time
        total_time += delayed_start_hours

    # -- De "normale" steps --
    for i in range(num_steps):
        print(f"\n--- Step {i+1} ---")

        # Indtast data
        ramp_time_hours = float(input("Hvor lang tid (i timer) til at nå næste temperatur? "))
        target_temp = float(input("Hvad er sluttemperaturen (°C)? "))
        
        # Brugeren taster holdetid i timer
        hold_time_hours = float(input("Hvor lang holdetid (i timer) ved denne temperatur? "))

        # Temperaturforskel
        temperature_diff = target_temp - current_temp
        
        if ramp_time_hours == 0:
            print("Fejl: Rampetid kan ikke være 0.")
            return

        # Beregn ramp rate
        ramp_rate = temperature_diff / ramp_time_hours

        # Omregn holdetid til minutter (til outputfil)
        hold_time_minutes = hold_time_hours * 60
        
        # Udskriv step-detaljer
        print(f"\nStep {i+1} detaljer:")
        print(f"  - Ramp fra {current_temp:.1f} °C til {target_temp:.1f} °C")
        print(f"    på {ramp_time_hours:.2f} timer (=> {ramp_rate:.2f} °C/time).")
        print(f"  - Hold {target_temp:.1f} °C i {hold_time_hours:.2f} timer.")

        # Tilføj til schedule_data
        schedule_data.append(ramp_rate)
        schedule_data.append(target_temp)
        schedule_data.append(hold_time_minutes)

        # Opdater samlet tid
        total_time += ramp_time_hours + hold_time_hours

        # Sæt nuværende temperatur
        current_temp = target_temp

    # -- Afkøling før støbning? --
    cooling_answer = input("\nSkal der være afkøling før støbning? (ja/nej): ").strip().lower()

    if cooling_answer == "ja":
        # Spørg om temperatur og holdetid
        cooling_temp = float(input("Hvilken temperatur skal der køles til? "))
        cooling_hold_hours = float(input("Hvor lang holdetid (i timer) ved den temperatur? "))

        # Ramp-rate er fast 100 (°C/time)
        ramp_rate_cooling = 100

        # Temperaturforskel
        temperature_diff_cooling = cooling_temp - current_temp
        
        # Rampetid i timer (husk absolute value, hvis man vil være sikker på at håndtere negative forskelle)
        ramp_time_cooling = abs(temperature_diff_cooling) / ramp_rate_cooling
        
        # Omregn holdetid til minutter til outputfil
        hold_time_cooling_minutes = cooling_hold_hours * 60

        # Udskriv info
        print(f"\nAfkøling før støbning:")
        print(f"  - Ramp fra {current_temp:.1f} °C til {cooling_temp:.1f} °C")
        print(f"    på {ramp_time_cooling:.2f} timer (fast sat til 100 °C/time).")
        print(f"  - Hold {cooling_temp:.1f} °C i {cooling_hold_hours:.2f} timer.")

        # Tilføj til schedule_data (samme 3-linje-format)
        schedule_data.append(ramp_rate_cooling)
        schedule_data.append(cooling_temp)
        schedule_data.append(hold_time_cooling_minutes)

        # Opdater total tid
        total_time += ramp_time_cooling + cooling_hold_hours

        # Opdater current_temp
        current_temp = cooling_temp

    # -- Spørg om filnavn --
    filename = input("\nHvad skal filen hedde (uden extension)? ")

    # -- Gem i fil uden extension --
    with open(filename, "w") as f:
        for value in schedule_data:
            f.write(f"{value:g}\n")  # :g fjerner unødvendige decimaler

    print(f"\nSamlet tid for hele processen (inkl. forsinkelse og evt. afkøling): {total_time:.2f} timer.")
    print(f"Data gemt i filen '{filename}' (uden fil-endelse).")


if __name__ == "__main__":
    main()


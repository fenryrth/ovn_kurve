# Ovnindstillings-script (README)

Velkommen til dette lille Python-script, som hjælper med at oprette en ovn-kurve med følgende muligheder:

- **Forskudt start** – Angiv, hvor mange timer ovnen skal vente, før den begynder at varme op.
- **Flere temperatur-steps** – For hver etape indtaster du:
  - Hvor lang tid (i timer) det tager at nå den ønskede temperatur.
  - Sluttemperaturen (°C).
  - Hvor længe temperaturen skal holdes (i timer).
- **Afkøling før støbning** – Scriptet kan tilføje en automatisk afkølingsfase med en fast ramp-rate på 100 °C/time.

Til sidst genererer scriptet en fil med 3 linjer pr. step (eller "sektion"), uden fil-endelse, som ovnen kan aflæse direkte.

## Kom hurtigt i gang

1. Klon eller download projektet, så du har `ovn_script.py` lokalt.
2. Sørg for at have **Python 3** installeret.
3. Åbn en terminal/kommandoprompt i mappen med scriptet.
4. Kør følgende kommando:

   ```sh
   python ovn_script.py
   ```

5. Følg anvisningerne i terminalen:
   - Indtast forskudt start (i timer) eller 0 for ingen.
   - Indtast din nuværende temperatur (°C).
   - Indtast antal steps.
   - For hvert step:
     - Antal timer til at nå næste temperatur.
     - Sluttemperatur (°C).
     - Holdetid (i timer).
   - Vælg om der skal tilføjes en afkøling før støbning.
   - Angiv filnavn (uden extension).

6. Når du har tastet alle data ind, skriver scriptet en fil (du selv har navngivet) med 3 linjer pr. step:

   ```
   Ramp rate (°C/time)
   Sluttemperatur (°C)
   Holdetid (minutter)
   ```

7. Hvis du har valgt forskudt start, tilføjes linjerne:

   ```
   9999
   3
   <Forskudt start i minutter>
   ```

8. Hvis du har valgt afkøling før støbning, tilføjes der til sidst:

   ```
   100
   <Afkølings-temperatur>
   <Afkølings-holdetid i minutter>
   ```

## Eksempel

**Brugersession:**

```
Hvor lang tid (i timer) for forskudt start? (0 = ingen): 2
Indtast starttemperatur (°C): 20
Hvor mange steps vil du indtaste? 1

--- Step 1 ---
Hvor lang tid (i timer) til at nå næste temperatur? 2
Hvad er sluttemperaturen (°C)? 150
Hvor lang holdetid (i timer) ved denne temperatur? 1

Skal der være afkøling før støbning? (ja/nej): ja
Hvilken temperatur skal der køles til? 80
Hvor lang holdetid (i timer) ved den temperatur? 1

Hvad skal filen hedde (uden extension)? min_ovnstyring
```

**Filoutput (`min_ovnstyring`):**

```
9999
3
120
65
150
60
100
80
60
```

**Forklaring:**

- `9999, 3, 120`: En forskudt start på 120 minutter (2 timer).
- `65, 150, 60`: Ramp rate = 65 °C/time, sluttemp 150 °C, holdetid 60 minutter (1 time).
- `100, 80, 60`: Afkøling fra 150 °C til 80 °C med 100 °C/time, hold 80 °C i 60 minutter (1 time).

## Tip

- Ønsker du at justere starttemperaturen, skal du blot indtaste en ny værdi, når scriptet spørger.
- Har du ingen afkøling før støbning, svarer du blot **“nej”** til sidst.
- Scriptet konverterer holdetid fra timer til minutter i filen, så ovnen læser det korrekt.
- Husk at give filen et tydeligt navn, så du kan genkende netop den kurve, du har genereret.

## Bidrag

- Du er velkommen til at lave **pull requests** eller **issues** for at forbedre scriptet.
- Skriptet er tænkt som et udgangspunkt – tilpas det gerne til dine egne behov.

**God fornøjelse!**


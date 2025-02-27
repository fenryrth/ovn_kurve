Velkommen til dette lille Python-script, som hjælper med at oprette en ovn-kurve med følgende muligheder:

    Forskudt start – Angiv, hvor mange timer ovnen skal vente, før den begynder at varme op.
    Flere temperatur-steps – For hver etape indtaster du:
        hvor lang tid (i timer) det tager at nå den ønskede temperatur,
        sluttemperaturen (°C),
        hvor længe temperaturen skal holdes (i timer).
    Afkøling før støbning – Scriptet kan tilføje en automatisk afkølingsfase med en fast ramp-rate på 100 °C/time.

Til sidst genererer scriptet en fil med 3 linjer pr. step (eller “sektion”), uden fil-endelse, som ovnen kan aflæse direkte.

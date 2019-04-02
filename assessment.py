from statistics import mean

sprache = {
    'Rechtschreibung': 1,
    'Grammatik': 1,
    'Ausdrucksweise': 1,
    'Fachsprache': 1,
    'abwechslungsreiche Sprache': 1,
    'sprachliche Struktur': 1
}

inhalt = {
    'Abstract': 1,
    'Zielsetzung': 1,
    'Motivation': 1,
    'Einschränkungen': 1,
    'Forschungsstand': 1,
    'definiert': 1,
    'präzise': 1,
    'alle wichtigen Aspekte': 1,
    'roter Faden': 1,
    'kritische Betrachtung': 1,
    'objektiv': 1,
    'Fazit': 3,
    'Ausblick': 1,
    'Aufbau': 1,
    'Abbildungen': 1
}

formatierung = {
    'einheitlich und sauber': 2,
    'Hervorhebungen': 2,
    'Ränder': 2,
    'Abbildungen': 2
}

quellenangabe = {'passend und ausreichend zitiert': 1, 'sorgfältig': 2}

evaluation = {
    'decken den Problemraum sehr gut ab': 1,
    'beschrieben': 1,
    'Präsentation': 1
}

gewichte = {
    'Sprache': 2,
    'Inhalt': 8,
    'Methode: Formatierung': 1,
    'Methode: Quellenangabe': 1,
    'Methode: Evaluation': 3
}

sprache_avg = mean(sprache.values())
inhalt_avg = mean(inhalt.values())
formatierung_avg = mean(formatierung.values())
quellenangabe_avg = mean(quellenangabe.values())
evaluation_avg = mean(evaluation.values())

sprache_weighted = sprache_avg * gewichte['Sprache']
inhalt_weighted = inhalt_avg * gewichte['Inhalt']
formatierung_weighted = formatierung_avg * gewichte['Methode: Formatierung']
quellenangabe_weighted = quellenangabe_avg * gewichte['Methode: Quellenangabe']
evaluation_weighted = evaluation_avg * gewichte['Methode: Evaluation']

overall = sprache_weighted \
          + inhalt_weighted \
          + formatierung_weighted \
          + quellenangabe_weighted \
          + evaluation_weighted
overall /= sum(gewichte.values())
integer = overall // 1
decimals = overall % 1

if decimals > 0.15 and decimals <= 0.5:
    overall_rounded = integer + 0.3
elif decimals > 0.5 and decimals <= 0.85:
    overall_rounded = integer + 0.7
elif decimals > 0.85:
    overall_rounded = integer + 1
else:
    overall_rounded = integer

print(f'Sprache: {sprache_avg:.2f}')
print(f'Inhalt: {inhalt_avg:.2f}')
print(f'Methode – Formatierung: {formatierung_avg:.2f}')
print(f'Methode – Quellenangabe: {quellenangabe_avg:.2f}')
print(f'Methode – Evaluation: {evaluation_avg:.2f}')
print('---')
print(f'Durchschnittliche Gesamtnote: {overall}')
print(f'Gesamtnote: {overall_rounded:.1f}')

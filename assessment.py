from statistics import mean

sprache = {
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
}

inhalt = {
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
}

formatierung = {
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
}

quellenangabe = {***REMOVED***}

evaluation = {
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
}

gewichte = {
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
    ***REMOVED***
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

print(f'{"Sprache:":<25}{sprache_avg:>3.2f}',
      f'\n{"Inhalt:":<25}{inhalt_avg:>3.2f}',
      f'\n{"Methode – Formatierung:":<25}{formatierung_avg:>3.2f}',
      f'\n{"Methode – Quellenangabe:":<25}{quellenangabe_avg:>3.2f}',
      f'\n{"Methode – Evaluation:":<25}{evaluation_avg:>3.2f}', f'\n{"-"*29}',
      f'\n{"Durchschnitt:":<25}{overall:>3.2f}',
      f'\n{"Gesamtnote:":<25}{overall_rounded:>3.1f}')

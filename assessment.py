#!/usr/bin/env nix-shell
#! nix-shell -i python -p "python3.withPackages (ps: with ps; [ click ])"

from click import argument, command, echo, option, Path, version_option
from configparser import ConfigParser
from dataclasses import dataclass
from pprint import pformat
from statistics import mean
from typing import Dict, Iterable, Mapping, Tuple

DELTA = 1e-3

SPRACHE_KEY = 'sprache'
INHALT_KEY = 'inhalt'
FORMATIERUNG_KEY = 'formatierung'
QUELLENANGABE_KEY = 'quellenangabe'
IMPLEMENTIERUNG_KEY = 'implementierung'
EVALUATION_KEY = 'evaluation'
MALI_KEY = 'mali'
GEWICHTE_KEY = 'gewichte'


@dataclass
class GradeAverages:

    sprache: float
    inhalt: float
    formatierung: float
    quellenangabe: float
    implementierung: float
    evaluation: float


class AveragesPrinter:

    averages: GradeAverages
    weights: Mapping[str, int]

    def __init__(self, weights: Mapping[str, int],
                 averages: GradeAverages) -> None:

        self.averages = averages
        self.weights = weights

    def __str__(self) -> str:

        averages_literal = (
            f'{"Sprache:":<28}{self.averages.sprache:>3.2f}\n' +
            f'{"Inhalt:":<28}{self.averages.inhalt:>3.2f}\n' +
            f'{"Methode – Formatierung:":<28}' +
            f'{self.averages.formatierung:>3.2f}\n' +
            f'{"Methode – Quellenangabe:":<28}' +
            f'{self.averages.quellenangabe:>3.2f}\n' +
            (f'{"Methode – Implementierung:":<28}' +
             f'{self.averages.implementierung:>3.2f}\n'
             if self.weights[IMPLEMENTIERUNG_KEY] != 0 else '') +
            (f'{"Methode – Evaluation:":<28}{self.averages.evaluation:>3.2f}\n'
             if self.weights[EVALUATION_KEY] != 0 else ''))

        return averages_literal.rstrip()


@dataclass
class GradeOveralls:

    overall: float
    overall_rounded: float


class OverallsPrinter:

    overalls: GradeOveralls
    mali: bool

    def __init__(self, overalls: GradeOveralls, mali: bool) -> None:

        self.overalls = overalls
        self.mali = mali

    def __str__(self) -> str:

        return (f'{"Durchschnitt:":<28}{self.overalls.overall:>3.2f}\n' +
                f'{"Mali:":<28}{self.mali}\n' + f'{"-"*33}\n' +
                f'{"Gesamtnote:":<28}{self.overalls.overall_rounded:>3.1f}')


@dataclass
class GradeSections:

    sprache: Dict[str, int]
    inhalt: Dict[str, int]
    formatierung: Dict[str, int]
    quellenangabe: Dict[str, int]
    implementierung: Dict[str, int]
    evaluation: Dict[str, int]


def print_weights(weights: Mapping[str, int]) -> None:

    echo(pformat(weights))


def config_items_to_dict(
        config_items: Iterable[Tuple[str, str]]) -> Dict[str, int]:

    return {k: int(v) for k, v in dict(config_items).items()}


def read_mali_from_config(config: ConfigParser) -> bool:

    return config.items(MALI_KEY)[0][1] == 'True'


def print_grades(averages_printer: AveragesPrinter,
                 overalls_printer: OverallsPrinter) -> str:

    assessment = (str(averages_printer) + '\n' + str(f'{"-"*33}\n') +
                  str(overalls_printer))

    echo(assessment)

    return assessment


def get_grade_sections(config: ConfigParser) -> GradeSections:

    sprache = config_items_to_dict(config.items(SPRACHE_KEY))

    inhalt = config_items_to_dict(config.items(INHALT_KEY))

    formatierung = config_items_to_dict(config.items(FORMATIERUNG_KEY))

    quellenangabe = config_items_to_dict(config.items(QUELLENANGABE_KEY))

    implementierung = config_items_to_dict(config.items(IMPLEMENTIERUNG_KEY))

    evaluation = config_items_to_dict(config.items(EVALUATION_KEY))

    return GradeSections(sprache, inhalt, formatierung, quellenangabe,
                         implementierung, evaluation)


def calculate_averages(config: ConfigParser) -> GradeAverages:

    grade_sections = get_grade_sections(config)

    sprache_avg = mean(grade_sections.sprache.values())
    inhalt_avg = mean(grade_sections.inhalt.values())
    formatierung_avg = mean(grade_sections.formatierung.values())
    quellenangabe_avg = mean(grade_sections.quellenangabe.values())
    implementierung_avg = mean(grade_sections.implementierung.values())
    evaluation_avg = mean(grade_sections.evaluation.values())

    return GradeAverages(sprache_avg, inhalt_avg, formatierung_avg,
                         quellenangabe_avg, implementierung_avg,
                         evaluation_avg)


def load_config(grades_file: str) -> ConfigParser:

    config = ConfigParser()
    config.read(grades_file)

    return config


def weigh_averages(averages: GradeAverages,
                   weights: Mapping[str, int]) -> GradeAverages:

    sprache_weighted = averages.sprache * weights[SPRACHE_KEY]

    inhalt_weighted = averages.inhalt * weights[INHALT_KEY]

    formatierung_weighted = averages.formatierung * weights[FORMATIERUNG_KEY]

    quellenangabe_weighted = (averages.quellenangabe *
                              weights[QUELLENANGABE_KEY])

    implementierung_weighted = (averages.implementierung *
                                weights[IMPLEMENTIERUNG_KEY])

    evaluation_weighted = averages.evaluation * weights[EVALUATION_KEY]

    return GradeAverages(sprache_weighted, inhalt_weighted,
                         formatierung_weighted, quellenangabe_weighted,
                         implementierung_weighted, evaluation_weighted)


def calculate_weighted_average(weighted_averages: GradeAverages,
                               weights: Mapping[str, int]) -> float:

    overall = (weighted_averages.sprache + weighted_averages.inhalt +
               weighted_averages.formatierung +
               weighted_averages.quellenangabe +
               weighted_averages.implementierung +
               weighted_averages.evaluation)
    overall /= sum(weights.values())

    return overall


def calculate_overall(weights: Mapping[str, int],
                      averages: GradeAverages) -> float:

    weighted_averages = weigh_averages(averages, weights)

    return calculate_weighted_average(weighted_averages, weights)


def split_decimal_number(decimal_number: float) -> Tuple[int, float]:

    integer = int(decimal_number)
    decimals = decimal_number % 1

    return integer, decimals


def round_to_nearest_grade(decimals: float) -> float:

    if decimals > 0.15 and decimals <= 0.5:
        return 0.3
    elif decimals > 0.5 and decimals <= 0.85:
        return 0.7
    elif decimals > 0.85:
        return 1.0
    else:
        return 0.0


def add_grade_level(grade: float) -> float:

    integer, decimals = split_decimal_number(grade)

    if abs(decimals - 0.3) < DELTA:
        grade += 0.4
    else:
        grade += 0.3

    return grade


def round_overall(overall: float, mali: bool) -> float:

    integer, decimals = split_decimal_number(overall)

    rounded_overall = integer + round_to_nearest_grade(decimals)

    if mali:
        rounded_overall = add_grade_level(rounded_overall)

    return rounded_overall


def calculate_grade_overalls(mali: bool, weights: Mapping[str, int],
                             averages: GradeAverages) -> GradeOveralls:

    overall = calculate_overall(weights, averages)
    overall_rounded = round_overall(overall, mali)

    return GradeOveralls(overall, overall_rounded)


def write_assessment(file_name: str, assessment: str) -> None:

    with open(file_name, 'w') as fh:
        fh.write(assessment + '\n\n')


def assess(config: ConfigParser, weights: Mapping[str, int]) -> str:

    averages = calculate_averages(config)
    mali = read_mali_from_config(config)
    overalls = calculate_grade_overalls(mali, weights, mali)

    averages_printer = AveragesPrinter(weights, averages)
    overalls_printer = OverallsPrinter(overalls, mali)

    return print_grades(averages_printer, overalls_printer)


@command()
@argument('grades', type=Path(exists=True), required=True)
@option('--out', type=Path(), help='Save assessment to file.')
@option('--weights',
        is_flag=True,
        help='Show the section\'s weights and exit.')
@version_option('1.1.0')
def main(grades: str, out: str, weights: bool) -> None:

    config = load_config(grades)
    section_weights = config_items_to_dict(config.items(GEWICHTE_KEY))

    if weights:
        print_weights(section_weights)
    else:
        assessment = assess(config, section_weights)
        if out: write_assessment(out, assessment)


if __name__ == '__main__':
    main()
# AdventOfCode

A place to store my brain solution to Advent of Code problems.

I rarely use classes because I try to embody ["Simple is better than complex"](https://peps.python.org/pep-0020/)

## Solution Requirements

- Accept provided logic tests for early dev sanity checks
- Output Part 1 and Part 2

## Usage

### Using venv

```shell
python3 -m venv ./venv_adventofcode
```

```shell
source ./venv_adventofcode/bin/activate
```

### Installing Advent of Code Requirements

```shell
pip install -r requirements.txt
```

### Testing

![Tests](https://github.com/UnicodeTreason/AdventOfCode/blob/main/.github/workflows/tests.yml/badge.svg)

Run all tests

```shell
pytest
```

Run all unittest tests

```shell
python3 -m unittest discover -s tests/
```

Run a specific unittest test

```shell
python3 -m unittest tests/year2015/test_day01.py
```

### Running

Run module

```shell
python3 -m adventofcode
```

Run app.py

```shell
python3 ./adventofcode/year2015/day01.py
```

# AdventOfCode

A place to store my brain solution to Advent of Code problems.

## Solution Requirements

- Perform automated testing using provided test data by examples
- Output Part 1
- Output Part 2 when magic toggle is True

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

Ensure requirements in place

```shell
pip install -r requirements_dev.txt
```

![Tests](https://github.com/UnicodeTreason/AdventOfCode/actions/workflows/tests.yml/badge.svg)

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

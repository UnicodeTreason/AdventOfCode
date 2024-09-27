# AdventOfCode

A place to store my solutions to Advent of Code problems.

## Solution Requirements

- Automated testing using provided test data
- Output Part 1
- Output Part 2

Future

- Run entire module
- Entire module has nice output for each year/day

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

Run a specific pytest test

**Note: [Output flavours](https://docs.pytest.org/en/7.1.x/how-to/output.html#modifying-python-traceback-printing)**

```shell
pytest tests/year2015/test_day01.py
```

Run a specific unittest test

```shell
python3 -m unittest tests/year2015/test_day01.py
```

### Running

Run entire module

```shell
python3 -m adventofcode
```

Run specific day

```shell
python3 ./adventofcode/year2015/day01.py
```

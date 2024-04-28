# Leetcode solutions in Python

![Language](https://img.shields.io/badge/Language-Python3-success.svg?logo=Python&logoColor=yellow)
![Update](https://img.shields.io/badge/Update-Daily-success.svg)
![Test Cases](https://img.shields.io/badge/Tests-4-success.svg)
![Progress](https://img.shields.io/badge/Progress-4%2F300-critical.svg)

## Introduction

Solutions for some Leetcode problems in Python3.

| problem set                                                                                                    | Solution                                   | Status      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|-------------|
| [Leetcode 50 Common Interview Questions](media/Clean_Code_Handbook-LeetCode_50_Common_Interview_Questions.pdf) | [Leetcode Problems](leetcode_common_50.md) | In progress |
| [Blind 75](https://leetcode.com/list/oizxjoit)                                                                 |                                            | Not started |
| [Grind 75](https://leetcode.com/list/rab78cw1)                                                                 |                                            | Not started |
| [Grind 169](https://leetcode.com/list/rabvlt31)                                                                |                                            | Not started |
| [Neetcode 150](https://leetcode.com/list/rr2ss0g5)                                                             |                                            | Not started |
| [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/)                                                     |                                            | Not started |
| [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/)                                                     |                                            | Not started |
| [Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)                                         |                                            | Not started |
| All above of leetcode problems in python                                                                       | [Leetcode Problems](leetcode.md)           | In progress |
| [SQL 50](https://leetcode.com/studyplan/top-sql-50/)                                                           |                                            | Not started |

## Environment

This project is coded in:

- Python 3.11.9
- Pycharm 2024.1 with [codeium](https://codeium.com) plugin
- Python [Black](https://github.com/psf/black) formatter
- [codecov](https://codecov.io) coverage test

The test cases uses the default `pytest` framework.

use `python -m unittest` to run all tests
use `pytest --cov=solutions tests/` to run test coverage tests.
use `coverage html` to generate code coverage reports in html to `htmlcov/index.html`.

## Code Layout

- `solutions`: holds solutions.
  The code are in the same code format as the leetcode requires, with different method names (follow PEP 8 standard).

- `utils`: contains some of the utilities for the Leetcode solutions.

- `tests`: contains unit tests.

## Update History

- Apr. 2024 created repository
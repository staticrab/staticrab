# staticrab
[![Build Status](https://travis-ci.org/staticrab/staticrab.svg?branch=master)](https://travis-ci.org/staticrab/staticrab)
[![License: MIT](https://img.shields.io/github/license/staticrab/staticrab)](https://opensource.org/licenses/MIT)
[![Wheel?](https://img.shields.io/pypi/wheel/staticrab)](https://pypi.org/project/staticrab/)
[![Documentation](https://img.shields.io/readthedocs/staticrab)](https://staticrab.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Version](https://img.shields.io/pypi/v/staticrab)](https://pypi.org/project/staticrab/)
[![Python version: 3.8](https://img.shields.io/pypi/pyversions/staticrab)](https://www.python.org/)

A library for fast calculation of various correlation measures in python. The API is described in the [documentation](https://staticrab.readthedocs.io/).

The goal of this mini library is not to replace [Scipy stack](https://www.scipy.org/), [statsmodels](https://www.statsmodels.org/stable/index.html) nor [PyMC3](https://docs.pymc.io/) but rather to complement them.

## Main features
So far, this library implements only one function and that is the fast(ish) calculation of Chatterjee's correlation coefficient.

### Chatterjee's correlation coefficient
Chatterjee's correlation coefficient (also called Chatterjee's xi) is a recently proposed correlation coeffient that can be used for testing of nonlinear functional relationships between two variables (viz [original paper](https://arxiv.org/abs/1909.10140)).

## Installation
```
pip install staticrab
```

## Notes

This library is just a thin wrapper over the `staticrab-backend` for proper testing and documentation and it thus requires to have installed the `staticrab-backend` installed.

```
pip install staticrab-backend
```

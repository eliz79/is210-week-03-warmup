#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some numeric types."""

import decimal
import fractions

INTVAL = decimal.Decimal('1')
FLOATVAL = 0.1
DECVAL = decimal.Decimal('0.1')
FRACVAL = fractions.Fraction(1, 10)

print INTVAL, FLOATVAL, DECVAL, FRACVAL

# -*- coding: utf-8 -*-
"""
This wrapper module provides Python bindings for the library of compiled C
routines that form the core of QuakeMigrate:

    * Migrate onsets - This routine performs the continuous migration through \
    time and space of the onset functions. It has been parallelised with \
    openMP.
    * Find maximum coalescence - This routine finds the continuous maximum \
    coalescence amplitude in the 4-D coalesence volume.

"""

from .QMigratelib import migrate, find_max_coa

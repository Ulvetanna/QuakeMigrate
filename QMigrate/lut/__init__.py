# -*- coding: utf-8 -*-
"""
The :mod:`QMigrate.lut` module handles the definition and generation of the
traveltime lookup tables used in QuakeMigrate.

"""

from .create_lut import compute_traveltimes, read_nlloc  # NOQA
from .lut import LUT  # NOQA


def update_lut(old_lut_file, save_file):
    """
    Utility function to convert old-style LUTs to new-style LUTs.

    Parameters
    ----------
    old_lut_file : str
        Path to lookup table file to update.
    save_file : str, optional
        Output path for updated lookup table.

    """

    from QMigrate.io import read_lut

    lut = read_lut(old_lut_file)

    try:

        traveltimes = {}
        for station, phases in lut.maps.items():
            for phase, ttimes in phases.items():
                phase_code = phase.split("_")[1]
                traveltimes.setdefault(station, {}).update(
                    {phase_code: ttimes})
        lut.traveltimes = traveltimes
        del lut.maps
    except AttributeError:
        pass
    lut.phases = ["P", "S"]
    lut.fraction_tt = 0.1
    try:
        lut.node_spacing = lut.cell_size
        lut.node_count = lut.cell_count
        del lut._cell_size, lut._cell_count
    except AttributeError:
        pass

    lut.save(save_file)

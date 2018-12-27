# Copyright (C) 2018 Paul King

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version (the "AGPL-3.0+").

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License and the additional terms for more
# details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# ADDITIONAL TERMS are also included as allowed by Section 7 of the GNU
# Affrero General Public License. These aditional terms are Sections 1, 5,
# 6, 7, 8, and 9 from the Apache License, Version 2.0 (the "Apache-2.0")
# where all references to the definition "License" are instead defined to
# mean the AGPL-3.0+.

# You should have received a copy of the Apache-2.0 along with this
# program. If not, see <http://www.apache.org/licenses/LICENSE-2.0>.


import numpy as np
import os

# DISTANCE FUNCTIONS
from pymedphys.dose import make_dist_vals
from pymedphys.dose import get_dist_vals, get_dose_vals
# DOSE FUNCTIONS
from pymedphys.dose import make_dose_vals
from pymedphys.dose import get_dose_vals
# PROFILE FUNCTIONS
from pymedphys.dose import make_dose_prof
from pymedphys.dose import make_pulse_dose_prof
from pymedphys.dose import is_even_spaced
from pymedphys.dose import resample
from pymedphys.dose import align_to
from pymedphys.dose import is_wedged
from pymedphys.dose import is_fff
# SLICING FUNCTIONS
from pymedphys.dose import find_strt_stop
from pymedphys.dose import slice_dose_prof
from pymedphys.dose import find_edges
from pymedphys.dose import find_umbra
# SCALING FUNCTIONS
from pymedphys.dose import find_dose
from pymedphys.dose import find_dists
from pymedphys.dose import norm_dose_vals
from pymedphys.dose import norm_dist_vals
from pymedphys.dose import cent_dose_prof
# FLATNESS & SYMMETRY FUNCTIONS
from pymedphys.dose import flatness
from pymedphys.dose import symmetry
from pymedphys.dose import make_dose_prof_sym


DATA_DIRECTORY = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 os.pardir, 'data', 'doseprofile'))

PROFILER = [(-16.4, 0.22), (-16, 0.3), (-15.6, 0.28),
            (-15.2, 0.3), (-14.8, 0.36), (-14.4, 0.38),
            (-14, 0.41), (-13.6, 0.45), (-13.2, 0.47),
            (-12.8, 0.51), (-12.4, 0.55), (-12, 0.62),
            (-11.6, 0.67), (-11.2, 0.74), (-10.8, 0.81),
            (-10.4, 0.91), (-10, 0.97), (-9.6, 1.12),
            (-9.2, 1.24),
            (-8.8, 1.4), (-8.4, 1.56), (-8, 1.75), (-7.6, 2.06),
            (-7.2, 2.31), (-6.8, 2.56), (-6.4, 3.14), (-6, 3.83),
            (-5.6, 4.98), (-5.2, 8.17), (-4.8, 40.6), (-4.4, 43.34),
            (-4, 44.17), (-3.6, 44.44), (-3.2, 44.96), (-2.8, 44.18),
            (-2.4, 45.16), (-2, 45.54), (-1.6, 45.07), (-1.2, 45.28),
            (-0.8, 45.27), (-0.4, 44.57), (0, 45.23), (0.4, 45.19),
            (0.8, 45.18), (1.2, 45.37), (1.6, 45.34), (2, 45.39),
            (2.4, 45.32), (2.8, 45.25), (3.2, 44.84), (3.6, 44.76),
            (4, 44.23), (4.4, 43.22), (4.8, 39.14), (5.2, 7.98),
            (5.6, 4.89), (6, 3.71), (6.4, 3.11), (6.8, 2.59),
            (7.2, 2.27), (7.6, 1.95), (8, 1.71), (8.4, 1.46),
            (8.8, 1.35), (9.2, 1.18), (9.6, 1.11), (10, 0.93),
            (10.4, 0.87), (10.8, 0.78), (11.2, 0.7),
            (11.6, 0.64), (12, 0.6), (12.4, 0.54),
            (12.8, 0.49), (13.2, 0.47), (13.6, 0.43),
            (14, 0.4), (14.4, 0.39), (14.8, 0.34),
            (15.2, 0.33), (15.6, 0.32), (16, 0.3), (16.4, 0.3)]


# DISTANCE FUNCTIONS

def test_make_dist_vals():
    assert len(make_dist_vals(-16.4, 16.4, .4)) == len(PROFILER)


def test_get_dist_vals():
    assert get_dist_vals(PROFILER)[0] == -get_dist_vals(PROFILER)[-1]


# DOSE FUNCTIONS

def test_make_dose_vals():
    def dose_func(dist):
        return 1.0
    assert np.allclose(make_dose_vals(get_dist_vals(PROFILER), dose_func), 1.0)


def test_get_dose_vals():
    assert np.allclose(get_dose_vals(PROFILER)[-1], 0.3)


# PROFILE FUNCTIONS

def test_make_dose_prof():
    assert make_dose_prof(
        get_dist_vals(PROFILER), get_dose_vals(PROFILER)) == PROFILER


def test_is_even_spaced():
    print("test_is_even_spaced is not implemented")


def test_make_pulse_dose_prof():
    print('test_make_pulse_dose_prof is not implemented')  # STUB
    print(make_pulse_dose_prof())  # STUB


def test_resample():
    resampled = resample(PROFILER)
    increments = np.diff([i[0] for i in resampled])
    assert np.allclose(increments, 0.1)
    assert np.allclose(resampled[0], PROFILER[0])


def test_align_to():  # STUB  ######
    print(align_to(PROFILER, PROFILER))
    print("test_align_to is not implemented")

    #     """ """
    #     # DYNAMIC WEDGE, PROFILER -> TOMO_FILM PROFILE
    #     p = read.profiler(TEST[1]);  to_move = p[p.keys()[0]]
    #     f = read.tomo_film(TEST[2]); to_match= f[f.keys()[0]]
    #     r = move_to_match(to_move, to_match, 0.1)
    #     assert abs(r['shft'] - 9.3) < 0.1
    #     assert np.allclose(r['flp'], True)
    #     assert len(r['x1']) -len(r['y1']) + len(r['x2']) -len(r['y2']) == 0
    #     if True: # POPUP PLOT
    #         import pylab as plt
    #         kwargs = {'markersize': 1,  'markeredgewidth': 0.2, 'marker': 'o',
    #           'linestyle': '-', 'linewidth': .010, 'markeredgecolor': 'r',
    #           'markerfacecolor': 'r'}
    #         plt.plot(r['x1'],  r['y1'], **kwargs)
    #         kwargs['markeredgecolor'] = 'b'; kwargs['markerfacecolor'] = 'b'
    #         plt.plot(r['x2'],  r['y2'], **kwargs)
    #         plt.show()
    #     print 'move_to_match passed'


def test_is_wedged():  # STUB  ######
    print(is_wedged(PROFILER))
    print('test_is_wedged is not yet implemented')


def test_is_fff():  # STUB  ######
    print(is_fff(PROFILER))
    print('test_is_fff is not yet implemented')

# SLICING FUNCTIONS


def test_find_strt_stop():
    assert find_strt_stop(PROFILER, -10, 500) == (-10, 16.4)


def test_slice_dose_prof():
    assert slice_dose_prof(PROFILER) == PROFILER


def test_find_edges():
    assert np.allclose(find_edges(PROFILER), (-4.9, 5.0))


def test_find_umbra():
    assert np.isclose(find_umbra(PROFILER)[0][0], -3.6)


# SCALING FUNCTIONS

def test_find_dose():
    assert np.allclose(find_dose(PROFILER, 0.0), 45.23)


def test_find_dists():
    assert np.allclose(find_dists(PROFILER, 23), [-5.017083, 5.007189])


def test_norm_dose_vals():
    assert norm_dose_vals(PROFILER, 0.0)[41][1] == 100.0


def test_norm_dist_vals():
    assert np.isclose(norm_dist_vals(PROFILER)[0][0], 3.3469387755)


def test_cent_dose_prof():
    assert np.allclose(cent_dose_prof(PROFILER)[0][0], -16.45)

# FLATNESS & SYMMETRY FUNCTIONS


def test_flatness():  # STUB  ######
    assert np.allclose(flatness(PROFILER), 0.03020309)


def test_symmetry():
    assert np.allclose(symmetry(PROFILER), 0.014657383657017305)


def test_make_dose_prof_sym():
    symmetric = make_dose_prof_sym(PROFILER)
    assert symmetric[0][1] == symmetric[-1][1]


if __name__ == "__main__":
    # DISTANCE FUNCTIONS
    test_make_dist_vals()
    test_get_dist_vals()
    # DOSE FUNCTIONS
    test_make_dose_vals()
    test_get_dose_vals()
    # PROFILE FUNCTIONS
    test_make_dose_prof()
    test_is_even_spaced()
    test_make_pulse_dose_prof()
    test_resample()
    test_align_to()
    test_is_wedged()
    test_is_fff()
    # SLICING FUNCTIONS
    test_find_strt_stop()
    test_slice_dose_prof()
    test_find_edges()
    test_find_umbra()
    # SCALING FUNCTIONS
    test_find_dose()
    test_find_dists()
    test_norm_dose_vals()
    test_norm_dist_vals()
    test_cent_dose_prof()
    # FLATNESS & SYMMETRY FUNCTIONS
    test_flatness()
    test_symmetry()
    test_make_dose_prof_sym()

import pytest
import numpy as np
from quail.egg import Egg

def test_analysis_lagcrp():
    # example from kahana lab lag-crp tutorial
    presented=[[['1', '2', '3', '4', '5', '6', '7', '8']]]
    recalled=[[['8', '7', '1', '2', '3', '5', '6', '4']]]
    egg = Egg(pres=presented,rec=recalled)
    assert np.allclose(egg.analyze('lagcrp').data.values,np.array([[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.333333, 0.333333, np.nan, 0.75, 0.333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]), equal_nan=True)

def test_analysis_lagcrp_best_euclidean():
    presented=[[[10, 20, 30, 40, 50, 60, 70, 80]]]
    recalled=[[[81, 71, 11, 21, 31, 51, 61, 41]]]
    egg = Egg(pres=presented,rec=recalled)
    assert np.allclose(egg.analyze('lagcrp', match='best', distance='euclidean').data.values,np.array([[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.333333, 0.333333, np.nan, 0.75, 0.333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]), equal_nan=True)

def test_acc_best_euclidean_3d():
    presented=[[[[10, 0, 0], [20, 0, 0], [30, 0, 0], [40, 0, 0], [50, 0, 0],
                 [60, 0, 0], [70, 0, 0], [80, 0, 0]]]]
    recalled=[[[[81, 0, 0], [71, 0, 0], [11, 0, 0], [21, 0, 0], [31, 0, 0],
                [51, 0, 0], [61, 0, 0], [41, 0, 0]]]]
    egg = Egg(pres=presented,rec=recalled)
    assert np.allclose(egg.analyze('lagcrp', match='best', distance='euclidean').data.values,np.array([[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.333333, 0.333333, np.nan, 0.75, 0.333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]), equal_nan=True)

# def test_analysis_lagcrp_smooth_correlation():
#     presented=[[[10, 20, 30, 40, 50, 60, 70, 80]]]
#     recalled=[[[81, 71, 11, 21, 31, 51, 61, 41]]]
#     egg = Egg(pres=presented,rec=recalled)
#     assert np.allclose(egg.analyze('lagcrp', match='best', distance='euclidean').data.values,np.array([[0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.333333, 0.333333, np.nan, 0.75, 0.333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]), equal_nan=True)

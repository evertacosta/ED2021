import trabajo3
import numpy as np

def test_sobreamortiguado1():
    assert trabajo3.sobreamortiguado(9.0, 7.0, 10.0) == (12.70, 3.97)


def test_sobreamortiguado23():
    assert trabajo3.sobreamortiguado(5/2, 5/8, 1.0) == (10.0, 16.0)


def test_subamortiguado1():
    assert trabajo3.subamortiguado(4.0, 1/2, 10.0) == (25.0, 1594.76)


def test_subamortiguado25():
    assert trabajo3.subamortiguado(2.5, np.pi/2, 0.1) == (0.4, 2.0)

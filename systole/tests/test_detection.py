# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import numpy as np
import unittest
from unittest import TestCase
from systole.detection import oxi_peaks, rr_artefacts, interpolate_clipping
from systole import import_ppg
from systole.utils import simulate_rr


class TestDetection(TestCase):

    def test_oxi_peaks(self):
        """Test oxi_peaks function"""
        ppg = import_ppg('1')[0, :]  # Import PPG recording
        signal, peaks = oxi_peaks(ppg)
        assert len(signal) == len(peaks)
        assert np.all(np.unique(peaks) == [0, 1])

    def test_rr_artefacts(self):
        rr = simulate_rr()  # Import PPG recording
        artefacts = rr_artefacts(rr)
        artefacts = rr_artefacts(list(rr))
        assert all(
            350 == x for x in [len(artefacts[k]) for k in artefacts.keys()])

    def test_interpolate_clipping(self):
        ppg = import_ppg('1')[0]
        clean_signal = interpolate_clipping(ppg)
        assert clean_signal.mean().round() == 100
        clean_signal = interpolate_clipping(list(ppg))
        assert clean_signal.mean().round() == 100
        clean_signal = interpolate_clipping(ppg)
        ppg[0], ppg[-1] = 255, 255
        clean_signal = interpolate_clipping(ppg)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

import pytest
import numpy as np
import L2

class TestFunction:

    def test_L2_result(self):
        assert L2.L2([1.0, 2.0], [2.0, 3.0]) == 6.324555320336759

    def test_L2_length_mismatch(self):
        with pytest.raises(ValueError):
            L2.L2([1.0, 2.0, 3.0], [2.0, 3.0])

    def test_L2_weights_missed(self):
        assert L2.L2([1.0, 2.0]) == 2.0

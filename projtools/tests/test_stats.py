import numpy as np
from projtools import stats

def test_permutation_test():
    """Test the permutation test function."""
    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([6, 7, 8, 9, 10])

    actual_diff, fake_diffs, p_value = stats.permutation_test(group1, group2, n_iters=10_000)

    print(actual_diff, fake_diffs, p_value)

    assert actual_diff == -5.0
    assert fake_diffs.shape == (10_000,)
    assert 0.0 < p_value < 1.0

def test_permutation_test_same_group():
    """Test the permutation test function."""
    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([1, 2, 3, 4, 5])

    actual_diff, fake_diffs, p_value = stats.permutation_test(group1, group2, n_iters=15_000)

    print(actual_diff, fake_diffs, p_value)

    assert actual_diff == 0.0
    assert fake_diffs.shape == (15_000,)
    assert 0.55 < p_value < 0.6

def test_permutation_test_greater():
    """Test the permutation test function."""
    group1 = np.array([1, 2, 3, 4, 5])
    group2 = np.array([6, 7, 8, 9, 10])

    actual_diff, fake_diffs, p_value = stats.permutation_test(group1, group2, alternative='greater', n_iters=10_000)

    print(actual_diff, fake_diffs, p_value)

    assert actual_diff == -5.0
    assert fake_diffs.shape == (10_000,)
    assert 0.001 < p_value < 0.01

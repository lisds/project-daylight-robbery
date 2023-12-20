import numpy as np
rng = np.random.default_rng()

def permutation_test(group1,
                     group2,
                     alternative='greater',
                     n_iters=10_000) -> (float, np.array, float):
    """Perform a permutation test.

    Parameters
    ----------
        group1: pd.Series
            A series of values for group 1
        group2: pd.Series
            A series of values for group 2
        alternative: str
            One of 'greater' or 'less' (default: 'greater')
        n_iters: int
            Number of iterations to perform
    
    Returns
    ----------
        actual_diff: float
            Actual difference in means
        fake_diffs: np.array
            Array of fake differences in means
        p_value: float
            Proportion of fake differences that are greater than or equal to the actual difference
    """

    actual_diff = np.mean(group1) - np.mean(group2)
    pooled = np.concatenate([group1, group2])

    n_subjects = len(group1)
    fake_diffs = np.zeros(n_iters)

    for index in range(n_iters):
        shuffled = rng.permuted(pooled)

        fake_group1_mean = np.mean(shuffled[:n_subjects])
        fake_group2_mean = np.mean(shuffled[n_subjects:])

        fake_diff = fake_group1_mean - fake_group2_mean
        fake_diffs[index] = fake_diff

    n_alt = 0
    if alternative == 'greater':
        n_alt = np.count_nonzero(fake_diffs <= actual_diff)
    elif alternative == 'less':
        n_alt = np.count_nonzero(fake_diffs >= actual_diff)

    return actual_diff, fake_diffs, n_alt / n_iters

import numpy as np
import pandas as pd
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
            The p-value for the test
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

def better_permutation_test(group1, #pylint: disable=too-many-locals
                     group2,
                     alternative='greater',
                     n_iters=10_000) -> (float, np.array, float):
    """Perform a permutation test. This test randomly assigns the total number of crimes to a month.
    
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
            The p-value for the test
    """

    actual_diff = np.mean(group1) - np.mean(group2)

    n_subjects = len(group1)
    fake_diffs = np.zeros(n_iters)
    total = int(np.sum(group1) + np.sum(group2))
    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

    for index in range(n_iters):
        shuffled_observations = np.random.choice(months, total)
        shuffled_obs_dict = {"01": [],"02": [],"03": [],"04": [],"05": [],"06": [],"07": [],"08": [],"09": [],"10": [],"11": [],"12": []} #pylint: disable=line-too-long
        for index2, key in enumerate(shuffled_obs_dict): #pylint: disable=unused-variable
            shuffled_obs_dict[key] = np.count_nonzero(shuffled_observations == key)

        shuffled_obs_group1_mean = np.mean(pd.Series(shuffled_obs_dict).iloc[:n_subjects])
        shuffled_obs_group2_mean = np.mean(pd.Series(shuffled_obs_dict).iloc[n_subjects:])

        fake_diffs[index] = shuffled_obs_group1_mean - shuffled_obs_group2_mean

    n_alt = 0
    if alternative == 'greater':
        n_alt = np.count_nonzero(fake_diffs <= actual_diff)
    elif alternative == 'less':
        n_alt = np.count_nonzero(fake_diffs >= actual_diff)

    return actual_diff, fake_diffs, n_alt / n_iters

import pandas as pd

def calculate_cumulative_family_frequencies(raw_family_abundance: pd.DataFrame) -> dict[str, float]:
    """Calculate cumulative frequency of each Family when separated by Genus

    In the original data of Alfano, the Family data rows are broken up by Genus.
    This function "un-pivots" the Family rows.

    Args:
    - raw_family_abundance: 0th column must contain the Family name while 2nd column
        holds relative abundance. Can contain however many rows

    Returns:
    - dict mapping Family name (str) to cumulative abundance (float)
    """
    family_abundance: dict[str, float] = dict()

    for i in range(len(raw_family_abundance)):
        if (fam := raw_family_abundance.iloc[i, 0]) not in family_abundance.keys():
            family_abundance[fam] = float(raw_family_abundance.iloc[i, 2])
        else:
            family_abundance[fam] += float(raw_family_abundance.iloc[i, 2])

    return family_abundance
import pandas as pd

def percentage(df, col1, col2):
    """Calculate percentage crosstab of two columns."""
    crosstab_percentage = (
        pd.crosstab(
            df[col1],
            df[col2],
            normalize="index",
            margins=True,
            margins_name="Total",
        ) * 100
    )
    return crosstab_percentage.applymap(lambda x: f"{x:.1f}%")

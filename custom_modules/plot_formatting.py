import matplotlib.pyplot as plt

def percentage_stacked_bars(plot, threshold=0):
    """Add percentage numbers to stacked bar plot."""
    for p in plot.patches:
        width = p.get_width()
        height = p.get_height()
        x = p.get_x() + width / 2
        y = p.get_y() + height / 2

        if height > threshold:
            plot.text(x, y, f'{height:.0f}%', ha="center", va="center", fontsize=7)
 

def ci_bar(counts_df, group="group"):
    """Plot confidence intervals on bar plot."""
    plt.errorbar(
        x=counts_df[group],
        y=counts_df["proportion"],
        yerr=[
            counts_df["proportion"] - counts_df["ci_lower"],
            counts_df["ci_upper"] - counts_df["proportion"],
        ],
        fmt="none",
        capsize=5,
        color="black",
    )


def estimates_bar(counts_df, bar_plot):
    """Add proportion estimates and confidence intervals to bar plot."""
    for index, row in counts_df.iterrows():
        bar_plot.text(
            index + 0.1,
            row["proportion"],
            f"{row['proportion']:.1%}",
            color="black",
            ha="left",
            va="bottom",
            fontweight="bold",
            fontsize=11,
        )
        ci_text = f"{row['ci_lower']:.1%} - {row['ci_upper']:.1%}"
        bar_plot.text(
            index,
            row["proportion"] - 0.035,
            ci_text,
            color="black",
            ha="center",
            va="top",
            fontstyle="oblique",
        )

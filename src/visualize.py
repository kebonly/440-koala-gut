from typing import Optional
import pandas as pd
import matplotlib

# VISUALIZATION PARAMETERS
THRESHOLD_ABUNDANCE_PIE = 5 # Minimum relative abundance to be included on pie chart

def plot_family_abundance(family_abundance: dict[str, float], dest_fig: Optional[str]) -> matplotlib.figure.Figure:
    """Produce Pie Chart of relative abundance of various Families

    Args:
    - family_abundance: dict containing family name and corresponding relative abundance
    - dest_fig: where the output pie chart figure will be saved

    Returns:
    - matplotlib.figure.Figure containing the axes on which the pie chart is plotted
    """
    family_abundance_ordered = family_abundance.items() # intermediate variable to guarantee order
    data = {
        "Abundance": [abun for _, abun in family_abundance_ordered 
            if abun > THRESHOLD_ABUNDANCE_PIE]
    }
            
    df_family_abundance = pd.DataFrame(
        data=data, 
        index=[fam for fam, abun in family_abundance_ordered 
            if abun > THRESHOLD_ABUNDANCE_PIE]
    )

    ax_family_abundance = df_family_abundance.plot.pie(
        y="Abundance",
        title="Relative abundance of prevalent bacterial families",
        ylabel="",
        legend=False
    )

    fig = ax_family_abundance.get_figure()
    if dest_fig:
        try:
            fig.savefig(dest_fig)
        except Exception as err:
            print(err)
            print("Tip: Make sure dest_fig is a path with respect to the project's root directory")

    return fig
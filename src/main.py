import pandas as pd
import matplotlib.pyplot as plt

import analysis
import visualize

if __name__ == "__main__":
    otu_relative_abundance = pd.read_excel(
        io="./raw_data/alfano-supp-table.xlsx", 
        sheet_name="Sheet1")

    family_abundance = analysis.calculate_cumulative_family_frequencies(
        raw_family_abundance=otu_relative_abundance)

    fig_koala_gut_family = visualize.plot_family_abundance(
        family_abundance=family_abundance, 
        dest_fig="./fig/Koala_Gut_Family_Pie_Chart.png")
# Results Documentation

This repository contains the results and visualizations for the experiments done using PushNPull algorithms. The experiments analyze switching ratios and PushNPull algorithm experiment performance metrics. Below is an overview of the files and their purposes.

---

## Folder Structure

### `switching_ratio_comparison`
This folder contains data and visualizations related to the comparison of switching ratios.

- **`all_switching_ratios.xlsx`**: Excel file containing detailed data on switching ratios across different scenarios.
- **`avg_calls_vs_switching_ratio.png`**: A plot showing the average number of calls versus switching ratios.
- **`avg_rounds_vs_switching_ratio.png`**: A plot showing the average number of rounds versus switching ratios.

### `plots_hybrid_experiment`
This folder contains data and visualizations for the  experiment, organized into subfolders.

#### Subfolders (`0/`, `0_1/`, `0_2/`, ..., `1/`)
Each subfolder contains all plots and data produced for specific switching ratio configurations.

#### Main Files
- **`avg_calls_vs_n.png`**: A plot showing the average number of calls as a function of `n`.
- **`avg_rounds_vs_n.png`**: A plot showing the average number of rounds as a function of `n`.
- **`boxplot_calls_vs_n.png`**: A boxplot visualizing the distribution of calls for different values of `n`.
- **`boxplot_rounds_vs_n.png`**: A boxplot visualizing the distribution of rounds for different values of `n`.
- **`ratio_avg_rounds_vs_log_n`**: A plot showing the average number of rounds (normalized by $\log n$) as a function of `n`.
- **`rounds_data.csv`**: CSV file containing raw data for the number of rounds across $10^4$ runs.
- **`calls_data.csv`**: CSV file containing raw data for the number of calls across across $10^4$ runs.
- **`combined_distribution_n_10_ratio_0.00.png`**: A combined distribution plot for `n=10` and a switching ratio of `0.00`.
---

## Overview of Experiments

### Switching Ratio Comparison
The switching ratio comparison experiment evaluates the relationship between switching ratios and performance metrics such as the average number of calls and rounds. The results are visualized in the `switching_ratio_comparison` folder.

### Hybrid Experiment
The experiment investigates the performance of a hybrid approach under varying conditions. The results are organized in the `plots_hybrid_experiment` folder, with subfolders representing different configurations.

---

## How to Use This Repository

1. **Explore Data**: Use the Excel and CSV files to analyze raw data.
2. **View Visualizations**: Open the `.png` files to view the plots and distributions.
3. **Presentation**: Refer to the `PushNPull_experiments.pptx` file for a summary of the experiments and key findings.

---

## Additional Notes

- Ensure you have a compatible viewer for `.xlsx` and `.csv` files.
- The plots are best viewed using an image viewer that supports `.png` format.
- These results were prepared by **`Havi Bohra (210429), UG Y21 MTH`**
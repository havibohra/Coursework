import numpy as np
import random
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import logging
import os  
import pandas as pd 
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def simulate_rumor_spread(n, switching_ratio, source=0):
    """
    Simulate the rumor spreading process on a set of n people.
    """
    switching_point = int(n * switching_ratio)
    if switching_point < 1: 
        switching_point = 1
    elif switching_point > n:
        switching_point = n

    informed = set([source])
    
    rounds = 0
    calls = 0

    # First phase: Push phase
    # Informed people call uninformed people
    while len(informed) < n and len(informed) < switching_point:
        temp_new = set()
        for person in informed:
            while True:
                target = random.randint(0, n - 1)
                if target != person:
                    break
                
            if target not in informed:
                temp_new.add(target)

            calls += 1

        rounds += 1
        informed.update(temp_new)
    
    uninformed = set(range(n)) - informed
    # Second phase: Pull phase
    # Uninformed people call informed people
    while len(informed) < n:
        temp_new = set()
        for person in uninformed:
            while True:
                target = random.randint(0, n - 1)
                if target != person:
                    break

            if target in informed:
                temp_new.add(person)    

            calls += 1

        rounds += 1
        informed.update(temp_new)
        uninformed -= temp_new

    return rounds, calls

def experiment_for_n(n, switching_ratio, num_trials=1000):
    """
    Run the rumor-spreading simulation num_trials times for a given n in parallel.
    Return the list of rounds needed for full spread and a sample progression.
    """
    logging.info(f"Starting {num_trials} trials for n = {n}")
    results = Parallel(n_jobs=-1)(
        delayed(simulate_rumor_spread)(n, switching_ratio) for _ in range(num_trials)
    )
    logging.info(f"Completed all {num_trials} trials for n = {n}")
    rounds_list = [result[0] for result in results]
    # Save the number of calls made in the first trial
    calls_made_list = [result[1] for result in results]
    
    return rounds_list, calls_made_list

def configure_plot(title, xlabel, ylabel, xscale=None, yscale=None):
    """
    Helper function to configure plots.
    """
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if xscale:
        plt.xscale(xscale)
    if yscale:
        plt.yscale(yscale)
    plt.grid(True, linestyle='--', alpha=0.7)

def main():

    # Define the set of n values to test and number of trials per n.
    n_values = [10, 100, 500, 1000, 10000, 100000, 1000000] 
    switching_ratios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # Test ratios from 0.2 to 0.8
    num_trials = 10000

    # Constants for tail probability analysis:
    c_exp = 2  # We compare against a bound of 1/n^c, here c = 2

    for switching_ratio in switching_ratios:
        output_folder = "results/plots_hybrid_experiment/" + str(switching_ratio).replace('.', '_')
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        results_df = pd.DataFrame(columns=[ 
            "n",
            "Average Rounds", 
            "Minimum Rounds",
            "Maximum Rounds",
            "log(n)", 
            "Ratio (Avg Rounds / log(n))",
            "Theoretical Bound (1/n^2)",
            "Average Calls",
            "nlog(n)"
        ])

        rounds_data = []
        calls_data = []

        excel_file = os.path.join(output_folder, "results.xlsx")

        logging.info(f"Starting experiments for switching ratio = {switching_ratio}")
        for n in n_values:
            logging.info(f"Starting experiments for n = {n} with switching ratio = {switching_ratio}")
            rounds_list, calls_made_list = experiment_for_n(n, switching_ratio, num_trials)
            mean_rounds = np.mean(rounds_list)
            log_n = np.log2(n)
            nlog_n = n * log_n
            rounds_to_log_ratio = mean_rounds / log_n  # Renamed for clarity
            theoretical_bound = 1 / (n ** c_exp)
            mean_calls = np.mean(calls_made_list)

            for rounds in rounds_list:
                rounds_data.append({"n": n, "switching_ratio": switching_ratio, "rounds": rounds})

            for calls in calls_made_list:
                calls_data.append({"n": n, "switching_ratio": switching_ratio, "calls": calls})

            logging.info(f"n = {n}, switching_ratio = {switching_ratio}: Average rounds = {mean_rounds:.2f}, log(n) = {log_n:.2f}, Ratio = {rounds_to_log_ratio:.2f}")

            # Create a combined figure with two subplots
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
            
            # Rounds distribution subplot
            ax1.hist(rounds_list, bins='auto', color='skyblue', edgecolor='black', alpha=0.7)
            ax1.set_title(f"Distribution of Rounds (n={n})")
            ax1.set_xlabel("Number of Rounds")
            ax1.set_ylabel("Frequency")
            ax1.grid(True, linestyle='--', alpha=0.7)
            
            # Calls distribution subplot
            ax2.hist(calls_made_list, bins='auto', color='orange', edgecolor='black', alpha=0.7)
            ax2.set_title(f"Distribution of Calls (n={n})")
            ax2.set_xlabel("Number of Calls")
            ax2.set_ylabel("Frequency")
            ax2.grid(True, linestyle='--', alpha=0.7)
            
            plt.suptitle(f"Distribution of Rounds and Calls (n={n}, switching ratio={switching_ratio:.2f})")
            plt.tight_layout()
            plt.savefig(os.path.join(output_folder, f"combined_distribution_n_{n}_ratio_{switching_ratio:.2f}.png"))
            plt.close()

            results_df = pd.concat([
                results_df,
                pd.DataFrame([{
                    "n": n,
                    "Average Rounds": mean_rounds,
                    "Minimum Rounds": np.min(rounds_list),
                    "Maximum Rounds": np.max(rounds_list),
                    "log(n)": log_n,
                    "Ratio (Avg Rounds / log(n))": rounds_to_log_ratio,
                    "Theoretical Bound (1/n^2)": theoretical_bound,
                    "Average Calls": mean_calls,
                    "nlog(n)": nlog_n
                }])
            ], ignore_index=True)

            # Save the updated DataFrame to the Excel file
            results_df.to_excel(excel_file, index=False)
            logging.info(f"Results for n = {n} saved to {excel_file}")

        # Step 3: One-time DataFrame conversion (very fast)
        rounds_data = pd.DataFrame(rounds_data)
        calls_data = pd.DataFrame(calls_data)
        # Save the DataFrames to CSV files
        rounds_data.to_csv(os.path.join(output_folder, "rounds_data.csv"), index=False)
        calls_data.to_csv(os.path.join(output_folder, "calls_data.csv"), index=False)   

        rounds_data["n"] = rounds_data["n"].astype(str)
        calls_data["n"] = calls_data["n"].astype(str)
        rounds_data["rounds"] = rounds_data["rounds"].astype(int)
        calls_data["calls"] = calls_data["calls"].astype(int)

        # Save average rounds vs. n plot
        plt.figure(figsize=(8, 5))
        plt.plot(n_values, results_df["Average Rounds"], marker='o', linestyle='-', color='red', label='Average rounds')
        plt.plot(n_values, results_df["log(n)"], marker='x', linestyle='--', color='green', label='log(n)')
        plt.plot(n_values, 2*results_df["log(n)"], marker='x', linestyle='--', color='blue', label='2*log(n)')
        configure_plot("Average Rounds vs. n", "Number of People (n)", "Rounds", xscale='log')
        plt.legend()
        plt.savefig(os.path.join(output_folder, "avg_rounds_vs_n.png"))  # Save the plot
        plt.close()

        # Step 2: Plot boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=rounds_data, x='n', y='rounds', hue='n', palette='viridis', legend=False)
        configure_plot("Distribution of Rounds for Different n", "Number of People (n)", "Rounds")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, "boxplot_rounds_vs_n.png"))  # Save the plot
        plt.close()

        # Save ratio of average rounds to log(n) vs. n plot
        plt.figure(figsize=(8, 5))
        plt.plot(n_values, results_df["Ratio (Avg Rounds / log(n))"], marker='o', linestyle='-', color='purple')
        configure_plot("Ratio: Average Rounds / log(n) vs. n", "Number of People (n)", "Average rounds / log(n)", xscale='log')
        plt.savefig(os.path.join(output_folder, "ratio_avg_rounds_vs_log_n.png"))  # Save the plot
        plt.close()

        # Save Average Calls vs. n (with nlog(n) reference) plot
        plt.figure(figsize=(8, 5))
        plt.plot(n_values, results_df["Average Calls"], marker='o', linestyle='-', color='orange', label ='Average Calls')
        plt.plot(n_values, results_df["nlog(n)"], marker='x', linestyle='--', color='blue', label='nlog(n)')
        plt.plot(n_values, results_df["n"] * np.log2(results_df["log(n)"]), marker='s', linestyle='-', color='green', label='n log(log(n))')

        # Annotate each point on the Average Calls line
        for i, n in enumerate(n_values):
            avg_calls = results_df["Average Calls"][i]
            plt.text(n, avg_calls, f"({n}, {avg_calls:.2f})", fontsize=8, ha='left', color='orange')

        # Annotate each point on the nlog(n) line
        for i, n in enumerate(n_values):
            nlog_n = results_df["nlog(n)"][i]
            plt.text(n, nlog_n, f"({n}, {nlog_n:.2f})", fontsize=8, ha='right', color='blue')

        plt.legend()
        configure_plot("Average Calls vs. n", "n", "Average Calls", xscale='log', yscale= 'log')
        plt.savefig(os.path.join(output_folder, "avg_calls_vs_n.png"))  # Save the plot
        plt.close()

        # Save boxplot for calls made
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=calls_data, x='n', y='calls', hue='n', palette='viridis', legend=False)
        configure_plot("Distribution of Calls Made for Different n", "Number of People (n)", "Total Calls (log scale)", yscale='log')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, "boxplot_calls_vs_n.png"))  # Save the plot
        plt.close()
    
    # Add comparative analysis across different switching ratios
    logging.info("Creating comparative plots for different switching ratios...")
    
    # Create a new directory for the comparative analysis
    comparative_output = "results/switching_ratio_comparison"
    if not os.path.exists(comparative_output):
        os.makedirs(comparative_output)
    
    # Collect data from all switching ratios
    all_ratio_data = []
    
    for switching_ratio in switching_ratios:
        ratio_folder = "results/plots_hybrid_experiment/" + str(switching_ratio).replace('.', '_')
        excel_file = os.path.join(ratio_folder, "results.xlsx")
        
        if os.path.exists(excel_file):
            df = pd.read_excel(excel_file)
            df['Switching Ratio'] = switching_ratio  # Add switching ratio column
            all_ratio_data.append(df)
    
    if all_ratio_data:
        # Combine all data
        combined_df = pd.concat(all_ratio_data, ignore_index=True)
        
        # Save the combined data
        combined_df.to_excel(os.path.join(comparative_output, "all_switching_ratios.xlsx"), index=False)
        
        # Plot average rounds vs switching ratio for each n
        plt.figure(figsize=(12, 8))
        for n in n_values:
            n_data = combined_df[combined_df['n'] == n]
            if not n_data.empty:
                plt.plot(n_data['Switching Ratio'], n_data['Average Rounds'], 
                         marker='o', linestyle='-', label=f'n={n}')
        
        configure_plot("Average Rounds vs Switching Ratio", 
                      "Switching Ratio", "Average Rounds")
        plt.legend(title="Network Size")
        plt.tight_layout()
        plt.savefig(os.path.join(comparative_output, "avg_rounds_vs_switching_ratio.png"))
        plt.close()
        
        # Plot average calls vs switching ratio for each n
        plt.figure(figsize=(12, 8))
        for n in n_values:
            n_data = combined_df[combined_df['n'] == n]
            if not n_data.empty:
                plt.plot(n_data['Switching Ratio'], n_data['Average Calls'], 
                         marker='o', linestyle='-', label=f'n={n}')
        
        configure_plot("Average Calls vs Switching Ratio", 
                      "Switching Ratio", "Average Calls", yscale='log')
        plt.legend(title="Network Size")
        plt.tight_layout()
        plt.savefig(os.path.join(comparative_output, "avg_calls_vs_switching_ratio.png"))
        plt.close()
        
        logging.info(f"Comparative analysis complete. Results saved to {comparative_output}")
    else:
        logging.warning("No data found for comparative analysis")

    logging.info("All plots and data saved successfully.")

if __name__ == '__main__':
    main()
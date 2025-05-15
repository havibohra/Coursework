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

def simulate_rumor_spread(n, source=0):
    """
    Simulate the rumor spreading process on a set of n people.
    """
    informed = set([source])
    rounds = 0
    calls = 0

    while len(informed) < n:
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

    return rounds, calls

def experiment_for_n(n, num_trials=1000):
    """
    Run the rumor-spreading simulation num_trials times for a given n in parallel.
    Return the list of rounds needed for full spread and a sample progression.
    """
    logging.info(f"Starting {num_trials} trials for n = {n}")
    results = Parallel(n_jobs=-1)(
        delayed(simulate_rumor_spread)(n) for _ in range(num_trials)
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

def plot_tail_probability_vs_K(n, rounds_list, K_values ):
    """
    Plots tail probability P(T > K log(n)) vs. K for a given n.
    
    Parameters:
        n (int): Number of people.
        rounds_list (list): List of rounds needed for full spread in each trial.
        K_values (list): List of K values to test.
    """

    # Plot
    plt.figure(figsize=(8, 5))
    tail_probs = []
    round_array = np.array(rounds_list)
    for k in K_values:
        threshold = k * np.log2(n)
        tail_prob = np.sum(round_array > threshold) / len(rounds_list)
        tail_probs.append(tail_prob)

    plt.plot(K_values, tail_probs, marker='o', linestyle='-', color='blue', label=f"Empirical P(T > K log(n)) for n={n}")
    
    plt.axhline(1 / (n**2), color='r', linestyle='--', label="Theoretical Bound (1/n²)")
    plt.grid(True, linestyle='--', alpha=0.7)
    configure_plot(f"Tail Probability vs. K for n={n}", "K (Multiplier of log(n))", "Tail Probability P(T > K log(n))", yscale='log')
    plt.legend()

    

def main():
    # Create a folder called "plots" to save all the plots
    output_folder = "results/plots_push"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the set of n values to test and number of trials per n.
    n_values = [10, 100, 500, 1000, 10000, 100000, 1000000] 
    num_trials = 100000

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

    # Constants for tail probability analysis:
    c_exp = 2  # We compare against a bound of 1/n^c, here c = 2

    excel_file = os.path.join(output_folder, "results.xlsx")
    

    for n in n_values:
        logging.info(f"Starting experiments for n = {n}")
        rounds_list, calls_made_list = experiment_for_n(n, num_trials)
        mean_rounds = np.mean(rounds_list)
        log_n = np.log2(n)
        nlog_n = n * log_n
        ratio = mean_rounds / log_n
        theoretical_bound = 1 / (n ** c_exp)
        mean_calls = np.mean(calls_made_list)

        for rounds in rounds_list:
            rounds_data.append({"n": n, "rounds": rounds})

        for calls in calls_made_list:
            calls_data.append({"n": n, "calls": calls})

        logging.info(f"n = {n}: Average rounds = {mean_rounds:.2f}, log(n) = {log_n:.2f}, Ratio = {ratio:.2f}")

        # Save histogram for distribution of rounds for each n
        plt.figure(figsize=(8, 5))
        plt.hist(rounds_list, bins='auto', color='skyblue', edgecolor='black', alpha=0.7)
        configure_plot(f"Distribution of Rounds for n = {n}", "Number of Rounds", "Frequency")
        plt.savefig(os.path.join(output_folder, f"histogram_n_{n}.png"))  # Save the plot
        plt.close()

        # Plot tail probability vs. K for this n
        K_values = np.linspace(1.5, 3, 200)
        plot_tail_probability_vs_K(n, rounds_list, K_values)
        plt.savefig(os.path.join(output_folder, f"tail_probability_vs_K_n_{n}.png"))  # Save the plot
        plt.close()

        # plot distribution of no. of calls made
        plt.figure(figsize=(8, 5))
        plt.hist(calls_made_list, bins='auto', color='orange', edgecolor='black', alpha=0.7)
        configure_plot(f"Distribution of Calls Made for n = {n}", "Number of Calls", "Frequency")
        plt.savefig(os.path.join(output_folder, f"calls_distribution_n_{n}.png"))  # Save the plot
        plt.close()

        results_df = pd.concat([
            results_df,
            pd.DataFrame([{
                "n": n,
                "Average Rounds": mean_rounds,
                "Minimum Rounds": np.min(rounds_list),
                "Maximum Rounds": np.max(rounds_list),
                "log(n)": log_n,
                "Ratio (Avg Rounds / log(n))": ratio,
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
    
    logging.info("All experiments completed and saved.")    
        
if __name__ == '__main__':
    main()
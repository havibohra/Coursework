import numpy as np
import random
import matplotlib.pyplot as plt
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
    informed_progress = [len(informed)]
    uninformed = set(range(n)) - informed
    rounds = 0
    calls = 0
    eff_calls = 0
    calls_list = []
    eff_calls_list = []

    while len(informed) < n:
        temp_new = set()
        curr_round_calls = 0 
        for person in uninformed:
            while True:
                target = random.randint(0, n - 1)
                if target != person:
                    break
                
            if target in informed:
                temp_new.add(person)

            calls += 1
            curr_round_calls += 1

        eff_calls += len(temp_new)  # Count effective calls made
        calls_list.append(curr_round_calls)  # Store calls made in this round
        eff_calls_list.append(len(temp_new))  # Store effective calls made in this round
        rounds += 1
        informed.update(temp_new)
        uninformed -= temp_new
        informed_progress.append(len(informed))

    return rounds, calls_list, eff_calls_list, informed_progress

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
    # Create a folder called "plots" to save all the plots
    output_folder = "results_plots/plots_pull"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the set of n values to test and number of trials per n.

    n_values = [10, 100, 500, 1000, 10000, 100000, 1000000 ]  # For a sample progression plot

    for n in n_values:
        logging.info(f"Starting experiments for n = {n}")
        rounds, calls_list, eff_calls_list, sample_progress = simulate_rumor_spread(n)
        
        # Plot effective calls in each round
        plt.figure(figsize=(10, 6))
        plt.xticks(ticks=range(1, rounds + 1))  # Annotate all rounds on the x-axis
        plt.plot(range(1, rounds+1), calls_list , marker='o', label='Total Calls per Round')
        plt.plot(range(1, rounds+1), eff_calls_list , marker='o', label='Effective Calls per Round')
        
        configure_plot(
            title=f"Effective Calls per Round (n={n})",
            xlabel="Round",
            ylabel="Number of Effective Calls",
            yscale='log'
        )
        plt.legend()
        plt.savefig(f"{output_folder}/effective_calls_n_{n}.png")
        plt.close()

        # Plot the ratio of effective calls to total calls per round
        plt.figure(figsize=(10, 6))
        ratios = [eff / total if total > 0 else 0 for eff, total in zip(eff_calls_list, calls_list)]
        plt.xticks(ticks=range(1, rounds + 1))  # Annotate all rounds on the x-axis
        plt.plot(range(1, rounds + 1), ratios, marker='o', label='Effective Calls / Total Calls per Round')
        configure_plot(
            title=f"Ratio of Effective Calls to Total Calls per Round (n={n})",
            xlabel="Round",
            ylabel="Ratio",
            yscale='log'  
        )
        plt.legend()
        plt.savefig(f"{output_folder}/ratio_eff_calls_n_{n}.png")
        plt.close()

        # Save progression of informed people for n
        rounds_axis = list(range(len(sample_progress)))
        plt.figure(figsize=(8, 5))
        plt.plot(rounds_axis, sample_progress, marker='o', linestyle='-', color='blue')
        configure_plot(f"Progression of Informed People for n = {n}", "Round (t)", "Number of Informed People I(t)")
        plt.savefig(os.path.join(output_folder, f"progression_n_{n}.png"))  # Save the plot
        plt.close()
    
    logging.info("All experiments completed and saved.")    
        
if __name__ == '__main__':
    main()
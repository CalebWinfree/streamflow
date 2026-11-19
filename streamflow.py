from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_streamflow(filename):
    """Read the streamflow CSV and return dates and flows (cfs), one column per gauge."""
    csv_path = Path(filename)
    if not csv_path.is_absolute():
        csv_path = Path(__file__).with_name(filename)

    streamflow_df = pd.read_csv(csv_path)
    dates = pd.to_datetime(streamflow_df["Site Number:"])
    flows = streamflow_df.iloc[:, 1:].to_numpy(dtype=float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot each gauge's flow with the June 2021 homework formatting."""
    plt.figure(figsize=(12, 6))
    for column, site in enumerate(sites):
        plt.plot(dates, flows[:, column], label=f"Site {site}")

    plt.title("June 2021 Provo River Streamflow Rates")
    plt.xlabel("Date & Time")
    plt.ylabel("Streamflow Rate")
    plt.xticks(dates[::96], rotation=45)
    plt.grid(True, linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


def summarize(dates, flows, sites):
    # Excel check for gauge 10163000: MAX = 131 cfs; AVERAGE = 56.9523611111113 cfs.
    summary = []
    print(
        f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<19}   "
        f"{'Min (cfs)':>10}   {'Avg (cfs)':>9}"
    )

    for column, site in enumerate(sites):
        site_flows = flows[:, column]
        max_index = int(np.argmax(site_flows))
        max_flow = np.max(site_flows)
        date_of_max = pd.Timestamp(dates[max_index]).strftime("%Y-%m-%d %H:%M")
        min_flow = np.min(site_flows)
        avg_flow = np.mean(site_flows)

        print(
            f"{site:<12}{max_flow:10.1f}   {date_of_max:<19}   "
            f"{min_flow:10.1f}   {avg_flow:9.1f}"
        )
        summary.append(
            {
                "Gauge": site,
                "Max (cfs)": max_flow,
                "Date of max": date_of_max,
                "Min (cfs)": min_flow,
                "Avg (cfs)": avg_flow,
            }
        )

    summary_path = Path(__file__).with_name("streamflow_summary.csv")
    pd.DataFrame(summary).to_csv(summary_path, index=False)


if __name__ == "__main__":
    sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
    dates, flows = load_streamflow(
        "June-2021-Provo-River-Streamflow-Rates (1).csv"
    )
    threshold = float(input("Enter a flow threshold in cfs: "))
    print(f"\nHours above {threshold:g} cfs in June 2021:")
    for column, site in enumerate(sites):
        # Count readings above the threshold and convert each 15-minute reading to 0.25 hours.
        hours_above = np.sum(flows[:, column] > threshold) * 0.25
        print(f"Gauge {site}: {hours_above:.2f} hours")

    plot_streamflow(dates, flows, sites)
    summarize(dates, flows, sites)

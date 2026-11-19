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


if __name__ == "__main__":
    sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
    dates, flows = load_streamflow(
        "June-2021-Provo-River-Streamflow-Rates (1).csv"
    )
    plot_streamflow(dates, flows, sites)

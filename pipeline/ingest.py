#!/usr/bin/env python

import sys
import pandas as pd


def ingest(input_csv: str, output_csv: str = "data_raw.csv") -> None:
    df = pd.read_csv(input_csv)
    df.to_csv(output_csv, index=False)
    print("Saved a raw copy as data_raw.csv.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <input_csv>")
        sys.exit(1)

    ingest(sys.argv[1])


if __name__ == "__main__":
    main()

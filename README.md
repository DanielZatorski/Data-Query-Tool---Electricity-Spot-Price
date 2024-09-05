# Data Query Tool for EnergiDataService

## Overview

The Data Query Tool is a Python-based application that leverages the [EnergiDataService](https://www.energidataservice.dk/) API to provide a straightforward interface for querying energy data. This tool runs locally on your PC and does not require any authentication.
The [executable file](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/build/exe.win-amd64-3.12/Data%20Query%20Tool%20-%20Electricity%20Spot%20Price.exe) was built with cx_Freeze library through [setup file](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/setup.py).

### Key Features
- **Interactive GUI:** Allows users to select parameters via a simple graphical interface.
- **Custom Queries:** Generate queries based on user-defined parameters and save the results as a `.csv` file in the same directory as the [executable file](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/build/exe.win-amd64-3.12/Data%20Query%20Tool%20-%20Electricity%20Spot%20Price.exe).
- **User Input:** Specify date ranges, areas, and aggregation types.
- **Data Retrieval:** Fetch data from EnergiDataService based on the selected parameters.
- **CSV Export:** Save the resulting data as a CSV file for further analysis.


### Components
- **[GUI File](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/gui.py):** Handles the graphical user interface and parameter selection.
- **[Data Fetching Code](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/gui_feed.py):** Manages data retrieval from the EnergiDataService API.


## Requirements

- Python 3.12

## Installation & Usage

1. **Clone the repository** to your local directory:
   ```bash
   git clone https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price.git

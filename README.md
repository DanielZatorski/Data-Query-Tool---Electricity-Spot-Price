# Data Query Tool for EnergiDataService

## Overview

The Data Query Tool is a Python-based application that leverages the [EnergiDataService](https://www.energidataservice.dk/) API to provide a straightforward interface for querying energy data with dynamic visualisation. This tool runs locally on your PC via Streamlit framework and does not require any authentication.

### Key Features
- **Interactive GUI:** Allows users to select parameters via a simple graphical interface.
- **Custom Queries:** Generate queries based on user-defined parameters where you can save the results as a `.csv` file.
- **User Input:** Specify date ranges, areas, and aggregation types.
- **Data Retrieval:** Fetch data from EnergiDataService based on the selected parameters.
- **Visualisations:** Based on generated queries, analyze the data.
- **CSV Export:** Save the resulting data as a CSV file for further analysis.


### Components
- **[GUI File](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/streamlit_gui.py):** Handles the graphical user interface and parameter selection using Streamlite framework.
- **[Data Fetching Code](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/gui_feed.py):** Manages data retrieval from the EnergiDataService API.


## Requirements

- Python 3.12

## Installation & Usage

1. **Clone the repository** to your local directory:
   ```bash
   git clone https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price.git

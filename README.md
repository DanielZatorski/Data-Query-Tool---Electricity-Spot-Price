# Data Query Tool for EnergiDataService

## Overview

The Data Query Tool is a Python-based application that leverages the [EnergiDataService](https://www.energidataservice.dk/) API to provide a straightforward interface for querying energy data with dynamic visualisation. This tool runs locally on your PC via Streamlit framework and does not require any authentication.

### Key Features
- **Interactive GUI:** Allows users to select parameters via a simple graphical interface.
- **Custom Queries:** Generate queries based on user-defined parameters
- **User Input:** Specify date ranges, areas, and aggregation types.
- **Data Retrieval:** Fetch data from EnergiDataService based on the selected parameters.
- **Visualisations:** Based on generated queries, analyze the data.
- **CSV Export:** Save the resulting data as a CSV file for further analysis


### Components
- **[GUI File](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/streamlit_gui.py):** Handles the graphical user interface and parameter selection using Streamlite framework.
- **[Data Fetching Code](https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price/blob/main/gui_feed.py):** Manages data retrieval from the EnergiDataService API.

## Presentation

![image](https://github.com/user-attachments/assets/1db7181c-2bf1-4222-8b4f-b0061f41c841)
![image](https://github.com/user-attachments/assets/bdbed0f9-c12f-49f5-8f1d-de59011b4645)
![image](https://github.com/user-attachments/assets/596ac5e1-bbe9-4fd7-9f52-ce8cb5d6a2bc)


## Requirements

- Python 3.12

## Installation & Usage

1. **Clone the repository** to your local directory:
   ```bash
   git clone https://github.com/DanielZatorski/Data-Query-Tool---Electricity-Spot-Price.git

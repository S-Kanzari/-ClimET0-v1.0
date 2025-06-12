
NASA POWER Climate Data Downloader with ET₀ Calculation
-------------------------------------------------------

Description:
------------
This Python script downloads daily climate data (minimum temperature, maximum temperature, and precipitation) for a list of locations from NASA's POWER API. It then calculates daily reference evapotranspiration (ET₀) using the Samani equation.

Requirements:
-------------
- Python 3.x
- Required Python packages:
  - requests
  - pandas
  - openpyxl (for writing Excel files)

Install dependencies with:
pip install requests pandas openpyxl

Input:
------
- Excel file named 'Palces_Coordiantes.xlsx' located in the same directory.
- The Excel file must have the following columns:
    - Place: Name of the location
    - Latitude: Decimal degrees
    - Longitude: Decimal degrees
- Choose Start Date and End Date

Example of Excel content:
| Place    | Latitude | Longitude |
|----------|----------|-----------|
| 1        | 36.8065  | 10.1815   |
| 2        | 34.7406  | 10.7603   |

Output:
-------
- For each location, a separate Excel file is created named '<Place>_climate_et0.xlsx'.
- Each file includes:
    - Date
    - T2M_MIN (°C): Daily minimum temperature
    - T2M_MAX (°C): Daily maximum temperature
    - Precipitation (mm): Corrected daily precipitation
    - ET0 (mm/day): Reference evapotranspiration (Samani method)

Notes:
------
- Make sure your internet connection is active when running the script.
- Dates are set manually in the script. You can change the `start_date` and `end_date` variables as needed.

Author:
-------


[![DOI](https://zenodo.org/badge/1001089213.svg)](https://doi.org/10.5281/zenodo.15652931)

Date: June 2025

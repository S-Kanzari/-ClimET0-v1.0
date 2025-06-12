import requests
import pandas as pd

# === Read stations from Excel file ===
stations_df = pd.read_excel('Palces_Coordiantes.xlsx')  # Make sure the file is in the same folder

start_date = '2025-01-28'
end_date = '2025-04-28'

for _, row in stations_df.iterrows():
    name = row['Place']
    lat = row['Latitude']
    lon = row['Longitude']

    # === NASA POWER API URL ===
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?start={start_date.replace('-', '')}&end={end_date.replace('-', '')}"
        f"&latitude={lat}&longitude={lon}"
        f"&parameters=T2M_MIN,T2M_MAX,PRECTOT"
        f"&community=AG&format=JSON"
    )

    response = requests.get(url)
    data = response.json()
    records = data['properties']['parameter']
    dates = list(records['T2M_MIN'].keys())

    # === Create DataFrame ===
    df = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'T2M_MIN (°C)': [records['T2M_MIN'][d] for d in dates],
        'T2M_MAX (°C)': [records['T2M_MAX'][d] for d in dates],
        'Precipitation (mm)': [records['PRECTOTCORR'][d] for d in dates]
    })

    # === Compute ET₀ using Samani equation ===
    tmin = df['T2M_MIN (°C)']
    tmax = df['T2M_MAX (°C)']
    tmean = (tmin + tmax) / 2
    df['ET0 (mm/day)'] = 0.0135 * (tmean + 17.78) * ((tmax - tmin) ** 0.5)

    # === Save to separate Excel file ===
    output_file = f"{name}_climate_et0.xlsx"
    df.to_excel(output_file, index=False)
    print(f"✅ {name}: Data saved to '{output_file}'")

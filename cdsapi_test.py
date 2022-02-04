import cdsapi
import zipfile
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

c = cdsapi.Client()

################################################## TEMPERATURE #############################################
print("Retrieving temperature data")

years = np.arange(2022, 2057, step=5)
years = years.tolist()

# c.retrieve(
#     'sis-marine-properties',
#     {
#         'origin': 'polcoms_ersem',
#         'vertical_resolution': 'water_column',
#         'time_aggregation': 'day',
#         'variable': 'sea_water_potential_temperature',
#         'experiment': [
#             'rcp4_5', 'rcp8_5',
#         ],
#         'year': years,
#         'month': [
#             '03'
#         ],
#         'format': 'zip',
#     },
#     '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_03.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '04'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_04.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '05'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_05.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '06'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_06.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '07'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_07.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '08'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_08.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '09'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_09.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '10'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_10.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '01'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_04.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '02'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_04.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '11'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_04.zip')


c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'sea_water_potential_temperature',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': years,
        'month': [
            '12'
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/temp_04.zip')

################################################## OXYGEN #############################################
print("Retrieving dissolved oxygen data")

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'mole_concentration_of_dissolved_oxygen',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '01', '02', '03',
            '04',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/oxy_01_04.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'mole_concentration_of_dissolved_oxygen',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '05', '06', '07',
            '08',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/oxy_05_08.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'mole_concentration_of_dissolved_oxygen',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '09', '10', '11',
            '12',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/oxy_09_12.zip')


################################################## CHLOROPHYLL-A #############################################
print("Retrieving total chlorophyll-a data")

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'total_chlorophyll_a',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '01', '02', '03',
            '04',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/chla_01_04.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'total_chlorophyll_a',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '05', '06', '07',
            '08',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/chla_05_08.zip')

c.retrieve(
    'sis-marine-properties',
    {
        'origin': 'polcoms_ersem',
        'vertical_resolution': 'water_column',
        'time_aggregation': 'day',
        'variable': 'total_chlorophyll_a',
        'experiment': [
            'rcp4_5', 'rcp8_5',
        ],
        'year': [
            '2006', '2007', '2008',
            '2009', '2010', '2011',
            '2012', '2013', '2014',
            '2015', '2016', '2017',
            '2018', '2019', '2020',
            '2021', '2022', '2023',
            '2024', '2025', '2026',
            '2027', '2028', '2029',
            '2030', '2031', '2032',
            '2033', '2034', '2035',
            '2036', '2037', '2038',
            '2039', '2040', '2041',
            '2042', '2043', '2044',
            '2045', '2046', '2047',
            '2048', '2049', '2050',
            '2051', '2052', '2053',
            '2054', '2055', '2056',
            '2057', '2058', '2059',
            '2060', '2061', '2062',
            '2063', '2064', '2065',
            '2066', '2067', '2068',
            '2069', '2070', '2071',
            '2072', '2073', '2074',
            '2075', '2076', '2077',
            '2078', '2079', '2080',
            '2081', '2082', '2083',
            '2084', '2085', '2086',
            '2087', '2088', '2089',
            '2090', '2091', '2092',
            '2093', '2094', '2095',
            '2096', '2097', '2098',
            '2099',
        ],
        'month': [
            '09', '10', '11',
            '12',
        ],
        'format': 'zip',
    },
    '/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/chla_09_12.zip')




#data_load = zipfile.ZipFile("tmp.zip", mode="r")
#files = zipfile.ZipFile.namelist(data_load)
##data_nc = data_load.open(files[0])
#with zipfile.ZipFile('tmp.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
#   zipObj.extractall()

#ds = nc.Dataset(files[0])
#plt.imshow(ds["thetao"][0, 0, :, :], origin="lower")


#data_se = cdsapi.geo.extract_point(data, lon=43.847366, lat=14.323250)
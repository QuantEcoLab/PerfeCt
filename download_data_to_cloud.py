import requests

links = [
    "https://download-0000.copernicus-climate.eu/cache-compute-0000/cache/data9/dataset-sis-marine-properties-254ce9de-4eca-4efd-a3fa-0167e4d148fc.zip",
    "https://download-0004.copernicus-climate.eu/cache-compute-0004/cache/data6/dataset-sis-marine-properties-1dcba46c-6dae-4b7f-a45e-5a1ffa426705.zip",
    "https://download-0015.copernicus-climate.eu/cache-compute-0015/cache/data6/dataset-sis-marine-properties-4cb7be83-2bba-4a05-b2b1-eeb800c62f09.zip",
    "https://download-0006.copernicus-climate.eu/cache-compute-0006/cache/data3/dataset-sis-marine-properties-953d770d-6ee6-4b6c-9662-b126c4560a5b.zip",
    "https://download-0012.copernicus-climate.eu/cache-compute-0012/cache/data3/dataset-sis-marine-properties-a8e9fbf1-36a8-4260-8c3f-89dbf815dfe9.zip",
    "https://download-0002.copernicus-climate.eu/cache-compute-0002/cache/data4/dataset-sis-marine-properties-03091dbd-d140-4b2b-be3a-ef25a4cf892f.zip",
    "https://download-0004.copernicus-climate.eu/cache-compute-0004/cache/data0/dataset-sis-marine-properties-65fa1e41-1c9e-44a5-b91a-3278fbcd26d1.zip",
    "https://download-0000.copernicus-climate.eu/cache-compute-0000/cache/data7/dataset-sis-marine-properties-87193ecd-aa9e-4c5d-b6ee-7b3b976ec500.zip",
    "https://download-0015.copernicus-climate.eu/cache-compute-0015/cache/data6/dataset-sis-marine-properties-6a3c2966-9f68-4bb7-89e5-5039009a5708.zip"
]

names = [
    "sis-marine-properties_01.zip",
    "sis-marine-properties_02.zip",
    "sis-marine-properties_04.zip",
    "sis-marine-properties_05.zip",
    "sis-marine-properties_06.zip",
    "sis-marine-properties_07.zip",
    "sis-marine-properties_09.zip",
    "sis-marine-properties_10.zip",
    "sis-marine-properties_12.zip",
]

cloud_path = "/run/user/1000/gvfs/ftp:host=cadaptcloud.local/CADAPT/DATA/BlueCloudHackathon_DATA/"

for i in range(len(links)):
    print(f"Downloading {names[i]}")
    url = links[i]
    print("Sending request...")
    r = requests.get(url, allow_redirects=True)
    print("Downloading data...")
    open(cloud_path+names[i], 'wb').write(r.content)
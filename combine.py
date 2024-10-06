import pandas as pd

# Load the datasets for multiple yearsmonarch_2021 = pd.read_csv('monarch_sightings2021.csv')
monarch_2010 = pd.read_csv('csv-files-data/2010/daily_temp_data2010.csv')
monarch_2011 = pd.read_csv('csv-files-data/2011/daily_temp_data2011.csv')
monarch_2012 = pd.read_csv('csv-files-data/2012/daily_temp_data2012.csv')
monarch_2013 = pd.read_csv('csv-files-data/2013/daily_temp_data2013.csv')
monarch_2014 = pd.read_csv('csv-files-data/2014/daily_temp_data2014.csv')
monarch_2015 = pd.read_csv('csv-files-data/2015/daily_temp_data2015.csv')
monarch_2016 = pd.read_csv('csv-files-data/2016/daily_temp_data2016.csv')
monarch_2017 = pd.read_csv('csv-files-data/2017/daily_temp_data2017.csv')
monarch_2018 = pd.read_csv('csv-files-data/2018/daily_temp_data2018.csv')
monarch_2019 = pd.read_csv('csv-files-data/2019/daily_temp_data2019.csv')
monarch_2020 = pd.read_csv('csv-files-data/2020/daily_temp_data2020.csv')
monarch_2021 = pd.read_csv('csv-files-data/2021/daily_temp_data2021.csv')
monarch_2022 = pd.read_csv('csv-files-data/2022/daily_temp_data2022.csv')
monarch_2023 = pd.read_csv('csv-files-data/2023/daily_temp_data2023.csv')

# Concatenate all years together
combined_data = pd.concat([monarch_2010, monarch_2011, monarch_2012, monarch_2013, monarch_2014, monarch_2015, monarch_2016, monarch_2017, monarch_2018, monarch_2019, monarch_2020, monarch_2021, monarch_2022, monarch_2023], ignore_index=True)

# Save combined data
combined_data.to_csv('combined_monarch_sightings.csv', index=False)

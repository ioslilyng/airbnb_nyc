# Airbnb NYC and CRISP-DM
The project applies CRISP-DM process on Airbnb New York City listings dataset to gain insight into Airbnb hosting business.
***
### Prerequisites

Basic packages are required to run notebooks as the followings:
  * [pandas](https://github.com/pandas-dev/pandas)
  * [numpy](https://github.com/numpy/numpy)
  * [matplotlib](https://github.com/matplotlib/matplotlib)
  * [seaborn](https://github.com/mwaskom/seaborn)
  
Packages for spatial analysis:
  * [geopandas](https://github.com/geopandas/geopandas)
  * [Fiona](https://github.com/Toblerity/Fiona)
  * [GDAL](https://github.com/OSGeo/gdal)
 ***
### Project Structure

1. Code
  - `NYC_data_collection` - Data preparation to find good features to work on our model.
  - `NYC_prep` - Data analysis and visualization.
  - `NYC_Final` - Basic Linear Regression model is applied.
2. Spatial Analysis
  - `nyc_map.html` - The interactive map which shows listings of super hosts around the city.
3. Data
  - Data folder includes raw dataset `listings` which can be found on [Inside Airbnb](http://insideairbnb.com/)
  - `sample.csv` is used for our Linear Regression model.
  
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

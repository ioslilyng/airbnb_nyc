# Data Analysis on Airbnb New York City
The project applies CRISP-DM process on Airbnb New York City listings dataset to gain insight into Airbnb hosting business.
A post for this project is on [Medium](https://medium.com/@lilyng15/data-analysis-on-airbnb-new-york-city-60bb85560a01).
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
  - `NYC_Analysis` - Data preparation and analysis.
  - `NYC_Prep` - Data analysis and visualization.
  - `NYC_Final` - Machine learning models are applied along with their evaluation metrics.
  
2. Spatial Analysis
  - `index.html` - The interactive map which shows listings of super hosts around the city.
  
3. Data
  - Data folder includes raw dataset `listings.csv` which can be found on [Inside Airbnb](http://insideairbnb.com/)
  - `prep_final.csv` and `final_sample` are obtained during data preparation and analysis step.
  
  
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

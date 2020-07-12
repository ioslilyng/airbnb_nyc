# Data Analysis on Airbnb New York City
The project applies CRISP-DM process on Airbnb New York City listings dataset to gain insight into Airbnb hosting business.
A post for this project is on [Medium](https://medium.com/@lilyng15/data-analysis-on-airbnb-new-york-city-60bb85560a01).

***

### Libraries use

  * [pandas](https://github.com/pandas-dev/pandas)
  * [numpy](https://github.com/numpy/numpy)
  * [matplotlib](https://github.com/matplotlib/matplotlib)
  * [seaborn](https://github.com/mwaskom/seaborn)
  * [sklearn](https://github.com/scikit-learn/scikit-learn)

  * [geopandas](https://github.com/geopandas/geopandas)
  * [Fiona](https://github.com/Toblerity/Fiona)
  * [GDAL](https://github.com/OSGeo/gdal)
***
### Project Motivation

Airbnb has become a travel trend in recent years. Their economic model benefits not only the company itself, but also hosts, and travelers as well. Whether you are a host or a traveler, understanding what factors contribute to your business when working with Airbnb is a smart move.  The project analyzes Airbnb data on purposes to figure out those factors. 

***

### Files include:

1. Code
  - `NYC_Analysis.ipynb` - Data preparation and analysis.
  - `NYC_Prep.ipynb` - Data analysis and visualization.
  - `NYC_Final.ipynb` - Machine learning models are applied along with their evaluation metrics.

2. Interactive map
  - index.html` - The interactive map which shows listings of super hosts around the city.

3. Data folder
  -  `listings.csv` - Raw dataset used in `NYC_Analysis.ipynb` 
  - `prep_final.csv` - Processed dataset used in `NYC_Prep.ipynb`
  - `neighbourhoods.geojson` - Geographic dataset used to crate interactive map in `NYC_Prep.ipynb`
  - `final_sample.csv` - Processed dataset used in `NYC_Final.ipynb` 

4. README.md 

   The project write-up.

***

### CRISP-DM process 

CRISP-DM process is applied throughout the project by following 6 basic steps as below:

1. Business understanding
2. Data understanding
3. Data preparation
4. Modeling
5. Evaluation
6. Deployment

Four questions are asked during CRISP-DM process, which aims to predict the price as final goal:

1. Do neighborhood and neighborhood groups affect the price?

2. How do amenities affect the price?

3. Where are super hosts located?

4. What type of room is reserved the most?

***

### Summary

- Neighborhood and neighborhood groups play a crucial role in the price.
- Some amenities are more important than others, such as bed linen, TV, coffee machine, cooking basics, etc. As a host, providing amenities that are in demand helps improve ratings. As a result, monthly earnings also enhanced.
- Super hosts centralize within three major boroughs, which include Manhattan, Brooklyn, and Queens.
- The entire home/ apartment and private room are booked the most in NYC.
- Finally, XGBoost stands out as the final result in terms of price prediction.

***

### Acknowledgements

- Stackoverflow
- Kaggle

***

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

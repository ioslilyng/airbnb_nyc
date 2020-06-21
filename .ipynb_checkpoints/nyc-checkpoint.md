***

## Data Description

*`listings` 

- 49530 listings in total 

 - Features: 
   3. host_is_superhost
   2. neighbourhood
   3. neighbourhood_group_cleansed
   4. property_type
   5. room_type
   6. accommodates
   7. bathrooms
   8. bedrooms
   9. beds
   10. price - object -> change to int
   11. security_deposit
   12. cleaning_fee
   13. guests_included
   14. minimum_nights
   15. availability_30
   16. availability_365
   17. number_of_reviews
   18. review_scores_rating - float
   19. review_scores_accuracy
   20. review_scores_cleanliness
   21. review_scores_checkin
   22. review_scores_communication
   23. review_scores_location
   24. review_scores_value
- 

***

## Data Collection

Data Collection:

- 19 numeric features and 5 categorical features are chosen 

- `security_deposit` has the most missing values (35.7%). While all `review` features are next with around 24.9%. `cleaning_fee` comes next with 21.9%
- Based on data distribution of each feature, I fill missing values with appropriate methods which include mean and median.
- For categorical features, dummy function is used to create dataframe 
- Then select useful features which are then applied for our model 
- 13 main features out of list of 20 best features for price prediction are as followings:
  - property_type
  - accommodates
  - bedrooms
  - bathrooms
  - beds
  - neighbourhood
  - cleaning_fee
  - neighbourhood_group_cleansed
  - room_type
  - guests_included
  - security_deposit
  - availability_365
  - number_of_reviews

Data preparation: 

- 18 numeric columns/ 26
- 8 categorical cols/26
- fillna for review_scores with median()
- Imputing zero values on `price`, `availability_30`, `availability_365`, 'number_of_reviews'

- `price` contains symbol $
- average price $163, using describe() function 
- drop missing values on `host_is_superhost` and `neighbourhood` since both columns contain small number of missing values 
- `price` and `number_of_reviews` also have missing values
- missing values on review scores 
- after cleaning missing values, dataset contains 49487 listings in total as compared to 49530 listings of the original dataset

***

Spatial Analysis

- price distribution across neighbourhoods




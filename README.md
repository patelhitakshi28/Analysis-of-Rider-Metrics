# Analysis-of-Rider-Metrics
Analysis of Rider Metrics: Duration, Distance, and Calories Burned

# If you find this repo useful, give it a STAR 
Approach for the provided task : 

# Steps to be followed :

1.	Loading and processing the CSV data : I have first, loaded the data into the pandas data frame for easier manipulation and analysis. I then calculated the required statistics for each rider including the number of trips, total distance, loggers used, average speed (in km/h), and calories burned per km.
2.	Generation JSON File: I, then grouped the data by rider_name to get the necessary data for each rider, and then saved the results as Json file.  
3.	Creating Visualization : For Visualizing the data I have used Microsoft Power Bi, and created graphs, and slicers to it for better understanding and further analysis. 
  a.	Individual statistics for each driver: duration, distance, and calories.
  b.	Comparative statistics for males and females: total duration, distance, and calories.
4. Handling Gender Data : As the provided original CSV data did not include gender information, I have assumed gender based on common names. If the data would be real time and complex then I would have considered to get a better csv data, which would already be having gender information.

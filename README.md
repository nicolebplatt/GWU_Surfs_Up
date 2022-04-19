# Surfs Up

## Overview

The purpose of this analysis is to examine and compare temperatures on Oahu during the months of June and December to establish whether a combination surf and ice cream shop is sustainable year-round.

## Results

Upon review of temperature data in Oahu during the months of June and December (summary statistics captured below), three major points arose:

**June**

![June_temps_desc](https://user-images.githubusercontent.com/99286327/164056753-5ff4a87b-e3fe-450e-802a-9a0e97c09c31.png)

**December**

![Dec_temps_desc](https://user-images.githubusercontent.com/99286327/164056830-7ccbdd0e-3d01-4a94-a3a3-e3d54187bbca.png)

1. There are approximately 200 fewer temperature readings in December as there are in June.

2. The average temperature in December is only ~4° colder than in June (71.04° compared to 74.94°, respectively). In fact, the first, second, and third quartiles show only a ~4° difference in temperature between the two months.

3. While the max temp in June was 85° and the max temp in December was 83° (a difference of only 2°), the difference between the two minimum temperatures (56° in December and 64° in June) is the largest difference across the summary statistics at 8°.


## Summary

Overall, it appears that the weather in Oahu will not hinder the sales of a combination surf and ice cream shop. Temperatures remain mostly steady and above 70° for the majority of the year.

Two additional queries I would perform to gather more weather data for June and December would be:

1. The same summary analysis conducted as above but compiled for each year of data in the dataset. This would allow us to see if there are nuances in trends over the last several years (i.e. temps getting warmer). Currently, the dataset spans Jan 1, 2010 to Aug 23, 2017 and it would be good to know if the temperature trends we saw above have remained steady across the years or if climate change is having an impact and we are seeing changes in temperature readings by year.

![Screen Shot 2022-04-19 at 12 30 01 PM](https://user-images.githubusercontent.com/99286327/164056864-baf74e10-b8d5-4ecd-a885-84418a37215c.png)

2. A quick analysis on temperatures by station. We can see in the raw data that the range of elevation is quite dramatic among the different stations and this difference might be skewing the results when aggregated. For example, one station has an elevation of 0.9 and another has an elevation of 306.6. As such, one station might have warmer or colder temps than the others and it would be good to factor this in when determining a location for the shop.

![Screen Shot 2022-04-19 at 1 14 02 PM](https://user-images.githubusercontent.com/99286327/164059151-64aa3413-388a-422d-8ef2-fc3b4a8d44d5.png)

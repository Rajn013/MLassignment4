#!/usr/bin/env python
# coding: utf-8

# 1. What are the key tasks involved in getting ready to work with machine learning modeling?
# 

# To work with machine learning modeling, key tasks include: defining the problem, gathering and preprocessing data, selecting and engineering features, splitting the data, choosing the right algorithm, training and evaluating models, validating and testing models, deploying and monitoring models, documenting and communicating the process, and iterating and improving models over time.

# 2. What are the different forms of data used in machine learning? Give a specific example for each of them.
# 

# The different forms of data used in machine learning include numerical data (e.g., housing prices), categorical data (e.g., customer satisfaction levels), text data (e.g., customer reviews), image data (e.g., handwritten digits), time series data (e.g., stock prices), audio data (e.g., spoken commands), and video data (e.g., surveillance footage).
# 

# 1. Numeric vs. categorical attributes
# 2. Feature selection vs. dimensionality reduction
# 

# Numeric attributes are quantitative and can take on a range of values, while categorical attributes represent qualitative variables that fall into specific categories.
# 
# Feature selection involves selecting a subset of relevant features based on their importance or predictive power, aiming to reduce model complexity and improve performance.
# 
# Dimensionality reduction transforms the original high-dimensional feature space into a lower-dimensional representation while preserving important information, helping to reduce computational complexity and remove noise or redundancy.

# 1. The histogram
# 
# 2. Use a scatter plot
# 

# A histogram is a graphical representation that organizes data into bins or intervals and displays the frequency or count of observations within each bin. It provides a visual representation of the distribution of a dataset and helps identify patterns, outliers, and the overall shape of the data.
# 
# Determine the range and number of bins you want to use. Bins divide the range of data into intervals.
# Count the number of observations falling into each bin.
# Create a bar chart where each bin is represented by a bar, and the height of each bar corresponds to the count of observations in that bin.
# Label the x-axis with the bins and the y-axis with the frequency or count.
# 
# 
# A scatter plot is a graphical representation that displays the relationship between two numeric variables. It shows the individual data points as dots on a two-dimensional plane, with one variable represented on the x-axis and the other on the y-axis. Scatter plots are useful for visualizing the correlation, trend, or clustering of data points.
# Identify the two numeric variables you want to plot on the x-axis and y-axis.
# For each data point, plot a dot at the corresponding x and y values.
# Label the x-axis with the variable represented on the x-axis and the y-axis with the variable represented on the y-axis.
# 
# 

#  Why is it necessary to investigate data? Is there a discrepancy in how qualitative and quantitative data are explored?
# 

# Investigating data is necessary to gain a comprehensive understanding and make informed decisions. While the overall goal is the same for both qualitative and quantitative data—to uncover patterns and insights—there are differences in approaches:
# 
# Qualitative data exploration: Analyze non-numerical data using techniques like content analysis or thematic analysis. Interpretation and contextual understanding are crucial. Techniques like coding, clustering, or visualization aid exploration.
# 
# Quantitative data exploration: Analyze numerical data using statistical techniques and visualization tools. Examine descriptive statistics, distributions, correlations, and conduct hypothesis testing. Techniques like histograms, scatter plots, and summary statistics are used.
# 
# Data exploration is essential for both qualitative and quantitative data, but the methods differ due to data nature. Qualitative exploration involves subjective interpretation, while quantitative exploration relies on statistical analysis and numerical patterns.

# 6. What are the various histogram shapes? What exactly are ‘bins'?
# 

# A histogram is a graphical representation that organizes data into bins or intervals and displays the frequency or count of observations within each bin. It provides a visual representation of the distribution of a dataset and helps identify patterns, outliers, and the overall shape of the data.
# 
# Determine the range and number of bins you want to use. Bins divide the range of data into intervals. Count the number of observations falling into each bin. Create a bar chart where each bin is represented by a bar, and the height of each bar corresponds to the count of observations in that bin. Label the x-axis with the bins and the y-axis with the frequency or count.
# 
# 
# In data analysis and visualization, "bins" refer to the intervals or groups into which the range of data values is divided. Binning is a technique used to discretize or categorize continuous or numeric data into discrete intervals.

# 7. How do we deal with data outliers?
# 

# Identify outliers using visual inspection or statistical methods.
# Understand the cause of outliers.
# Remove outliers if they are erroneous or not representative (with caution).
# Transform the data using mathematical transformations to reduce the impact of outliers.
# Apply winsorization or capping by replacing extreme values with a predetermined threshold.
# Use robust statistical measures that are less sensitive to outliers.
# Utilize model-based approaches that are specifically designed to handle outliers within certain modeling techniques.

# 8. What are the various central inclination measures? Why does mean vary too much from median in certain data sets?
# 

# Mean: The mean is calculated by summing all the values in the dataset and dividing by the number of data points. It represents the arithmetic average of the data. The mean is sensitive to extreme values (outliers) and can be influenced by skewed distributions.
# 
# Median: The median is the middle value in an ordered dataset. It is not affected by extreme values and is a robust measure of central tendency. It is useful when the data has skewed distributions or contains outliers.
# 
# Mode: The mode is the value that appears most frequently in a dataset. It is particularly useful for categorical or discrete data. Unlike the mean and median, the mode is not a measure of central location for continuous numerical data.
#     
# 
#  the mean varies significantly from the median in certain datasets due to the influence of outliers or skewed distributions. The median provides a more robust measure of central tendency in such cases.
#     

# 10. Describe how cross-tabs can be used to figure out how two variables are related.
# 

# Set up a table: Create a table with one variable as rows and the other variable as columns.
# 
# Populate the table: Count the number of observations that fall into each combination of categories and fill in the corresponding cells.
# 
# Analyze the table: Look for patterns, differences, or associations between the categories. Pay attention to cells with high or low counts.
# 
# Interpret the results: Based on the table, observe how the variables are related. Determine if there is a strong association or dependency between the variables.
# 
# Consider statistical tests: Use statistical tests, such as the chi-square test, to assess the significance of the relationship between the variables.

# In[ ]:





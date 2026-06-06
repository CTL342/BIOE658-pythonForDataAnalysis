# Import the matplotlib.pyplot module with the alias plt
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Define your data
# You have been given the following sample monthly data for one year.
months = np.arange(1, 13)  # 1 to 12
avg_temperatures = [30, 31, 29, 25, 22, 20, 19, 20, 22, 24, 27, 29]  # Example temperatures
rainfall = [80, 70, 90, 150, 210, 220, 200, 190, 170, 100, 90, 80]  # Rainfall in mm
humidity = [65, 70, 75, 78, 80, 85, 87, 85, 80, 77, 70, 65]  # Humidity in percentage

#%% Step 2: Create subplots
# Create a figure and a 2x2 grid of subplots. Use plt.subplots() function.
fig, axs = plt.subplots(2, 2, figsize=(10,8))

#%% Step 3: Line Plot
# On the first subplot, create a line plot showing the average temperatures across the months.
# Remember to add markers, a title, axis labels, and grid lines for better readability.
axs[0, 0].plot(months, avg_temperatures, color='red', marker='o')
axs[0, 0].set_title('Average Temperatures')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Temperature (C)')
axs[0, 0].set_xticks(np.arange(2, 13, 2))
axs[0, 0].grid(True)

#%% Step 4: Bar Chart
# On the second subplot, create a bar chart to display the rainfall per month.
# Customize the bar color, and add a title, axis labels, and grid lines.
axs[0, 1].bar(months, rainfall, color='blue')
axs[0, 1].set_title('Monthly Rainfall')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Rainfall (mm)')
axs[0, 1].set_xticks(np.arange(2, 13, 2))
axs[0, 1].grid(True)

#%% Step 5: Scatter Plot
# On the third subplot, create a scatter plot to explore the relationship between average temperatures and humidity.
# Customize marker color, add a title, and label the axes.
axs[1, 0].scatter(avg_temperatures, humidity, color='green', marker='o')
axs[1, 0].set_title('Humidity vs. Average Temperature')
axs[1, 0].set_xlabel('Average Temperature (C)')
axs[1, 0].set_ylabel('Humidity (%)')

#%% Step 6: Histogram
# On the fourth subplot, create a histogram to show the distribution of average temperatures over the year.
# Choose an appropriate number of bins, set a color, and add a title and axis labels.
axs[1, 1].hist(avg_temperatures, bins=5, color='purple', edgecolor='black')
axs[1, 1].set_title("Temperature Distribution")
axs[1, 1].set_xlabel('Average Temperature (C)')
axs[1, 1].set_ylabel('Frequency')

#%% Step 7: Customization
# Ensure each plot has appropriate titles and axis labels. Feel free to customize the plots with different colors or markers.


#%% Step 8: Adjust Layout
# Adjust the layout to make sure there is no overlapping content. Use plt.tight_layout() or figure adjustments.
fig.suptitle('Weather Patterns Over a Year', fontsize=20)

#%% Step 9: Display the Plot
# Use plt.show() to display your figure containing all the subplots.
plt.show()
# Bonus: Explore additional functionalities of Matplotlib if time permits. For example, try adding annotations to highlight specific data points or use the plt.savefig() function to save your figure as a .png file.
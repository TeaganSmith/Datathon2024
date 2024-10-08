How we built it:
What we did is pull data from the different monarch butterfly and AQI sites given to us, and we extracted data like daily AQI, temperature, monarch butterfly count and more, then compared these values with one another. We then generated a custom LLM model via OpenAI that can process and recreate CSV files with relevant season, county, AQI, temperature, and FIPS columns given only a date, state, and city. We first visualized the monarch count, creating a script to normalize our data, then generate a heat map of the U.S. to visualize the dispersion of Monarch sightings by county over the last 15 years using Python libraries like matplotlib and geopandas. Next we mapped this information across relevant data such as Milkweed growth rates, temperature, and AQI by county to scan for similarities in migration patterns. We then started a deeper statistical analysis of relevant variables, beginning with a linear regression model, before pivoting to a negative binomial regression model due to our Y value being a count variable, and our data-set being heavily over-dispersed. This allowed us to adequately find a correlation between season, year, air quality, and temperature across 15 years to map and explain the decline of monarch butterflies, as well as generate a potential solution.

Challenges we ran into:
Our original AI analysis was consistently finding no correlation, contrary to our pre-processing research. After analyzing our model choice, we realized we weren't using the best approach, and had to pivot last-minute. Our data pre-processing initiative was very long due to maintaining a grueling verification process of our data transformations, however this allowed us to verify datasets as we worked, rather than encountering errors and having to fix them later in our process.

Accomplishments that we're proud of:
Created CSVs through batch processing so we could test things at a small level, and scale it up to find multiple correlation factors. Created several CSVs using Python, allowing us to visualize our data and more. Utilizing multiple AI models and visualization tactics.






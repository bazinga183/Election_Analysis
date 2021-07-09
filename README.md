# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who received votes.
3. Calculate the total number of votes each cadidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: [election_results.csv](https://github.com/bazinga183/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.9.6, Visual Studio Code, 1.57.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGetter
  - Raymon Anthony Doane
- The candidate results were:
  -Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  -Diane DeGette received 73.8% of the vote and 272,893 number of votes.
  -Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,893 number of votes.

![election_analysis](https://user-images.githubusercontent.com/46951897/125124810-4b7fb200-e0be-11eb-89a0-d96843120c77.PNG)

 
## Challenge Overview
The Colorado Board of Election employee gave further tasks:

1. Calculate the voter turnout by county.
2. Calculate the percentage of votes from each county of the total count.
3. Calculate the county with the highest turnout.

## Challenge Summary
For the challenge, additional lists and dictionaries were added so that it would also incorporate the counties to be printed in the [election_results.txt](https://github.com/bazinga183/Election_Analysis/blob/main/analysis/election_results.txt) file.

```
# 1: Create a county list and county votes dictionary.
county_list = []
county_voter_turnout = {}
```

The analysis on the selected counties show that:
- There were 369,711 votes cast in the election.
- The counties that took part in the election were:
    - Jefferson
    - Denver
    - Arapahoe
- The results for the election were:
    - Jefferson County casted 38,855 votes, which made up 10.5% of the vote.
    - Denver County casted 306,055 votes, which made up 82.8% of the vote.
    - Arapahoe County casted 24,801 votes, which made up 6.7% of the vote.
The county that had the highest voter turnout was:
  - Denver County who cast 306,055 votes and made up 82.8% of the vote.

This results was obtained by iterating through each county in the data to see which had the highest voter turnout and the highest percentage of the vote.

```
# 6a: Write a for loop to get the county from the county dictionary.
    for voting_county in county_voter_turnout:

        # 6b: Retrieve the county vote count.
        vote_count = county_voter_turnout.get(voting_county)

# 6f: Write an if statement to determine the winning county and get its vote count.
        if (vote_count > largest_count):
            largest_count = vote_count
            largest_county_turnout = voting_county
```

![election_results](https://user-images.githubusercontent.com/46951897/125124899-723de880-e0be-11eb-93ce-09ee0d2b5844.PNG)

## Future Uses of This Code
This script could potentially be used for future elections, but some nuances can be added if needed.
- For instance, demographics can be added into the csv file so that each voter has more information that the committee can use for future elections. This would also give more information to future candidates and incumbents for which demographics they could target in the future.
- Another way to modify the script is to add the percentage of votes in a county that went towards a certain candidate. This would provide more information to the committee for their own database and for candidates/incumbents on which counties they can target during their runnin for office.

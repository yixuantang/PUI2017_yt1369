Hi Yixuan, 

I have reviewed your HW3 CitiBike project proposal assignment.

**a. verify that your Null and alternative hypotheses are formulated correctly

Your idea is:
The post-90s are more likely than pre-90s to choose biking for commuting
And your NULL HYPOTHESIS is :
The ratio of post-90s biking on weekends over post-90s biking on weekdays is the same or lower than the ratio of pre-90s biking over weekends to pre-90s biking on weekdays

The hypothesis was formulated correctly and clearly. To imporve your Hypothesis and make it more pursuasive, properbaly it is better to dig more into weekdays' rush hours and analyze the usage by post-90s and pre-90s. 

**b. verify that your data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

I saw you did good job to pick the only necessary but enough dataset columns for your analysis, "brith year" and "date", the former contains user's age information(post or pre-90s) and the later contains usage time stamp information. One suggestions here,  do a drop of the lines without data(in this case there are lines without user birth year) is better since we are not always know how the blank ones/zero filling number will impact your data(they can be 0, then it can be counted in pre-90 since 0<1994) when doing math comparation/filtering.But this project is OK, I have tested and confirmed your filtering has the right result. 


**c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

First, the data for pre-90s and post-90s all from the same trying to compare and find the difference from different populations, as non-parametric, it has one variable as usage quantity of the bike, and two categories(pre and post-90s)).The data is unpaired, and we can easily tell the sample is way over 30, so according to the flowchart we should use z-test to test this hypothesis.

Good Job and Good Luck


Ci(Hans) He

Who is winning the NL Central this Weekend!?
================
Brandon Hoeft
9/26/2018

-   [Analytical Approach](#analytical-approach)
-   [Simulation Approach](#simulation-approach)
-   [Let's check against someone much smarter than me](#lets-check-against-someone-much-smarter-than-me)
-   [R Markdown](#r-markdown)

It is the end of the 2018 regular season in MLB. The Chicago Cubs are on everybody's mind at my office, and of course it's hard for me to sympathize as a long-time Milwaukee Brewers fan.

The dynamic right now is quite interesting. As of today, September 26, 2018, the NL Central standings looks as follows. The Cubs have a 0.5 game lead on the Brewers because they have played one less game.

![](./images/standings_9_26_2018.png)

The Cubbies have 5 games left to play and the Brewers have only 4. The team with the most wins will win the division. If the division standings end in a tie for first place, a 1 game playoff will be played to crown the division champion. So, **What is the probability that the Brewers will steal the division title from the Cubs?** The answer to this question can be estimated by identifying how likely it is the Brewers win at least the same number of games as the Cubs. This is equivalent to the Cubs losing at least 1 more game remaining than the Brewers.

To approach this problem, I built a simple data model based upon a mathematical function called the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution). Binomial distributions are useful in estimating the probability of binary event outcomes, like "Heads" or "Tails" of a coin flip. In our use case, given **n** games left to play, and an underlying probability **p** of winning a game, we can measure the likelihood of any number of Wins using these 2 parameters for a given team.

We'll build a data model for each the Cubs and the Brewers probability of winning **X** more games, using their respective winning percentages as parameter **p**, and their respective **n** number of games left.

Analytical Approach
-------------------

To solve this analytically, we apply a little math magic . . .

1.  Calculate the probability of winning **X** games with **n** left to play, given **p**, the team's winning percentage. We use a function called `dbinom()` in the statistical programming language, `R`, to do this easily.

2.  Use matrix multiplication to calculate the [joint probability](http://www.statisticshowto.com/joint-probability-distribution/) of the Cubs and Brewers winning exactly **X** of their remaining games (ex. Brewers win 1 more and Cubs win 3 more). In probability theory, you multiply probability of different events/outcomes when they are assumed independent of each other. Since the Cubs and Brewers don't play any more games against each other, this is a fair assumption to make.

3.  Sum all the joint probabilities where the Brewers won the same number of games or more than the Cubs. This is the final probability answer to our question.

Simulation Approach
-------------------

Let's check against someone much smarter than me
------------------------------------------------

Let's get a reality check on whether this math checks out. We can look to Nate Silver's www.fivethirtyeight.com and their [MLB standings projections](https://projects.fivethirtyeight.com/2018-mlb-predictions/?ex_cid=rrpromo) for comparison.

![](./images/538_mlb_projections_9_26_2018.png)

To do this, we

This weekend is going to be very angsty for a lot of baseball fans. Since probability is an interest of mine, as well as an underlying theme of this blog, I started doing a back of the envelope calculation of \*\*What is the probability

R Markdown
----------

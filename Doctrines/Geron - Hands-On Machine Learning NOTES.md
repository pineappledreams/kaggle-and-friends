# Chapter 1 - What is Machine Learning

## What is machine learning

Machine Learning is the science (and art) of programming computers so they can  
learn from data.  

They can help you by:  

* Machine Learning can simplify code and perform better.
* Can automate it's efficiency and adapt to new data.
* Find new patterns in things.  

### How are machine learning seperated

Machine Learning Systems are seperated by:  

* Whether or not they are trained with human supervision (supervised, unsuper‐
vised, semisupervised, and Reinforcement Learning)

• Whether or not they can learn incrementally on the fly (online versus batch
learning)

• Whether they work by simply comparing new data points to known data points,
or instead detect patterns in the training data and build a predictive model, much
like scientists do (instance-based versus model-based learning)

Of course they can be mixed and matched to your liking.  

## Seperation by supervision  

In here we will be talking about Supervised, Unsupervised, Semisupervised and Reinforcement Learning.  

### Supervised Learning

By supervised learning, the classical example is the spam filter.  
People get an annoying letter, they *label* it SPAM.  
Algo decides that yup, I will take it into consideration and see where it goes.  
The typical learning task is **classification** - spam or not spam (classes).  
The other typical task is predicting a *target* numeric value given features  
also known as *predictors*. This is called **regression**. You train this  
by giving it a whole ton of cars, whatever features you got and the target  
price labels attached.  

NOTE: Attribute is the class label - mileage, but feature is attribute plus value.  
However, people mix them all the time (Such is the sciences of our time).  

So why is it called a regression when we are predicting stuff?  
    Answer: Thanks to a man named Francis Galton he noticed that tall people  
    tended to have manlet children.  
    So he called it *regression to the mean* and here we are. You use words and  
    it don't mean what you think it do.

However - some regression algorithms can be used for classification as well.  
    Example: logistic regression is used for classification, and it can  
    output value  that corresponds to the probability of belonging into a  
    class. For example: 50% beast, 50% machine, 100% man etc.  

Most important Supervised Learning Algos:  
    *k-Nearest Neighbors
    *Linear Regression
    *Logistic Regression
    *Support Vector Machines (SVMs)
    *Decision Trees and Random Forests
    *Neural Networks (can be also semisupervised and unsupervised)

### Unsupervised learning

It means that you run your algo, it takes raw, unlabeled data and just goes to town.  
Important algos:  

* Clustering
  * K-Means
  * DBSScan
  * Hierarchical Cluster Analysis (HCA)
* Anomaly detection and novelty detection
  * One-class Support Vector Machines
  * Isolation Forest
* Visulation and Dimensionality reduction
  * Principal Component Analysis (PCA)
  * Kernel PCA
  * Locally-Linear Embedding (LLE)
  * t-distributed Stochastic Neighbor Embedding (t-SNE)
* Association rule learning
  * Apriori
  * Eclat

For example - if you want to know more about your """blog""" visitors, then  
you run a clustering algo to see what kind of demos are you hitting.  
You might notice 40% of your visitors are male die-hard computer nerds,  
20% are young, rich housewives and so on.  Rest are just bots though.  
You can also run an hierarchical clustering algo and see that  
70% of your bots are of Russian origin, 20% Chinese and 10% zombies.  

Visualization algos are good examples of unsupervised algos -  
you give it LOADS of complex, unlabeled data and it gives you a 2D/3D representation  
of your data that can be plotted.  
These algos will try to preserver your structure(seperate clusters in the input space  
from overlapping in the visualization)  
So YOU can understand how your data is organized and identify unsuspected patterns.  

A related task is dimensionality reduction - where the goal is to simplify the data  
wihout losing too much information. One way is to merge several correlating  
features into one.  
For example - Cars mileage are usually correlating with age, so dimensionality  
reduction algo will merge them into one feature that means "Wear & Tear".  
Another example - Counts, Viscounts, Dukes, Kings, Barons, Baronets, Queens,  
Marquis, Earl...  
"Do men ever visit Boston?" - Duke, Marquis, Earl(aka. Count), Viscount, Barons, with the Duke on top.  
What do they all got in common? They are all NOBLES! So instead of having like 90 different titles,  
just slam them all together into nobles.  
Much like in statistics you also put all "working class" into somebody who earns X amount of money per year  
even though they are baristas, book sellers, popcorn peddlers, till monkeys and desk jockeys etc.  
This is all called **Feature Extraction**

It's a good idea to reduce dimensionality before you move your data on to another algo.  
It will run faster.. maybe  

Another important unsupervised task is **anomaly detection** - detecting  
unusual credit card transactions, catching manufacturing defects or  
just *removing outliers from a data set before feeding it into another algo.*  
System gets loads of normal data, it learns to recognize it.  
When you add more new data, it will know if it's normal or an anomaly.  
Another similar task is **novelty detection**.  
Novelty detection - excepts to see only normal data.  
Anomaly detection - tolerates outliers.  

**Association rule learning** is also very common. It digs into large amounts of data  
and discovers interesting relations between attributes.  
Book brings out idea that if you are running a supermarket, then you might notice that  
barbecue sauce and potato chip buyers also buy steak, so you put them together.  
In reality - drunk driving incidents may happen en route to or from 24/7 alcohol stores.
<https://www.thestate.com/opinion/letters-to-the-editor/article102241157.html>  

### Semisupervised learning

These algos deal with partially labeled data - usually just a little bit of labels,  
rest is unlabeled.  Photo-hosting services are good examples -  
It can show that X person shows up in same photos at the same event while Y in other pics.  
Then it can put X and Y together so you can find your gf at any pics.  
One label per person!  

Semisupervised Learning is usually a combination of different algos.  
Deep Belief Network (DBN) is based on unsupervised component called  
Restricted Boltzmann Machines (RBM) stacked one upon another.  
RMBs are trained in an unsupervised manner, then the whole syste mis fine-tuned  
using supervised learning techniques.  

### Reinforcement Learning  

This is quite different from the aforementioned three learning styles.  
Reinforcement Learning involves an **agent** observing the environment, selecting and  
performing actions and it will get **rewards or penalties** to it's actions.  
It must choose the best **policy** - which actions to take at which situation -  
to get most rewards over time.  

For example -  robots learning to walk, or DeepMind's AlphaGo defeating  
the world champ Ke Jie in Go.  
Or just babies learning that fire is hot by getting burned a bit.  

Observe -> Select action -> Action -> Get points -> Update policy -> Iterate until best policy is found.  

## Batch and Online Learning

Another criterion used to classify Machine Learning systems is whether or not  
the system can learn incrementally from a stream of incoming data.  

### Batch Learning

This DOES NOT learn incrementally - it must be trained using all the available data.  
So it's usually done offline. First it's trained, then it's run.  **Offline learning!**  
So if you want to update the system, you gotta train the new version fromm scratch  
on the new full dataset (Not just new data, but old data), stop the old system  
then you can roll it out.  

But the whole process can be automated p. easy.  Just update the data and retrain and run it again!  

The solution is easy and works fine, but training the full data set can take hours.  
It cannot react on the fly.  

Also traning on the full set of data would take loads of computing resources,  
CPU/memory/disk space/ disk IO, network IO...  
If you got loads of data and automate the system to train every day, you are using  
quite a lot of resources BY THE DAY.  

So you need to choose where you apply batch learning. Obviously  
don't use it on your iPhone or smth lmao.  

### Online learning

Online Learning means that you train your system by feeding it data instances  
individually or in bite-sized mini-batches. Learning is fast and cheap,  
so it can learn on the fly.  

Online learning is great for things that NEED to learn on the fly...  
But more importantly - it works for when you have limited computing resources.  
Once and online learning system has learned about your data, it does not need them anymore  
so you can just discard them (unless you need to roll back/replay data).  

It also works when you need to learn out-of-core (out of main memory), so you learn  
about the big thing one batch at a time. It breaks up the huge 10TB database into  
idk, 100mb chunks and it learns 100mb at a time.  

FYI: **out-of-core is usually done offline (not on a live system), so saying  
it's online is confusing. Use Incremental Learning word instead.**

One important parameter on your online learning systems is how fast can they  
adapt to changing data - what is the *learning rate* of the system.  
High learning rate = adapts quickly to changes, but forgets learned rules.  
Low learning rate = intertia is high, but less sensitive to change.  

The big challenge for online learning system is when you get bad data fed into the system.  
You will see a drop in performance which might linger for a long time and on a live  
system your clients will notice. For example - your search engine gets SPAMMED  
with huge amounts of crap to rank high on the results. Or a malfunctioning sensor  
is feeding crap into the system.  

You will need to monitor your system, switch learning off in these cases and  
maybe even revert to a previous, more fit state.  
Also react to abnormal data by using anomaly detection algorithms.  

## Instance-based learning VS Model-based learning

The 3rd way to seperate your systems is by how they generalize.  
Most ML tasks are about making predictions, which means that given a number  
of training examples, it can generalize to the examples never seen before.  
Having a good performance measure on the training data is good, but insufficient.  
The main goal is to use it IRL.  

### Instance-based learning  

The most trivial of the learning - it learns ALL the stuff that it has seen,  
then automatically flags exact same things it has seen.  
You make it better by giving it the ability to find similar things to other  
instances as well by the measure of similarity.  

## Model-based learning

You build a model out of your examples, then use that model to make predictions.  

For example - does having more money make you happier? OECD data, Happiness data,  
put em together and see. Well, there seems to be a trend, but it's noisy.  
It looks like it goes more or less linearly upwards. So you model life satisfaction  
as a linear function to GDP per capita.  
So you select linear model of life satisfaction with just one attribute - GDP per capita.  

life_satisfaction = theta0 + theta1x * GDP_per_capita

The model has two parameters - theta 0 and theta 1.
(Theta is frequently used to represent model parameters)  

So you've got two things you gotta figure out - theta0 and theta1.  
How can you know which values will make your model perform best?  
You will need to specificy a performance measure.  
Utility function (Fitness function) - How good the modle is.
Cost function - How bad it is.  

For linear regression problems, people typically use a cost function that measures  
the distance between linear predictions and training examples. You gotta minimize the  
distance.  

So that's where the linear regression algorithm comes it -  you feed it examples and  
it will come with the parameters which makes your linear model fit best to your data.  
This is called training the model.  

NOTE: all code examples are over here, so take a gander!!

<https://github.com/ageron/handson-ml2>

Replacing the Linear Regression model with k-Nearest Neighbors
regression in the previous code is as simple as replacing these two
lines:  

```python
import sklearn.linear_model
model = sklearn.linear_model.LinearRegression()
```

with these two:

```python
import sklearn.neighbors
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
```

If your model can make good predictions, then great. But usually you will  
need more attributes, get more/better data or select a better model  
like a Polynomal Regression Model.  

Summary:  

1. Study the data
2. Select a model
3. Train the algo to minimize cost function
4. Apply model to make predictions on new cases (aka. **inference**)

This is the typical life cycle. But this is the typical *good* day in ML.  
Remember the Murphy's law - if it can break, then it will break.  

## The Main Challenges of Machine Learning

Since your main work is going to be selecting a learning algo and train it on  
the data, you will hear people complain about bad algos or bad data.  

**BAD DATA** can be all sorts - insufficient, biased, nonrepresentative, poor quality,  
irrevelant,  overfit, underfit or just plain wrong, false data.  

**Insufficient data** - just like you point an apple to a child, you do the same for computers.  
Except computers need to see like a million of apples before it finally understand  
ah, an apple. OK.  Then it still mixes up a pear (nashi) with an apple.  

In 2001, Microsoft nerds Michele Banko and Eric Brill found that loads of data  
can make algos perform better - but let's be honest - unless we got access to Facebook  
level data, you will not be able to do BIG DATA.  

**Nonrepresentative Training Data** - remember that GDP and Happiness linear function?  
Did you know it didn't have countries like Brazil, Norway & Luxembourg on it, which TOTALLY  
skewed your model and blew it apart.  

If your sample set is too small - it will have sampling noise -  
nonrepresentative data as a result of chance!  

If it's too big, then it can be sample biased aka. the collection was wrong.  
For example - if you write to 1000 people and ask them about a heated topic and  
all of them happen to be in an extreme clique, you won't be able to make an generalization  
for the general population.  

Or if you use Youtube to make a Shazam clone, you might end up with biased music  
which is "hip" in your local area or whatever Youtube is being paid to promote to  
the general ilk. (For example if you write in "rock" into the searchbar  
you will get boomer rock music in USA but OK ONE ROCK in Japan. Well..  
Not me at least - but if I were a normie, I would get OK ONE ROCK here.)

**Poor Quality Data** - Full of errors, outliers and noise - you will need  
to spend your time to *clean your data*. If you were a 9-5 Data Science Person,  
this is where the 90% of the work is.  (The rest of the 10% is the other 90%)  

If you got outliers - you can discard or fix the data.  
If you got missing features - you can either ignore the attribute altogether,  
fill in with the missing value, ignore those instances only, or train a model  
with and without the attribute!  

**Irrevelant features** - Garbage in, garbage out! If you put too much crap into  
your training data, then boom, no wonder you get crap predictions as well.  
The critical part of your success story is coming up with a good set of features  
to train on. This is called *feature engineering* - a big word you will hear a lot.  

Feature engineering is done with:  
    * Feature selection - choosing the most useful attributes to train on.  
    * Feature extraction - combining existing attributes to produce a more useful one  
    * Creating new features by gathering new data.  

Let's also talk about **BAD ALGOS**.  

**Overfitting** - You use ea polynomal life satisfaction model and it overfits THE HECK  
out of the thing. It notices crap like countries with a w in it has high life satisfaction.  
New Zealand, Sweden, Switzerland..  Now how about countries like Rwanda and Zimbabwe?  
How about Wongolia or Whina?

Overfitting happens when the model is too complex relative to the amount and  
noisiness of your training data.  Possible solutions:

* Simplify the model by selecting the one with fewer parameters or  
  reducing number of attributes or constraining the data..  
* Gather more training data
* Reduce noise in the training data.  

Constraining a model to make it simpler is called **regularization**

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
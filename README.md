# Machine Learning CS0451 Project Proposal

Cece Ziegler, David Bryne, Julia Fairbank
April 7th, 2023

# Utilizing Biomechanical and Force Plate Data to Predict Bat Speed for Baseball Hitters

Abstract

Our project will address the future of baseball training by understanding the underlying factors that contribute to athlethic success. We are pulling our data from the Open Biomechanics Project (OBP), which is an open source project from Driveline Baseball, the leading data driven player development facility in Seattle, WA. The data was captured using a combination of ground force plates, a marker motion capture system, bat speed sensors, and ball flight monitors. As a result, the data available is rather robust, with time series force plate data in all three dimensions, hip, torso, shoulder, and hand velocities, as well as bat speed and ball flight data. In essence, every piece of information that is responsible a baseball swing is accounted for. 

Our project hopes to determine the most important factors that affect players' statistics, primarily bat speed. We anticipcate beginning with an initial unsupervised data scrub to determine which variables have the strongest correlation to bat speed, then using those variables to build some predictive model. 

Ultimately, we will evaluate our success based on our ability to explain our dataset, our predicitive model, and our approach. Regardless of how strong our model ends up, we are priortizing creating a project that is detailed and easy to understand. Throughout this project, we anticipate making weekly goals that correspond to our greater goal of creating a strong, fair predicitive model. As we work through the next few weeks, setting and reaching weekly goals will allow us to be realistic about the work ahead to meet our final goal, and allow us to adjust as necessary. 

In building a predicitve model for bat speed, we could help inform coaching decision when it comes to developing hitters. If an athlete's true bat speed closely aligns with their predicted bat speed, this would mean that they are currently moving efficiently in the swing. In other words, they are transfering all of the energy they produce through the bat and into contact. On the other hand, if a hitter did not meet their predicted bat speed value, this would be indicitve of a mechanical inefficiency. As a result, a coach with access to this data and model would be able to bucket athletes into two main groups: strength focused and skill focused. Players with efficient movements would benefit from strength training to increase their baseline capabilities for bat speed, whereas players with high force production would benefit from a mechanical focus.

https://github.com/drivelineresearch/openbiomechanics


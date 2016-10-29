# pinder
Tinder for papers

This is an open source project under GPL3.0. The initial aim of this project is to build a ranking system for arXiv papers. The user would swipe right and left on daily arXiv papers and the platform learns what they like and rank the future daily feeds according to what it thinks is their prefernce. This makes it significantly easier for users to browse through newly posted papers and remain up to date. This is specially a big problem for researchers coming back from hollidays :)

My initial impression about tools and techniques used in this project is the following: Natural language processing and text analysis (to extract features from the summatry and abstract of the papers), Topic Modelling (to map out trending topics), Data visualization toolboxes (to create a dashboard that feeds back to the user what they like, in case they're unaware of their latent tendencies- things like a word cloud of the papers they like, topic trend of what they like over time, etc), Classification or collaborative filtering once we have a larger user base (to rank unseen papers according to users prefences)

# USBaggingClassifier
# Overview
Bagging Classifier with Under Sampling.  
This approach is good for classification imbalanced data.  
You can use both of Binary or Multi-Class Classification.  
Methods could use looks like sci-kit learn's APIs.  
Only use in python 3.x
# Usage
## Parameters
* base_estimator : object    
Classifier looks like sklearn.XXClassifier.  
Classifier must have methods [fit(X, y), predict(X)].  
It is not nesessary predict_proba(X), but if it has this method,  
you could select 'soft voting' option and get predict probability.  
* n_estimators : int (default=10)  
The number of base estimators.  
* voting : str {'hard','soft'} (default='hard')  
hard : use majority rule voting  
soft : argmax of the sums of prediction probabilities  
* n_jobs : int (default=1)  
number of jobs to run in parallel for fit.  
If -1, equals to number of cores.  
## methods
* fit(X, y)  
X : pandas.DataFrame  
y : pandas.Series  
return : None  
* predict(X)  
X : pandas.DataFrame  
return : predicted y : numpy.array  
* predict_proba(X)  
X : pandas.DataFrame
return : predicted probabilities (mean of all bagged models)

# LICENSE
This software is released under the MIT License, see [LICENSE](/LICENSE)
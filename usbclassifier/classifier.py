import numpy as np
import pandas as pd
import copy
import inspect
import collections


class USBaggingClassifier():
    def __init__(self, base_estimator, n_estimators=10, voting='hard', n_jobs=1):
        if voting not in ['hard', 'soft']:
            raise ValueError('voting: You can select only "hard" or "soft".')

        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.voting = voting
        self.n_jobs = n_jobs
        self.models = []
        self.classes_ = None
        self.estimator_methods = [x[0] for x in inspect.getmembers(base_estimator, inspect.ismethod)]

    def _under_sampling(self, df, column_name):
        value_counts = df[column_name].value_counts().sort_values(ascending=True)
        df_each_classes = []
        for i in range(len(value_counts)):
            df_one_class = df[df[column_name] == value_counts.index[i]]
            if i != 0:
                df_one_class = df_one_class.sample(n=len(df_each_classes[0]))
            df_each_classes.append(df_one_class)

        df_balanced = pd.concat(df_each_classes, axis=0)
        df_balanced = df_balanced.reset_index(drop=True)
        return df_balanced

    def fit(self, X, y):
        models = [copy.deepcopy(self.base_estimator) for i in range(self.n_estimators)]
        y_column_name = y.name
        df = pd.concat([X, y], axis=1)
        for model in models:
            df_sampled = self._under_sampling(df, y_column_name)
            X = df_sampled.drop(y_column_name, axis=1)
            y = df_sampled[y_column_name]
            model.fit(X, y)
        self.models = models
        self.classes_ = models[0].classes_

    def predict(self, X):
        if self.voting == 'hard':
            y_predicts = []
            for model in self.models:
                y_predicts.append(model.predict(X))
            y_predicts = np.array(y_predicts).T
            y_pred = []
            for y_pred_votes in y_predicts:
                pred_count_dict = collections.Counter(y_pred_votes)
                y_pred.append(pred_count_dict.most_common(1)[0][0])
            return y_pred

        elif self.voting == 'soft':
            probabilities = self.predict_proba(X)
            prob_idx = probabilities.argmax(axis=1)
            y_pred = [self.classes_[i] for i in prob_idx]
            return y_pred
        else:
            raise ValueError()

    def predict_proba(self, X):
        if 'predict_proba' not in self.estimator_methods:
            raise AttributeError('This model does not have method "predict_proba".')
        y_predicts = []
        for model in self.models:
            y_predicts.append(model.predict_proba(X))
        y_predicts = np.array(y_predicts)
        probabilities = y_predicts.mean(axis=0)
        return probabilities
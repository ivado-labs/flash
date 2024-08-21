# Nixtla Tutorial

The Flash team is excited to share a small tutorial on how to use Nixtla with you.

## What is Nixtla ? 🤔

Nixtla is a Python library designed to simplify time series forecasting.

Nixtla’s ecosystem offers several packages, including the following:

- **StatsForecast**: This offers a wide range of statistical and econometric models, such as Theta, ARIMA, ETS, etc., on a shelf
- **TSFeature**: This package allows you to compute various features from time series data, helping you to understand and extract meaningful information from your datasets.
- **mlforecast**: This package lets you handle all the time series feature engineering elements and two forecasting methods: recursive forecast (one model, multiple time steps prediction) and chained forecast (one model per time step prediction).
You also can utilize models from scikit-learn or other boosting libraries.
- **hierarchicalforecast**: This package enables you to apply popular methods of hierarchical forecast reconciliation, such as MINTS, BottomUp, TopDown, etc. Additionally, it offers a tool to construct a hierarchical dataset.
- **neuralforecast**: This package provides several state-of-the-art deep learning models on a shelf; if we want to name some of us, there’s TemporalFusionTransformer, LSTM, NBEATS, NHITS, etc.

## Why should I use Nixtla?

Here are some reasons why you might consider using Nixtla:

- **An all-in-one tool for time-series forecasting**: It offers various tools and functionalities that streamline the process of building, training, and evaluating forecasting models.
- **Rich implementation of multiple time-series/ML techniques**: It has a very rich and well-documented library of statistical and machine-learning models.
- **Support conformal predictions and hierarchical reconciliation**: It also provides ways to achieve conformal predictions, hierarchical reconciliation, and more. There are lots of very useful tools for us, data scientists, in our forecasting tasks.

## What are Nixtla's limitations?

It seems like the dream tool; why not use it all the time? Well, here are some limitations you should be aware of:
- **Multiple dependencies**: A large number of distinct libraries are required from the Nixtla ecosystem to achieve a basic end-to-end
forecasting project.
- **Performance**: The performance can be slow when experimenting with a very large dataset.
Luckily, Nixtla integrates well with distributed systems like Spark (more about it [here](https://nixtlaverse.nixtla.io/statsforecast/blog/posts/2022-10-05-distributed-fugue/index#statsforecast-code))
Note that it has also been noticed that Pycharm can crash when Plotly is used as an engine for visualization.
- **Documentation**: Although their documentation is very rich, finding what you're looking for can be overwhelming.
For instance, their documentation contains multiple versions (some of them obsolete) of the same evaluation methodology.

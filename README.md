


# Learn Data Engineering with Python

<a href="https://www.packtpub.com/product/data-engineering-with-python/9781839214189?utm_source=github&utm_medium=repository&utm_campaign=9781839214189"><img src="https://static.packt-cdn.com/products/9781839214189/cover/smaller" alt="Learn Amazon SageMaker" height="256px" align="right"></a>

This is the code repository for [Data Engineering with Python](https://www.packtpub.com/product/data-engineering-with-python/9781839214189?utm_source=github&utm_medium=repository&utm_campaign=9781839214189), published by Packt.

**Work with massive datasets to design data models and automate data pipelines using Python**

## What is this book about?
Data engineering provides the foundation for data science and analytics, and forms an important part of all businesses. This book will help you to explore various tools and methods that are used for understanding the data engineering process using Python.

The book will show you how to tackle challenges commonly faced in different aspects of data engineering. You’ll start with an introduction to the basics of data engineering, along with the technologies and frameworks required to build data pipelines to work with large datasets. You’ll learn how to transform and clean data and perform analytics to get the most out of your data. As you advance, you'll discover how to work with big data of varying complexity and production databases, and build data pipelines. Using real-world examples, you’ll build architectures on which you’ll learn how to deploy data pipelines.

By the end of this Python book, you’ll have gained a clear understanding of data modeling techniques, and will be able to confidently build data engineering pipelines for tracking data, running quality checks, and making necessary changes in production.

This book covers the following exciting features: 
* Understand how data engineering supports data science workflows
* Discover how to extract data from files and databases and then clean, transform, and enrich it
* Configure processors for handling different file formats as well as both relational and NoSQL databases
* Find out how to implement a data pipeline and dashboard to visualize results
* Use staging and validation to check data before landing in the warehouse
* Build real-time pipelines with staging areas that perform validation and handle failures
* Get to grips with deploying pipelines in the production environment

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/183921418X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

```

**Following is what you need for this book:**
This book is for data analysts, ETL developers, and anyone looking to get started with or transition to the field of data engineering or refresh their knowledge of data engineering using Python. This book will also be useful for students planning to build a career in data engineering or IT professionals preparing for a transition. No previous knowledge of data engineering is required.

With the following software and hardware list you can run all code files present in the book (Chapter 2-15).

### Software and Hardware List

| Chapter  | Software required                                                                                   | OS required                        |
| -------- | ----------------------------------------------------------------------------------------------------| -----------------------------------|
| 2 - 15   |   Python 3.x, Spark 3.x, Nifi 1.x, PostgreSQL 13.x, Elasticsearch 7.x, Kibana 7.x, Apache Kafka 2.x | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781839214189_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Practical Data Analysis Using Jupyter Notebook [[Packt]](https://www.packtpub.com/product/practical-data-analysis-using-jupyter-notebook/9781838826031) [[Amazon]](https://www.amazon.com/dp/B08BNDJJH6)

* The Data Analysis Workshop [[Packt]](https://www.packtpub.com/product/the-data-analysis-workshop/9781839211386) [[Amazon]](https://www.amazon.com/dp/1839211385)

## Get to Know the Author
**Paul Crickard**
 is the author of Leaflet.js Essentials and co-author of Mastering Geospatial Analysis with Python and the Chief Information Officer at the Second Judicial District Attorney’s Office in Albuquerque, New Mexico.

With a Master's degree in Political Science and a background in Community, and Regional Planning, he combines rigorous social science theory and techniques to technology projects. He has Presented at the New Mexico Big Data and Analytics Summit and the ExperienceIT NM Conference. He has given talks on data to the New Mexico Big Data Working Group, Sandia National Labs, and the New Mexico Geographic Information Council.

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781839214189">https://packt.link/free-ebook/9781839214189 </a> </p>
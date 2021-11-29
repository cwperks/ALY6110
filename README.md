# Running the Notebook

### Virtual Environment

I strongly recommend using a virtual environment when installing the dependencies. Virtual environments help you keep separate python installation and work on different projects on the same computer without installing dependencies globally.

To install a virtual environment run:

```virtualenv <name_of_venv>```

The instructions can also be found [here](https://virtualenv.pypa.io/en/latest/installation.html).

From there activate the virtual environment by running:

```source <name_of_venv>/bin/activate```

You should now see your terminal begin with the name of the virtual environment.

### Installing Apache Spark

If you are on a Mac you can use the following [tutorial](https://www.freecodecamp.org/news/installing-scala-and-apache-spark-on-mac-os-837ae57d283f/) from FreeCodeCamp to install and run Apache Spark which is needed to run the pyspark commands in the notebook.

For Windows Users, the following [https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows/](guide) should help.

### Install Dependencies

To install the dependencies run:

```pip3 install -r requirements.txt```

### Run Jupyter

In the directory where the jupyter notebook is located run:

```jupyter notebook```

When jupyter launches open the notebook titled: `ALY6110.70531_Assignment3_Craig_Perkins_EDA.ipynb`

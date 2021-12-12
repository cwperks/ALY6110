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

### Downloading the data file

Our data can be downloaded from Northeastern OneDrive at this link: [https://northeastern-my.sharepoint.com/:u:/g/personal/perkins_cr_northeastern_edu/EXnkAbD4KDBMn1meaOQ6WCwBKaBDDkcDu5RtpWoQAKhpxQ?e=A2FKRE](https://northeastern-my.sharepoint.com/:u:/g/personal/perkins_cr_northeastern_edu/EXnkAbD4KDBMn1meaOQ6WCwBKaBDDkcDu5RtpWoQAKhpxQ?e=A2FKRE).

If you are running the notebook *Final Project.ipynb*, you need to put the data file (`combined.csv`) in a directory called `data/` under the root of this project.

After cloning this project on your computer, run the following commands.

```
cd ALY6110.70531_Final_Project
mkdir data
cp /path/to/combined.csv data/
# To run the `Connect to Spark Docker Cluster.ipynb` you also need to copy the data to /tmp/spark-data.
mkdir -p /tmp/spark-data
cp /path/to/combined.csv /tmp/spark-data
```

### (Optional) Run Spark on Cluster of Docker Containers

This repo has 2 notebooks that differ in where Spark is run. The notebook titled *Connect to Spark Docker Cluster.ipynb* will run a Spark master node and 2 worker nodes in a cluster of Docker containers. 

To run the cluster please first copy the `combined.csv` dataset into a folder named `spark-data` in `/tmp`

```
mkdir -p /tmp/spark-data
cp data/combined.csv /tmp/spark-data
```

Install Docker and `docker-compose` on your machine. See the instructions from [https://docs.docker.com/compose/install/](Docker) for details.

Run

```
docker-compose down && docker-compose up
```

Please contact Craig Perkins (perkins.cr@northeastern.edu) if you encounter any issues with setup.

Once the 3 containers (1 Master + 2 Workers) are spun up, you can verify by navigating to:

- Master - [localhost:9090](http://localhost:9090)
- Worker 1 - [localhost:9091](http://localhost:9091)
- Worker 2 - [localhost:9092](http://localhost:9092)

Now you are ready to run the *Connect to Spark Docker Cluster.ipynb* workbook.

### Install Dependencies

To install the dependencies run:

```pip3 install -r requirements.txt```

### Run Jupyter

In the directory where the jupyter notebook is located run:

```jupyter notebook```

When jupyter launches open:

1. Notebook that runs with local spark installation: *Final Project.ipynb*
2. Notebook that runs with cluster of docker containers: *Connect to Spark Docker Cluster.ipynb*

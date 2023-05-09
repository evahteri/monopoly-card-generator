# Monopoly card generator

This application is for drawing random cards for playing monopoly.

The card files are from [this](https://github.com/ampersandmcd/Monopoly/blob/master/cards.csv) repository.

The application uses two csv files provided in the repository, you can create your own cards based on them, but do not alter the file names.

### Installing instructions with github clone

- Make sure you have python 3.10 installed.

- Clone this repository.

- Run ``` python3 generator.py ``` in the root of the project.

### Running from Docker image

There is a pre-built Docker image on [Dockerhub](https://hub.docker.com/repository/docker/evahteri/monopoly-card-generator/general)

- Pull the image from Dockerhub 
```docker pull evahteri/monopoly-card-generator```

- Run the program
```docker run -it evahteri/monopoly-card-generator```

### User guide

The application draws random cards designed for Monopoly.

- Press 1 to draw a Chance card

- Press 2 to draw a Community Chest card

- Press 3 to quit

- The card info and actions are printed on the screen.

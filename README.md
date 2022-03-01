# ``ffratings`` - A Fantasy Football draft projection scraper
A Python library for scraping popular fantasy football draft projections

<p align="center">
  <a href="#description">Description</a> •
  <a href="#installation">Installation</a> •
</p>

## Description
The goal for ``ffratings`` is to provide a wrapper to scraping several popular fantasy foot draft project websites for programmatic consumption. 

## Installation
### For Usage in your ownpots

### For development
Getting up and running with ``ffratings`` is just a few commands:

    # Clone ``ffratings``
    git clone https://github.com/pattertj/ffratings.git

    # Install dependencies
    pipenv install -e . --dev

    # Setup pre-commit and pre-push hooks
    pipenv run pre-commit install -t pre-commit
    pipenv run pre-commit install -t pre-push
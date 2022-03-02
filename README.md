# ``ffratings`` - A Fantasy Football draft projection scraper
A Python library for scraping popular fantasy football draft projections

<p align="center">
  <a href="#description">Description</a> •
  <a href="#installation">Installation</a>
</p>

## Description
The goal for ``ffratings`` is to provide a wrapper to scraping several popular fantasy foot draft project websites for programmatic consumption. 

## Installation
### For usage in your own programs

### For development
Getting up and running with ``ffratings`` is just a few commands:

  1) Clone ``ffratings``
  2) Install dependencies
  3) Setup pre-commit and pre-push hooks
    
    git clone https://github.com/pattertj/ffratings.git
    pipenv install -e . --dev    
    pipenv run pre-commit install -t pre-commit
    pipenv run pre-commit install -t pre-push

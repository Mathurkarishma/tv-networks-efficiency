<!-- PROJECT LOGO -->
<p align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TV Network Efficiency Evaluation</h3>

  <p align="center">
    Creating important marketing calculations to determine how effectly a network converts a viewer into a consumer.
    <br />
    <a href="https://github.com/Mathurkarishma/tv-networks-efficiency"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mathurkarishma/tv-networks-efficiency/issues">Report Bug</a>
    ·
    <a href="https://github.com/Mathurkarishma/tv-networks-efficiency/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We will be speaking into 3 different datasets.  Client XYZ advertises their products on several TV networks with airing information and survey data after customers make their purchases.  We will be reviewing these using a lookup table and ultimately put it into a report format through Python.  There will be guidance on the cost to acquire a customer through TV and the most cost-efficient networks so Client XYZ can determine where to increase or decrease spending.  The survey looks like the below image.

<img src="images/survey.png" alt="survey">


### Built With

* [Python](https://www.python.org/)
* [Spyder](https://www.spyder-ide.org/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, download the `Analyst_Dataset.xlsx` Excel file and the `TV_Networks.py` Python file. Then run the code in an IDE software, such as Spyder.  Save them in the same folder.

<!-- USAGE EXAMPLES -->
## Usage

The first step is cleaning up the data.  We intend to create a report that shows calculations of the below per network.  We need to extract important information from each dataset in a format desired for the calculations.

* Cost per Visitor -> Spend/Lift (low is desired)
* Conversion Rate -> Purchases/Lift (high is desired)
* Cost per Acquisition (CPA) -> Spend/Purchases (low is desired)

The output of the code is the monthly report, shown below, with the three calculations.

<img src="images/report.JPG" alt="report">

<!-- CONCLUSION -->
## Conclusion

A few takeaways with each of the calculations are written below.

Cost per Visitor ranges between ~$3 - $70
* Lowest cost is desired
* Science and Comedy Central networks are the highest outlier CPV’s

Conversion Rate ranges between ~0.2% - 4%
* Higher rate is desired
* Majority rates are above 1% except Willow TV, One America News Network, Dish Network, Zee TV, and Star Plus

Cost per Acquisition (CPA) ranges between ~$400 - $5,000
* Lowest cost is desired
* CNBC has unusually low CPA

The guidance includes removing 4 networks.  Comedy Central has a good conversion rate, but cost per visitor and CPA are both too high.  Willow TV, One America News Network, and Zee TV have a poor conversion rate and very high CPA.  It can be recommended to spend on 3 networks.  CNBC, MSNBC, and CNN have a low cost per visitor and CPA and have a higher conversion rate.

<!-- CONTACT -->
## Contact

Karishma Mathur - karishma324@gmail.com

Project Link: [https://github.com/Mathurkarishma/tv-networks-efficiency](https://github.com/Mathurkarishma/tv-networks-efficiency)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SirDaniel1st/plotyDashWebapp">
    Spotify Data Analysis
  </a>

<h3 align="center">BIG DATA PROJECT</h3>

  <p align="center">
  <h3>Abstract—</h3>Music an an intrinsic part of the human experience.One  method  of  consuming  music  in  the  modern  era  is  throughstreaming  platform,  of  which  Spotify  is  one  of  the  most  ubiq-uitous.  <br>
  Spotify  provides  a  wealth  of  data  on  tracks  and  ranksin  the  form  of  the  Top  200  and  Viral  50.  We  use  this  data  toidentify  <br>
  characteristics  common  to  popular  tracks  and  create  aclassifier  to  predict  whether  a  song  will  be  popular  or  not.Index  Terms—music  trends,  music  seasonality,  music  predic-tion,  machine  learning,  Spotify
  
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About The Project

We  have  decided  to  probe  into  Spotify’s  Song  and  TopCharts database to identify what attributes <br>characterize songson  the  Top  Charts.  We  aim  to  visualize  trends,  investigate  iftrends have seasonality and whether genre and acoustic featurefluctuate  by  season  and  location.  With  this,  we  will  createmodels to predict if a particular song will be in the top charts.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Our DataSet
The  Spotify  music  data  was  obtained  from  two  differentKaggle  datasets  namely  the  Spotify  1.2M+  Songs  dataset  byRodolfo Figueroa and Spotify Charts dataset by Dhruvil Dave.Due to the Spotify Charts dataset being updated more regularlythan the Spotify 1.2M+ Songs dataset, more recent songs aremissing  from  the  latter.  Therefore,  the  Spotify  API  is  usedto  supplement  the  existing  data  and  fill  any  missing  datafrom  either  dataset.  The  data  from  both  datasets  is  mergedusing  the  internal  Spotify  ID  as  the  key  in  order  to  combinetrack  features  for  particular  songs  as  well  as  to  allow  formeaningful  analysis  of  the  data.  Additionally,  for  supervisedlearning  songs  that  did  not  make  the  Top  or  Viral  lists  wereextracted from the Song dataset and combined with songs thatdid in equal measure.

Download our [Datasets](https://myuwi-my.sharepoint.com/:f:/g/personal/rajiv_sadho1_my_uwi_edu/ErZLCIrxDDNLkX9RqA4maS8BK9Y9Q068UeQGermqtMTtHA?e=qrSnIU)   

## FireBase

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Park, Minsu, et al. “Global Music Streaming Data Reveal Diurnal andSeasonal  Patterns  of  Affective  Preference.”  Nature  Human  Behaviour,vol.  3,  no.  3,  2019,  pp.  230–236](https://doi.org/10.1038/s41562-018-0508-z.)
* [Araujo, Carlos Soares, et al. “Predicting Music Popularity on StreamingPlatforms.”  Anais  Do  Simp ́osio  Brasileiro  De  Computac ̧ ̃ao  Musical(SBCM 2019), 2019.](https://doi.org/10.5753/sbcm.2019.10436.)
* [Hastie, T., Tibshirani, R., Friedman, J. Unsupervised Learning. In: TheElements of Statistical Learning. Springer Series in Statistics. Springer,New York, NY. 2009. ](https://doi.org/10.1007/978-0-387-84858-714)


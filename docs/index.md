# WCSD COVID-19 Tracker

This website monitors the COVID-19 stats published by the Waukee School District in their [official dashboard](https://waukeeschools.org/rtl/covid-19-information-for-families/)
for the 2021-2022 school year.

Data for the 2020-2021 year is available [here](year2020.html)


## Total cases

The following graph shows the total cumulative staff and students that tested positive since August 25, 2021. The numbers are
updated weekly.

<div id="data-cumulative2021"></div>


## Current number of cases

The information below is numbers as of the timestamp below of anyone who is currently in isolation (positive case).
The dashboard is updated daily, as new cases are confirmed with Dallas County Public Health.

<div id="data-totals2021"></div>


## Number of cases by building


The following graph shows the number of current positive cases per building. The reported numbers are either `0`, `1 to 5`
or the actual number if `6` and above. Numbers between 1 and 5 are shown with a value of 2.5.

<div id="data-buildings2021"></div>



<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.13.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>
<script src="plots.js"></script>

<script type="text/javascript">
  load_plot("data-cumulative2021");
  load_plot("data-totals2021");
  load_plot("data-buildings2021");
</script>

# WCSD COVID-19 Tracker

This website monitors the COVID-19 stats published by the Waukee School District in their [official dashboard](https://waukeeschools.org/rtl/covid-19-information-for-families/)
for the 2021-2022 school year.

Plots and data are being updated.

Data for the 2020-2021 year is available [here](year2020.html)


## Students and staff testing positive

The information below is current numbers as of the timestamp below of anyone who is currently in isolation (positive case).
The dashboard is updated weekly on Friday, as new cases are confirmed with Dallas County Public Health.

The dashboard is to provide current positive cases per building (either `0`, `1 to 5` or the actual number if `6` and above).
Numbers between 1 and 5 are shown with a value of 2.5.

<div id="data-building21"></div>



<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.13.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>
<script src="plots.js"></script>

<script type="text/javascript">
  load_plot("data-building21");
</script>

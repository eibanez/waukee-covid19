# WCSD COVID-19 Tracker

This website monitors the COVID-19 stats published by the Waukee School District in their [official dashboard](https://waukeeschools.org/rtl/covid-19-information-for-families/).

## Students testing positive
<div id="data-students" width="100%"></div>

## Staff members testing positive
<div id="data-staff" width="100%"></div>

## Staff and/or students isolating/quarantining
<div id="data-isolating" width="100%"></div>

## Buildings with known positive cases.
<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.13.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>
<script src="plots.js"></script>

<script type="text/javascript">
  load_plot("data-students");
  load_plot("data-staff");
  load_plot("data-isolating");
</script>

# WCSD COVID-19 Tracker

This website monitors the COVID-19 stats published by the Waukee School District in their [official dashboard](https://waukeeschools.org/rtl/covid-19-information-for-families/)
during the 2019-2020 school year.


## Students and staff testing positive

Student and staff currently testing positive (total students 9,217 in-person, total staff 1,800). Beginning September 18, 2019, the District stopped
reporting the exact number of cases if they are between 1 and 5. The graph below shows a value of 2.5 cases in
those days.

<div id="data-positives"></div>


## Staff/students isolating and being monitored

Staff and/or students currently isolating/quarantining by Dallas County Public Health. Beginning October 5, the District
started reporting the amount of students being monitored, but still in school.

<div id="data-out"></div>


## Buildings with known positive cases

Current buildings or programs with known positive cases.

<div id="buildings"></div>



<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.13.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>
<script src="plots.js"></script>

<script type="text/javascript">
  load_plot("data-positives");
  load_plot("data-out");
  load_plot("buildings");
</script>

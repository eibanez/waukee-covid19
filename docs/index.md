# WCSD COVID-19 Tracker

This website monitors the COVID-19 stats published by the Waukee School District in their [official dashboard](https://waukeeschools.org/rtl/covid-19-information-for-families/).


## Students testing positive

Student(s) currently testing positive (total students 9,217 in-person)

<div id="data-students"></div>


## Staff members testing positive

Staff members currently testing positive (total staff 1,800). Beginning September 18, the District does not
report the exact number of cases if they are between 1 and 5. The graph below uses a value of 2.5 cases in
those days.

<div id="data-staff"></div>


## Staff/students isolating

Staff and/or students currently isolating/quarantining by Dallas County Public Health

<div id="data-isolating"></div>


## Buildings with known positive cases

Current buildings or programs with known positive cases.

<div id="buildings"></div>



<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.13.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>
<script src="plots.js"></script>

<script type="text/javascript">
  load_plot("data-students");
  load_plot("data-staff");
  load_plot("data-isolating");
  load_plot("buildings");
</script>

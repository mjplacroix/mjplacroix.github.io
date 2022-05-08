---
layout: post
title: Have OAI Records Increased Over the Past Yeaer?
subtitle: Need one?
date: 2022-04-21 
author: Michael LaCroix 
tags: [data science, kedro]
---

COVID has affected nearly every part of our lives - personal, work, and beyond. Despite the well known mailman's creed of "Neither snow nor rain nor heat nor gloom of night...", government was no expection to this. We can see this clearly in the collection of data on FDA inspections over the past decade. In the macro - we can see total inspections holding steady between roughly 20-25,0000 from 2010 to 2019. Then, to no one's surprise, we see a steep drop by over 50% in 2020 to 9,638 and still further in 2021 to 7,689. You can see this overall trend clearly below.

<div id="line_chart" style="width: 900px; height: 500px"></div>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var data = google.visualization.arrayToDataTable([
    ['Fiscal Year', 'Total Number'],
      ['2010', 21517],
      ['2011', 25489],
      ['2012', 24774],
      ['2013', 21561],
      ['2014', 20442],
      ['2015', 20447],
      ['2016', 20728],
      ['2017', 21756],
      ['2018', 21546],
      ['2019', 19527],
      ['2020', 9637],
      ['2021', 7689],
      ['2022', 3173]
    ]);

    var options = {
      title: 'Total Inspections',
      // curveType: 'function',
      legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('line_chart'));

    chart.draw(data, options);
  }
</script>


It gets interesting when we zoom in into the types of inspections and the ratios in which they occurred. Here, I want to specifically look at the ratio of Official Action Indicated (OAI) inspections. As a ratio or percent of the total inspections by year, we see a steady rise from 2009 to 2013, a steady decrease from here to 2018, and the beginning of another uptick which actually continued well into COVID with a continued rise in OAI inspections (as a percentage) from 2019-2020 (2.9% -> 3.1%) and 2020-2021 (3.1% -> 3.7%).

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart', 'bar']});

  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawColColors);

  // Callback that creates and populates a data table,
  // instantiates the pie chart, passes in the data and
  // draws it.
  function drawColColors() {

    // Create the data table.
      var data = google.visualization.arrayToDataTable([
['Fiscal Year',
'No Action Indicated (NAI)',
'Official Action Indicated (OAI)',
'Voluntary Action Indicated (VAI)'],
['2009', 62.44459597681554, 3.98340720536424, 33.5719968178202],
['2010', 60.71478365943208, 4.10837942092299, 35.176836919644934],
['2011', 61.16756247793166, 4.59806190905881, 34.23437561300953],
['2012', 63.33252603535965, 4.58545249051424, 32.0820214741261],
['2013', 63.86995037335931, 5.2687723203933, 30.86127730624739],
['2014', 62.09275022013502, 4.8625379121416605, 33.04471186772331],
['2015', 62.54707292023279, 4.94938132733408, 32.50354575243312],
['2016', 65.20165959089155, 3.6375916634504, 31.16074874565804],
['2017', 66.53337010479868, 3.3140283140283096, 30.15260158117301],
['2018', 66.54599461617006, 2.3391812865497, 31.11482409728023],
['2019', 65.16105904644851, 2.92927741076458, 31.90966354278691],
['2020', 62.29116945107399, 3.08187195185223, 34.626958597073774],
['2021', 64.67681102874236, 3.6675770581349902, 31.655611913122637],
['2022', 74.40907658367476, 0.94547746612039, 24.64544595020485]
      ]);

    // Set chart options
      var options = {
        width: 600,
        isStacked: 'percent',
        height: 400,
        legend: { position: 'top', maxLines: 3 },
        bar: { groupWidth: '75%' },
      };

    // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data, options);
  }
  
</script>

It will be interesting to see where it goes from here as the sheer overall number of inspections has started to pick up again. We're only nearing the end of Q1 and already approaching 50% of the inspections for 2021. In fact, if we zoom in again on month-by-month inspection totals from the last 2 years, we can clearly see the number of overall inspections increasing. Which, thankfully, seems to be another indication that we're trending towards a return to normalcy.

*NOTE:* Why data only shows through 2021 - we're using fiscal year as a proxy since the date of completion is actually a lagging indicator

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">

  // Load the Visualization API and the corechart package.
  google.charts.load('current', {packages: ['corechart', 'bar']});

  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawColColors);

  // Callback that creates and populates a data table, instantiates the pie chart, passes in the data and draws it.
  function drawColColors() {
    var data = google.visualization.arrayToDataTable([
      ['Year', 'OAI percent'],
    ['2009', 3.98340720536424],
      ['2010', 4.10837942092299],
      ['2011', 4.59806190905881],
      ['2012', 4.58545249051424],
      ['2013', 5.2687723203933],
    ['2014', 4.8625379121416605],
    ['2015', 4.94938132733408],
    ['2016', 3.6375916634504],
    ['2017', 3.3140283140283096],
    ['2018', 2.3391812865497],
    ['2019', 2.92927741076458],
    ['2020', 3.08187195185223],
    ['2021', 3.6675770581349902],
    ['2022', 0.94547746612039]
  ]);

  var options = {
    width: 600,
    height: 400,
    legend: { position: 'top', maxLines: 3 },
    bar: { groupWidth: '75%' },
    // isStacked: true,
  };

    // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data, options);
  }
  
</script>


# Separator for below tables as reference

<div id="inspections"></div>

<script>
async function getJSON(filename) {
  const response = await fetch(filename)
  return response.json()
}

google.charts.load('current', {
  'packages': ['corechart']
});
google.charts.setOnLoadCallback(loadAndDrawChart);

function loadAndDrawChart() {
  getJSON("../assets/out_inspection.json")
  .then(drawChart)
}

function drawChart(rawData) {
  var data = google.visualization.arrayToDataTable([
    ['Inspection Classification', 'OAI', 'VAI', 'NAI', { role: 'annotation' } ],
    ...rawData.map(
      ({year, NAI, OAI, VAI, oai_ratio}) => {
        return [year, OAI, VAI, NAI, '']
      }
    )
  ]);

  var options = {
    width: 600,
    height: 400,
    // legend: { position: 'top', maxLines: 3 },
    // bar: { groupWidth: '75%' },
    isStacked: true,
    hAxis: { 
      format:'',
      showTextEvery: 1,
      slantedText: true,
      slantedTextAngle: 9,
    },
  };
  var view = new google.visualization.DataView(data);
  var chart = new google.visualization.ColumnChart(document.getElementById('inspections'));

  chart.draw(view, options);
}
</script>

# Inserting space


<!--more-->
# Therapeutic class analysis

Over 80% of API antiviral manufacturing sites that support US markets are located in India and China. <br>

Analgesics have the highest portion of DMFs sourced in the US at 25%.


<div id="aggro" style="width: 900px; height: 500px"></div>

<script>
async function getJSON(filename) {
  const response = await fetch(filename)
  return response.json()
}

google.charts.load('current', {
  'packages': ['corechart']
});
google.charts.setOnLoadCallback(loadAndDrawChart2);

function loadAndDrawChart2() {
  getJSON("../assets/class_antivirals.json")
  .then(drawChart2)
}


function drawChart2(rawData) {
  var data = google.visualization.arrayToDataTable([
    ['Region', 'India', 'China', 'Europe', 'United States', 'Other'],
    ...rawData.map(
      ({year, India, China, Europe, US, Other}) => {
        return [year, India, China, Europe, US, Other]
      }
    )
  ]);
  var options = {
    title: "Geographic evolution of antiviral pharmaceutical manufacturing capacity",
    legend: { position: 'bottom', maxLines: 3 },
    vAxis: {
      minValue: 0,
      ticks: [0, .25, .5, .75, 1],
      title: 'Portion of new Type II currently active API DMFs by region', 
      titleTextStyle: {italic: false}
    },
    hAxis: {
      title: 'Year of DMF Submission', 
      titleTextStyle: {italic: false}
    },
    annotations: {
      textStyle: {
        color: 'black',
      },
    },
    series: [
      {color:'#ec9332'},
      {color:'#c44129'},
      {color:'#3e8410'},
      {color:'#0560bd'},
      {color:'#D3D3D3', visibleInLegend: false},
    ],
    isStacked: 'percent',
  };

    var chart = new google.visualization.AreaChart(
      document.getElementById("aggro")
    );
    chart.draw(data, options);
}
</script>


# Testing a second chart

Over 80% of API antiviral manufacturing sites that support US markets are located in India and China.

<div id="inspections_2"></div>

<script>
async function getJSON(filename) {
  const response = await fetch(filename)
  return response.json()
}

google.charts.load('current', {
  'packages': ['corechart']
});
google.charts.setOnLoadCallback(loadAndDrawChart);

function loadAndDrawChart() {
  getJSON("../assets/out_inspection.json")
  .then(drawChart)
}

function drawChart(rawData) {
  var data = google.visualization.arrayToDataTable([
    ['Inspection Classification', 'OAI', 'VAI', 'NAI', { role: 'annotation' } ],
    ...rawData.map(
      ({year, NAI, OAI, VAI, oai_ratio}) => {
        return [year, OAI, VAI, NAI, '']
      }
    )
  ]);

  var options = {
    width: 600,
    height: 400,
    // legend: { position: 'top', maxLines: 3 },
    // bar: { groupWidth: '75%' },
    isStacked: true,
    hAxis: { 
      format:'',
      showTextEvery: 1,
      slantedText: true,
      slantedTextAngle: 9,
    },
  };
  var view = new google.visualization.DataView(data);
  var chart = new google.visualization.ColumnChart(document.getElementById('inspections_2'));

  chart.draw(view, options);
}
</script>
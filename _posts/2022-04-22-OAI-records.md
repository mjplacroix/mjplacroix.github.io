---
layout: post
title: Have OAI Records Increased Over the Past Yeaer?
subtitle: Need one?
date: 2022-04-21 
author: Michael LaCroix 
tags: [data science, kedro]
---

COVID has affected nearly every part of our lives - personal, work, and beyond. Despite the well known mailman's creed of "Neither snow nor rain nor heat nor gloom of night...", government was no expection to this. We can see this clearly in the collection of data on FDA inspections over the past decade. In the macro - we can see total inspections holding steady between roughly 20-25,0000 from 2010 to 2019. Then, to no one's surprise, we see a steep drop by over 50% in 2020 to 9,638 and still further in 2021 to 7,689. You can see this overall trend clearly below.

- graph created & data output is below -> dataframe to list of lists for javascript function

It gets interesting when we zoom in into the types of inspections and the ratios in which they occurred. Here, I want to specifically look at the ratio of Official Action Indicated (OAI) inspections. As a ratio or percent of the total inspections by year, we see a steady rise from 2009 to 2013, a steady decrease from here to 2018, and the beginning of another uptick which actually continued well into COVID with a continued rise in OAI inspections (as a percentage) from 2019-2020 (2.9% -> 3.1%) and 2020-2021 (3.1% -> 3.7%).

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


It will be interesting to see where it goes from here as the sheer overall number of inspections has started to pick up again. We're only nearing the end of Q1 and already approaching 50% of the inspections for 2021. In fact, if we zoom in again on month-by-month inspection totals from the last 2 years, we can clearly see the number of overall inspections increasing. Which, thankfully, seems to be another indication that we're trending towards a return to normalcy.

*NOTE:* Why data only shows through 2021 - we're using fiscal year as a proxy since the date of completion is actually a lagging indicator
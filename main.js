google.charts.load('current', {packages: ['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    let data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows([
        ['Sport and other activities', 10],
        ['Meeting friends', 5],
        ['Working and coding', 25],
        ['Reading, cooking, and eating', 10],
        ['Watching documentaries and movies', 10],
        ['Checking the latest tech news', 10],
        ['Sleeping & dreaming about starting a new job', 25],
    ]);

    let options = {
        width: 700,
        is3D: true,
        legend: {
            position: 'labeled',
            textStyle: {color: 'white', fontSize: 16}
        },
        enableInteractivity: false,
        pieSliceText: 'none',
        backgroundColor: 'transparent',
        chartArea: {width: '100%', height: '100%'},
        tooltip: {trigger: 'none'},
    };

    // Instantiate and draw our chart, passing in some options.
    let chart = new google.visualization.PieChart(document.getElementById('day-chart'));
    chart.draw(data, options);
}
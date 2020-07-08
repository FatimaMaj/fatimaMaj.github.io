"use strict";

let chartData = {
    labels: [
        "Working and improving my programming skills",
        "Sport and other activities",
        "Sleeping & dreaming about starting a new job",
        "Spending time reading through books plus cooking and eating",
        "Watching documentaries and movies",
        "Checking the latest tech news",
        "Meeting friends"
    ],
    series: [25, 10, 25, 10, 10, 10, 5]
};

new Chartist.Pie("#day-chart", chartData, {
    width: "100%",
    donut: true,
    donutSolid: true,
    donutWidth: "65%",
    labelPosition: "outside"
});
# ATAC-Monitor

The dataset is based on the [Open Data](https://romamobilita.it/it/tecnologie/open-data) by `romamobilita.it`. I collect and store the expected waiting time for bus lines in Rome. For __every bus__ line, we consider the second-last station in the trip. We measure the minutes to be waited for the next upcoming bus at that station. I collect this measure for every bus line every __3 minutes__. This data is stored, and this page shows some statistics.

## Average waiting minutes

We can see the distribution of waiting minutes for every bus line. Every bar in the chart represents a bus line. The length of the bar shows the average amount of minutes to wait.

<iframe style="border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-project-0-urdrh/embed/charts?id=45ebb281-e181-4c1f-9678-cb5b5fad1d24&tenant=b6ce3d2e-8588-4414-bc01-ab06e40b3635"></iframe>

Note that this average may under-estimate the real waiting time. If you are at a stop, but no bus is upcoming, there is no _expected waiting time_. This statistics only takes in account waiting time when a bus left the terminus and is actually driving to the station.

## Average waiting over the day

For every hour of the day, we compute the maximum and the average waiting time for all the __bus lines__.

<iframe style="border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);" width="640" height="480" src="https://charts.mongodb.com/charts-project-0-urdrh/embed/charts?id=511d7883-016b-4510-9a66-2902f0af5fd8&tenant=b6ce3d2e-8588-4414-bc01-ab06e40b3635"></iframe>

On the X-axis we have the hour of the day (`13 = 13:00-13:59`). The lines represents the average waiting time during that hour for all the bus lines.

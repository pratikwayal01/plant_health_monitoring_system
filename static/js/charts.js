// charts.js

// Initialize Chart.js configurations for the report page
document.addEventListener('DOMContentLoaded', function() {

    // Function to create charts
    function createChart(context, type, data, options) {
        return new Chart(context, {
            type: type,
            data: data,
            options: options
        });
    }

    // N-P-K Nutrients Chart
    const nutrientsCtx = document.getElementById('nutrientsChart').getContext('2d');
    const nutrientsData = {
        labels: processedData.chart_data.N.labels,
        datasets: [
            {
                label: 'Nitrogen (N)',
                data: processedData.chart_data.N.values,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                tension: 0.1,
                fill: true
            },
            {
                label: 'Phosphorus (P)',
                data: processedData.chart_data.P.values,
                borderColor: 'rgba(153, 102, 255, 1)',
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                tension: 0.1,
                fill: true
            },
            {
                label: 'Potassium (K)',
                data: processedData.chart_data.K.values,
                borderColor: 'rgba(255, 159, 64, 1)',
                backgroundColor: 'rgba(255, 159, 64, 0.2)',
                tension: 0.1,
                fill: true
            }
        ]
    };
    const nutrientsOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            title: {
                display: true,
                text: 'N-P-K Nutrient Levels Over Time',
                font: { size: 16 }
            },
            tooltip: {
                mode: 'index',
                intersect: false
            }
        },
        scales: {
            y: { beginAtZero: true, title: { display: true, text: 'Nutrient Level' } },
            x: { title: { display: true, text: 'Date' } }
        }
    };
    createChart(nutrientsCtx, 'line', nutrientsData, nutrientsOptions);

    // Temperature Chart
    const temperatureCtx = document.getElementById('temperatureChart').getContext('2d');
    const temperatureData = {
        labels: processedData.chart_data.temperature.labels,
        datasets: [{
            label: 'Temperature (°C)',
            data: processedData.chart_data.temperature.values,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            tension: 0.1,
            fill: true
        }]
    };
    const temperatureOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { title: { display: true, text: 'Temperature Over Time', font: { size: 16 } } },
        scales: { y: { title: { display: true, text: '°C' } } }
    };
    createChart(temperatureCtx, 'line', temperatureData, temperatureOptions);

    // Humidity Chart
    const humidityCtx = document.getElementById('humidityChart').getContext('2d');
    const humidityData = {
        labels: processedData.chart_data.humidity.labels,
        datasets: [{
            label: 'Humidity (%)',
            data: processedData.chart_data.humidity.values,
            borderColor: 'rgba(54, 162, 235, 1)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            tension: 0.1,
            fill: true
        }]
    };
    const humidityOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { title: { display: true, text: 'Humidity Over Time', font: { size: 16 } } },
        scales: { y: { title: { display: true, text: '%' } } }
    };
    createChart(humidityCtx, 'line', humidityData, humidityOptions);

    // pH Chart
    const pHCtx = document.getElementById('pHChart').getContext('2d');
    const pHData = {
        labels: processedData.chart_data.pH.labels,
        datasets: [{
            label: 'Soil pH',
            data: processedData.chart_data.pH.values,
            borderColor: 'rgba(255, 206, 86, 1)',
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            tension: 0.1,
            fill: true
        }]
    };
    const pHOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { title: { display: true, text: 'Soil pH Over Time', font: { size: 16 } } }
    };
    createChart(pHCtx, 'line', pHData, pHOptions);

    // Rainfall Chart
    const rainfallCtx = document.getElementById('rainfallChart').getContext('2d');
    const rainfallData = {
        labels: processedData.chart_data.rainfall.labels,
        datasets: [{
            label: 'Rainfall (mm)',
            data: processedData.chart_data.rainfall.values,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            tension: 0.1,
            fill: true
        }]
    };
    const rainfallOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { title: { display: true, text: 'Rainfall Over Time', font: { size: 16 } } },
        scales: { y: { title: { display: true, text: 'mm' } } }
    };
    createChart(rainfallCtx, 'line', rainfallData, rainfallOptions);

});

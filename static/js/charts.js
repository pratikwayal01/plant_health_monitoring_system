        // // Parse the data from Flask
        // const processedData = JSON.parse('{{ processed_data|tojson|safe }}');
        
        // // Validate and ensure no negative values in chart data
        // function validateChartData(data) {
        //     const validatedData = JSON.parse(JSON.stringify(data)); // Deep clone
            
        //     for (const param in validatedData.chart_data) {
        //         validatedData.chart_data[param].values = validatedData.chart_data[param].values.map(value => {
        //             // Ensure all values are non-negative
        //             return Math.max(0, parseFloat(value) || 0);
        //         });
        //     }
            
        //     return validatedData;
        // }
        
        // const safeData = validateChartData(processedData);
        
        // // Initialize Chart.js
        // Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';
        // Chart.defaults.color = '#6c757d';
        
        // // Create charts when DOM is loaded
        // document.addEventListener('DOMContentLoaded', function() {
        //     // N-P-K Nutrients Chart
        //     const nutrientsCtx = document.getElementById('nutrientsChart').getContext('2d');
        //     new Chart(nutrientsCtx, {
        //         type: 'line',
        //         data: {
        //             labels: safeData.chart_data.N.labels,
        //             datasets: [
        //                 {
        //                     label: 'Nitrogen (N)',
        //                     data: safeData.chart_data.N.values,
        //                     borderColor: 'rgba(75, 192, 192, 1)',
        //                     backgroundColor: 'rgba(75, 192, 192, 0.2)',
        //                     tension: 0.1,
        //                     fill: true
        //                 },
        //                 {
        //                     label: 'Phosphorus (P)',
        //                     data: safeData.chart_data.P.values,
        //                     borderColor: 'rgba(153, 102, 255, 1)',
        //                     backgroundColor: 'rgba(153, 102, 255, 0.2)',
        //                     tension: 0.1,
        //                     fill: true
        //                 },
        //                 {
        //                     label: 'Potassium (K)',
        //                     data: safeData.chart_data.K.values,
        //                     borderColor: 'rgba(255, 159, 64, 1)',
        //                     backgroundColor: 'rgba(255, 159, 64, 0.2)',
        //                     tension: 0.1,
        //                     fill: true
        //                 }
        //             ]
        //         },
        //         options: {
        //             responsive: true,
        //             maintainAspectRatio: false,
        //             plugins: {
        //                 title: {
        //                     display: true,
        //                     text: 'N-P-K Nutrient Levels Over Time',
        //                     font: { size: 16 }
        //                 },
        //                 tooltip: {
        //                     mode: 'index',
        //                     intersect: false
        //                 }
        //             },
        //             scales: {
        //                 y: { 
        //                     beginAtZero: true,
        //                     title: { display: true, text: 'Nutrient Level' },
        //                     min: 0 // Ensure y-axis starts at 0
        //                 },
        //                 x: { title: { display: true, text: 'Date' } }
        //             }
        //         }
        //     });
            
        //     // Temperature Chart
        //     const temperatureCtx = document.getElementById('temperatureChart').getContext('2d');
        //     new Chart(temperatureCtx, {
        //         type: 'line',
        //         data: {
        //             labels: safeData.chart_data.temperature.labels,
        //             datasets: [{
        //                 label: 'Temperature (°C)',
        //                 data: safeData.chart_data.temperature.values,
        //                 borderColor: 'rgba(255, 99, 132, 1)',
        //                 backgroundColor: 'rgba(255, 99, 132, 0.2)',
        //                 tension: 0.1,
        //                 fill: true
        //             }]
        //         },
        //         options: {
        //             responsive: true,
        //             maintainAspectRatio: false,
        //             plugins: { 
        //                 title: { 
        //                     display: true,
        //                     text: 'Temperature Over Time',
        //                     font: { size: 16 }
        //                 }
        //             },
        //             scales: { 
        //                 y: { 
        //                     title: { display: true, text: '°C' },
        //                     min: 0 // Ensure no negative temperatures
        //                 }
        //             }
        //         }
        //     });
            
        //     // Humidity Chart
        //     const humidityCtx = document.getElementById('humidityChart').getContext('2d');
        //     new Chart(humidityCtx, {
        //         type: 'line',
        //         data: {
        //             labels: safeData.chart_data.humidity.labels,
        //             datasets: [{
        //                 label: 'Humidity (%)',
        //                 data: safeData.chart_data.humidity.values,
        //                 borderColor: 'rgba(54, 162, 235, 1)',
        //                 backgroundColor: 'rgba(54, 162, 235, 0.2)',
        //                 tension: 0.1,
        //                 fill: true
        //             }]
        //         },
        //         options: {
        //             responsive: true,
        //             maintainAspectRatio: false,
        //             plugins: { 
        //                 title: { 
        //                     display: true,
        //                     text: 'Humidity Over Time',
        //                     font: { size: 16 }
        //                 }
        //             },
        //             scales: { 
        //                 y: { 
        //                     title: { display: true, text: '%' },
        //                     min: 0,
        //                     max: 100 // Humidity can't exceed 100%
        //                 }
        //             }
        //         }
        //     });
            
        //     // pH Chart
        //     const pHCtx = document.getElementById('pHChart').getContext('2d');
        //     new Chart(pHCtx, {
        //         type: 'line',
        //         data: {
        //             labels: safeData.chart_data.pH.labels,
        //             datasets: [{
        //                 label: 'Soil pH',
        //                 data: safeData.chart_data.pH.values,
        //                 borderColor: 'rgba(255, 206, 86, 1)',
        //                 backgroundColor: 'rgba(255, 206, 86, 0.2)',
        //                 tension: 0.1,
        //                 fill: true
        //             }]
        //         },
        //         options: {
        //             responsive: true,
        //             maintainAspectRatio: false,
        //             plugins: { 
        //                 title: { 
        //                     display: true,
        //                     text: 'Soil pH Over Time',
        //                     font: { size: 16 }
        //                 }
        //             },
        //             scales: { 
        //                 y: { 
        //                     min: 0,
        //                     max: 14 // pH scale is 0-14
        //                 }
        //             }
        //         }
        //     });
            
        //     // Rainfall Chart
        //     const rainfallCtx = document.getElementById('rainfallChart').getContext('2d');
        //     new Chart(rainfallCtx, {
        //         type: 'line',
        //         data: {
        //             labels: safeData.chart_data.rainfall.labels,
        //             datasets: [{
        //                 label: 'Rainfall (mm)',
        //                 data: safeData.chart_data.rainfall.values,
        //                 borderColor: 'rgba(75, 192, 192, 1)',
        //                 backgroundColor: 'rgba(75, 192, 192, 0.2)',
        //                 tension: 0.1,
        //                 fill: true
        //             }]
        //         },
        //         options: {
        //             responsive: true,
        //             maintainAspectRatio: false,
        //             plugins: { 
        //                 title: { 
        //                     display: true,
        //                     text: 'Rainfall Over Time',
        //                     font: { size: 16 }
        //                 }
        //             },
        //             scales: { 
        //                 y: { 
        //                     title: { display: true, text: 'mm' },
        //                     min: 0 // Rainfall can't be negative
        //                 }
        //             }
        //         }
        //     });
        // });
    // charts.js

function generateRandomData(min, max) {
    return (Math.random() * (max - min) + min).toFixed(2);
}

// NPK Nutrient Chart
const nutrientsChart = new Chart(document.getElementById("nutrientsChart"), {
    type: 'bar',
    data: {
        labels: ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)'],
        datasets: [{
            label: 'Nutrient Level',
            backgroundColor: ['#4caf50', '#2196f3', '#ff9800'],
            data: [generateRandomData(20, 60), generateRandomData(10, 40), generateRandomData(30, 70)]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'NPK Levels' }
        }
    }
});

// Temperature Chart
new Chart(document.getElementById("temperatureChart"), {
    type: 'line',
    data: {
        labels: ['6AM', '9AM', '12PM', '3PM', '6PM'],
        datasets: [{
            label: 'Temperature (°C)',
            borderColor: '#f44336',
            backgroundColor: 'rgba(244,67,54,0.2)',
            data: [generateRandomData(18, 22), generateRandomData(22, 26), generateRandomData(27, 31), generateRandomData(30, 34), generateRandomData(24, 28)],
            fill: true
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Daily Temperature Variations' }
        }
    }
});

// Humidity Chart
new Chart(document.getElementById("humidityChart"), {
    type: 'line',
    data: {
        labels: ['6AM', '9AM', '12PM', '3PM', '6PM'],
        datasets: [{
            label: 'Humidity (%)',
            borderColor: '#3f51b5',
            backgroundColor: 'rgba(63,81,181,0.2)',
            data: [generateRandomData(80, 90), generateRandomData(70, 85), generateRandomData(60, 75), generateRandomData(65, 80), generateRandomData(70, 85)],
            fill: true
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Humidity Levels' }
        }
    }
});

// pH Chart
new Chart(document.getElementById("pHChart"), {
    type: 'bar',
    data: {
        labels: ['Soil pH'],
        datasets: [{
            label: 'pH Value',
            backgroundColor: '#9c27b0',
            data: [generateRandomData(5.5, 7.5)]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Soil pH' }
        },
        scales: {
            y: { suggestedMin: 4, suggestedMax: 9 }
        }
    }
});

// Rainfall Chart
new Chart(document.getElementById("rainfallChart"), {
    type: 'bar',
    data: {
        labels: ['Rainfall (mm)'],
        datasets: [{
            label: 'Rainfall',
            backgroundColor: '#03a9f4',
            data: [generateRandomData(20, 100)]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Rainfall Measurement' }
        },
        scales: {
            y: { suggestedMin: 0, suggestedMax: 150 }
        }
    }
});

        
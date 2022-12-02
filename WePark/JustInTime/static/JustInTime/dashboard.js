/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs

  const ctx2 = document.getElementById('Chart_2')
  const Chart_2 = new Chart(ctx2, {
    type: 'line',
    data: {
      labels: [
        '5:00',
        '6:00',
        '7:00',
        '8:00',
        '9:00',
        '10:00',
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00',
        '18:00',
        '19:00',
        '20:00',
        '21:00',
        '22:00'
      ],
      datasets: [{
        data: [
          0,
          4.44,
          0,
          0,
          2.2,
          0,
          108.8,
          15.5,
          26.6,
          0,
          0,
          2.2,
          37.7,
          0,
          4.4,
          80,
          0,
          2.2
        ],
        lineTension: 0,
        backgroundColor: '#CCCCCC30',//'transparent',
        borderColor: 'crimson',//'#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#860a23'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })




})()

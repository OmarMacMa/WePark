/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  const ctx = document.getElementById('Chart_1')
  // eslint-disable-next-line no-unused-vars
  const Chart_1 = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Lunes',
        'Martes',
        'Miércoles',
        'Jueves',
        'Viernes',
        'Sábado',
        'Domingo'
      ],
      datasets: [{
        data: [
          /*24000,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034*/
          10,
          20,
          30,
          70,
          25,
          94,
          66
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
          10,
          50,
          55,
          60,
          70,
          76,
          80,
          79,
          78,
          69,
          55,
          40,
          43,
          42,
          43,
          20,
          2
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

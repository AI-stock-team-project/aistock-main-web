// chart js
(function () {
    'use strict'
    drawKospiChart()
    drawKosdaqChart()
  
    function drawKospiChart(){
      var kospi_data = {"2021-01-04":2944.45,"2021-01-05":2990.57,"2021-01-06":2968.21,"2021-01-07":3031.68,"2021-01-08":3152.18,"2021-01-11":3148.45,"2021-01-12":3125.95,"2021-01-13":3148.29,"2021-01-14":3149.93,"2021-01-15":3085.9,"2021-01-18":3013.93,"2021-01-19":3092.66,"2021-01-20":3114.55,"2021-01-21":3160.84,"2021-01-22":3140.63,"2021-01-25":3208.99,"2021-01-26":3140.31,"2021-01-27":3122.56,"2021-01-28":3069.05,"2021-01-29":2976.21,"2021-02-01":3056.53,"2021-02-02":3096.81,"2021-02-03":3129.68,"2021-02-04":3087.55,"2021-02-05":3120.63,"2021-02-08":3091.24,"2021-02-09":3084.67,"2021-02-10":3100.58,"2021-02-15":3147.0,"2021-02-16":3163.25,"2021-02-17":3133.73,"2021-02-18":3086.66,"2021-02-19":3107.62,"2021-02-22":3079.75,"2021-02-23":3070.09,"2021-02-24":2994.98,"2021-02-25":3099.69,"2021-02-26":3012.95,"2021-03-02":3043.87,"2021-03-03":3082.99,"2021-03-04":3043.49,"2021-03-05":3026.26,"2021-03-08":2996.11,"2021-03-09":2976.12,"2021-03-10":2958.12,"2021-03-11":3013.7,"2021-03-12":3054.39,"2021-03-15":3045.71,"2021-03-16":3067.17,"2021-03-17":3047.5,"2021-03-18":3066.01,"2021-03-19":3039.53,"2021-03-22":3035.46,"2021-03-23":3004.74,"2021-03-24":2996.35,"2021-03-25":3008.33,"2021-03-26":3041.01,"2021-03-29":3036.04,"2021-03-30":3070.0,"2021-03-31":3061.42,"2021-04-01":3087.4,"2021-04-02":3112.8,"2021-04-05":3120.83,"2021-04-06":3127.08,"2021-04-07":3137.41,"2021-04-08":3143.26,"2021-04-09":3131.88,"2021-04-12":3135.59,"2021-04-13":3169.08,"2021-04-14":3182.38,"2021-04-15":3194.33,"2021-04-16":3198.62,"2021-04-19":3198.84,"2021-04-20":3220.7,"2021-04-21":3171.66,"2021-04-22":3177.52,"2021-04-23":3186.1,"2021-04-26":3217.53,"2021-04-27":3215.42,"2021-04-28":3181.47,"2021-04-29":3174.07,"2021-04-30":3147.86,"2021-05-03":3127.2,"2021-05-04":3147.37,"2021-05-06":3178.74,"2021-05-07":3197.2,"2021-05-10":3249.3,"2021-05-11":3209.43,"2021-05-12":3161.66,"2021-05-13":3122.11,"2021-05-14":3153.32,"2021-05-17":3134.52,"2021-05-18":3173.05,"2021-05-20":3162.28,"2021-05-21":3156.42,"2021-05-24":3144.3,"2021-05-25":3171.32,"2021-05-26":3168.43,"2021-05-27":3165.51,"2021-05-28":3188.73,"2021-05-31":3203.92,"2021-06-01":3221.87,"2021-06-02":3224.23,"2021-06-03":3247.43,"2021-06-04":3240.08,"2021-06-07":3252.12,"2021-06-08":3247.83,"2021-06-09":3216.18,"2021-06-10":3224.64,"2021-06-11":3249.32,"2021-06-14":3252.13,"2021-06-15":3258.63,"2021-06-16":3278.68,"2021-06-17":3264.96,"2021-06-18":3267.93,"2021-06-21":3240.79,"2021-06-22":3263.88,"2021-06-23":3276.19,"2021-06-24":3286.1,"2021-06-25":3302.84,"2021-06-28":3301.89,"2021-06-29":3286.68,"2021-06-30":3296.68,"2021-07-01":3282.06,"2021-07-02":3281.78,"2021-07-05":3293.21,"2021-07-06":3305.21,"2021-07-07":3285.34,"2021-07-08":3252.68,"2021-07-09":3217.95,"2021-07-12":3246.47,"2021-07-13":3271.38,"2021-07-14":3264.81,"2021-07-15":3286.22,"2021-07-16":3276.91,"2021-07-19":3244.04,"2021-07-20":3232.7,"2021-07-21":3215.91,"2021-07-22":3250.21,"2021-07-23":3254.42,"2021-07-26":3224.95,"2021-07-27":3232.53,"2021-07-28":3236.86,"2021-07-29":3242.65,"2021-07-30":3202.32,"2021-08-02":3223.04,"2021-08-03":3237.14,"2021-08-04":3280.38,"2021-08-05":3276.13,"2021-08-06":3270.36,"2021-08-09":3260.42,"2021-08-10":3243.19,"2021-08-11":3220.62,"2021-08-12":3208.38,"2021-08-13":3171.29,"2021-08-17":3143.09,"2021-08-18":3158.93,"2021-08-19":3097.83}
      drawKospiKosdaqChart('kospiChart', kospi_data)
    }
  
    function drawKosdaqChart(){
      var kospi_data = {"2021-01-04":977.62,"2021-01-05":985.76,"2021-01-06":981.39,"2021-01-07":988.86,"2021-01-08":987.79,"2021-01-11":976.63,"2021-01-12":973.72,"2021-01-13":979.13,"2021-01-14":980.29,"2021-01-15":964.44,"2021-01-18":944.67,"2021-01-19":957.75,"2021-01-20":977.66,"2021-01-21":981.4,"2021-01-22":979.98,"2021-01-25":999.3,"2021-01-26":994.0,"2021-01-27":985.92,"2021-01-28":961.23,"2021-01-29":928.73,"2021-02-01":956.92,"2021-02-02":963.81,"2021-02-03":970.69,"2021-02-04":964.58,"2021-02-05":967.42,"2021-02-08":960.78,"2021-02-09":957.85,"2021-02-10":964.31,"2021-02-15":981.97,"2021-02-16":977.74,"2021-02-17":979.77,"2021-02-18":967.42,"2021-02-19":965.11,"2021-02-22":954.29,"2021-02-23":936.6,"2021-02-24":906.31,"2021-02-25":936.21,"2021-02-26":913.94,"2021-03-02":923.17,"2021-03-03":930.8,"2021-03-04":926.2,"2021-03-05":923.48,"2021-03-08":904.77,"2021-03-09":896.36,"2021-03-10":890.07,"2021-03-11":908.01,"2021-03-12":925.49,"2021-03-15":926.9,"2021-03-16":940.65,"2021-03-17":943.78,"2021-03-18":949.83,"2021-03-19":952.11,"2021-03-22":955.38,"2021-03-23":946.31,"2021-03-24":953.82,"2021-03-25":954.99,"2021-03-26":956.7,"2021-03-29":954.1,"2021-03-30":958.06,"2021-03-31":956.17,"2021-04-01":965.78,"2021-04-02":970.09,"2021-04-05":969.77,"2021-04-06":968.63,"2021-04-07":973.22,"2021-04-08":982.02,"2021-04-09":989.39,"2021-04-12":1000.65,"2021-04-13":1010.37,"2021-04-14":1014.42,"2021-04-15":1013.9,"2021-04-16":1021.62,"2021-04-19":1029.46,"2021-04-20":1031.88,"2021-04-21":1022.22,"2021-04-22":1025.71,"2021-04-23":1026.82,"2021-04-26":1030.06,"2021-04-27":1021.01,"2021-04-28":998.27,"2021-04-29":990.69,"2021-04-30":983.45,"2021-05-03":961.81,"2021-05-04":967.2,"2021-05-06":969.99,"2021-05-07":978.3,"2021-05-10":992.8,"2021-05-11":978.61,"2021-05-12":967.1,"2021-05-13":951.77,"2021-05-14":966.72,"2021-05-17":962.5,"2021-05-18":969.1,"2021-05-20":971.13,"2021-05-21":965.63,"2021-05-24":948.37,"2021-05-25":962.07,"2021-05-26":966.06,"2021-05-27":974.08,"2021-05-28":977.46,"2021-05-31":981.78,"2021-06-01":984.59,"2021-06-02":981.1,"2021-06-03":990.19,"2021-06-04":987.58,"2021-06-07":985.86,"2021-06-08":986.12,"2021-06-09":978.79,"2021-06-10":987.77,"2021-06-11":991.13,"2021-06-14":997.41,"2021-06-15":997.37,"2021-06-16":998.49,"2021-06-17":1003.72,"2021-06-18":1015.88,"2021-06-21":1010.99,"2021-06-22":1011.56,"2021-06-23":1016.46,"2021-06-24":1012.62,"2021-06-25":1012.13,"2021-06-28":1017.91,"2021-06-29":1022.52,"2021-06-30":1029.96,"2021-07-01":1035.64,"2021-07-02":1038.18,"2021-07-05":1047.33,"2021-07-06":1044.96,"2021-07-07":1047.36,"2021-07-08":1034.48,"2021-07-09":1028.93,"2021-07-12":1034.64,"2021-07-13":1043.31,"2021-07-14":1044.98,"2021-07-15":1054.31,"2021-07-16":1051.98,"2021-07-19":1049.83,"2021-07-20":1043.64,"2021-07-21":1042.03,"2021-07-22":1050.25,"2021-07-23":1055.5,"2021-07-26":1047.63,"2021-07-27":1046.55,"2021-07-28":1035.68,"2021-07-29":1044.13,"2021-07-30":1031.14,"2021-08-02":1037.8,"2021-08-03":1036.11,"2021-08-04":1047.93,"2021-08-05":1059.54,"2021-08-06":1059.8,"2021-08-09":1060.0,"2021-08-10":1052.07,"2021-08-11":1051.92,"2021-08-12":1054.09,"2021-08-13":1040.78,"2021-08-17":1011.05,"2021-08-18":1021.08,"2021-08-19":991.15}
      drawKospiKosdaqChart('kosdaqChart', kospi_data)
    }
  
    // feather.replace({ 'aria-hidden': 'true' })
    function drawKospiKosdaqChart(sel, chartData){
      // Graphs
      var ctx = document.getElementById(sel)
      // eslint-disable-next-line no-unused-vars
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: Object.keys(chartData),
          datasets: [{
            data: Object.values(chartData),
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          }]
        },
        options: {
          elements: {
              point:{
                  radius: 0
              }
          },
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false
              }
            }],
            xAxes: [{
              ticks: {
                autoSkip: true,
                maxTicksLimit: 10
              }
            }]
          },
          legend: {
            display: false
          }
        }
      })
    }
})();

// rank
(function() {
    var httpRequest;
    // document.getElementById("ajaxButton").addEventListener('click', makeRequest);
    // var api_url = document.getElementById("api_server_info").dataset
    // console.log(API_SERVER_URL)
    
    // makeRequest(`${API_SERVER_URL}/strategy_rank/`)
    doAjaxFetch('/strategy_rank/',(text) => {
      onSuccess(text)
    })
  
    function doAjaxFetch(url, onSuccess){
      const headers = new Headers();
      headers.append('X-CSRFToken', getCookie('csrftoken'));
  
      fetch(url, {
          method: 'POST',
          headers,
          mode: 'same-origin'  // Do not send CSRF token to another domain.
      }).then(function(response) {
          response.text().then(function(text){
              // console.log(text)
              onSuccess(text)
          })
      });
  }

      /**
     * CSRF 를 위한 부분
     * @param {str} name 
     * @returns 
     */
       function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function makeRequest(url) {
      httpRequest = new XMLHttpRequest();
  
      if(!httpRequest) {
        alert('XMLHTTP Failed');
        return false;
      }
      httpRequest.onreadystatechange = onreadystatechange;
      httpRequest.open('POST', url);
      httpRequest.send();
    }
  
    function onreadystatechange() {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
          // alert(httpRequest.responseText);
          // success
          onSuccess(httpRequest.responseText)
        } else {
          //alert('ajax failed');
          console.log('ajax failed')
        }
      }
    }

    function onSuccess(responseText){
        // console.log(responseText)
        const json = JSON.parse(responseText)
        // console.log(json)
        /*
        el_mo_1 = document.getElementById('rank_mo_1')
        el_mo_1.innerHTML = ''

        var html = ''
        json.mo_1.forEach(it => {
            console.log(it)
            html += `<li class="list-group-item">${it.name}</li>`
        });
        el_mo_1.innerHTML = html*/
        // console.log(json.mo_1)

        appendList('rank_mo_1', json.mo_1)
        appendList('rank_mo_3', json.mo_3)
        appendList('rank_soaring', json.soaring)
        appendList('rank_dual_mo', json.dual_mo)
        appendList('rank_up_freq', json.up_freq)
    }

    function appendList(sel, json){
        el = document.getElementById(sel)
        el.innerHTML = ''

        var html = ''
        json.forEach(it => {
            // console.log(it)
            html += `<li class="list-group-item">${it.name}</li>`
        });
        el.innerHTML = html
    }
})();
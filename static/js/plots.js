function buildRunChart() {
  var url = "http://localhost:5009/runsScatterData";
  d3.json(url).then(function(data){
  
     var runsTeam = data.Runs
     var winsTeam = data.Wins
     var runsLabelsData = data.Layout
     
  var trace1 = {
      x: runsTeam,
      y: winsTeam,
      text: runsLabelsData,
      mode: 'markers'
    };
    
    var data = [trace1];
    
    var layout = {
        autosize: true,
        width: 1000,
        height: 500,
        title: "Runs v. Wins",
        margin: {
          l: 50,
          r: 50,
          b: 100,
          t: 100,
          pad: 4
        },
        paper_bgcolor: "white",
        plot_bgcolor: "white",
        xaxis: {
            title: {
              text: 'Team Runs for the Season',
              font: {
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Wins',
              font: {
                size: 18,
                color: '#7f7f7f'
              }
            }
          }    
    };
    
    Plotly.newPlot('runsScatter', data, layout);
 });
}
buildRunChart();

function buildHomerunChart() {
    var url = "http://localhost:5009/homerunsScatterData";
    d3.json(url).then(function(data){
    
       var homerunsTeam = data.Homeruns
       var winsTeam = data.Wins
       var runsLabelsData = data.Layout
    
    var trace1 = {
        x: homerunsTeam,
        y: winsTeam,
        text: runsLabelsData,
        mode: 'markers'
      };
      
      var data = [trace1];
      
      var layout = {
          autosize: true,
          width: 1000,
          height: 500,
          title: "Homeruns v. Wins",
          margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 100,
            pad: 4
          },
          paper_bgcolor: "white",
          plot_bgcolor: "white",
          xaxis: {
              title: {
                text: 'Team Homeruns for the Season',
                font: {
                  size: 18,
                  color: '#7f7f7f'
                }
              },
            },
            yaxis: {
              title: {
                text: 'Wins',
                font: {
                  size: 18,
                  color: '#7f7f7f'
                }
              }
            }    
      };
      
      Plotly.newPlot('homerunsScatter', data, layout);
   });
  }
  buildHomerunChart();
  
  function buildERAChart() {
    var url = "http://localhost:5009/ERAScatterData";
    d3.json(url).then(function(data){
    
       var ERATeam = data.ERA
       var winsTeam = data.Wins
       var runsLabelsData = data.Layout
    
    var trace1 = {
        x: ERATeam,
        y: winsTeam,
        text: runsLabelsData,
        mode: 'markers'
      };
      
      var data = [trace1];
      
      var layout = {
          autosize: true,
          width: 1000,
          height: 500,
          title: "ERA v. Wins",
          margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 100,
            pad: 4
          },
          paper_bgcolor: "white",
          plot_bgcolor: "white",
          xaxis: {
              title: {
                text: 'Team ERA for the Season',
                font: {
                  size: 18,
                  color: '#7f7f7f'
                }
              },
            },
            yaxis: {
              title: {
                text: 'Wins',
                font: {
                  size: 18,
                  color: '#7f7f7f'
                }
              }
            }    
      };
      
      Plotly.newPlot('ERAScatter', data, layout);
   });
  }
  buildERAChart();
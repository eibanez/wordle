var opts = {
  "actions": false,
  "config": {
    "style": {
      "guide-label": {"fontSize": 12.5},
      "guide-title": {"fontSize": 13.5, "fontStyle": "normal"}
    },
    "header": {"labelFontSize": 14.5},
    "legend": {"orient": "top"},
    "facet": {"spacing": 5}
  }
};

function load_plot(id, name) {
  vegaEmbed("#" + id, "specs/" + id + ".json", opts).then(function(result) {
    if (name) {
      // Filter data, keeping only the one person we want
      result.view.remove('data', d => d.name != name).run();
    }
  }).catch(console.error);;
}

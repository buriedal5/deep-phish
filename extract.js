if (document.body.lastChild.id == "extracted") {
  document.body.removeChild(document.body.lastChild);
}
var newSetlists = document.getElementsByClassName("setlist");
var html = "";
for (var i = 0; i < newSetlists.length; ++i) {
  if (newSetlists[i].classList.contains("excluded")) {
    continue;
  }
  var date = newSetlists[i].getElementsByClassName("sldate");
  html += date[0].innerHTML.substring(date[0].innerHTML.indexOf(",") + 1) + "<br>";
  var paras = newSetlists[i].getElementsByTagName("P");
  for (var j = 0; j < paras.length; ++j) {
    var titles = paras[j].getElementsByTagName("B");
    if (typeof titles[0] != "undefined") {
      html += titles[0].innerHTML + "<br>";
      var songs = paras[j].getElementsByTagName("A");
      for (var k = 0; k < songs.length; ++k) {
        if (songs[k].classList.length == 0 || songs[k].classList.contains("full")) {
          html += songs[k].href + "<br>";
        }
      }
    }
  }
}
var elem = document.createElement("DIV");
elem.id = "extracted";
elem.style.marginTop = "500px";
elem.innerHTML = html;
document.body.appendChild(elem);

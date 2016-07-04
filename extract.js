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
  var showHtml = "";
  showHtml += date[0].innerHTML.substring(date[0].innerHTML.indexOf(",") + 1) + "<br>";
  var paras = newSetlists[i].getElementsByTagName("P");
  var hasSong = false;
  for (var j = 0; j < paras.length; ++j) {
    var titles = paras[j].getElementsByTagName("B");
    if (typeof titles[0] != "undefined") {
      showHtml += titles[0].innerHTML + "<br>";
      for (var k = 0; k < paras[j].childNodes.length; ++k) {
        var node = paras[j].childNodes[k];
        if (node.nodeType == 1
            && node.tagName == "A"
            && (node.classList.length == 0
            || node.classList.contains("full"))) {
          hasSong = true;
          showHtml += node.href + "<br>";
        } else if (node.nodeType == 3) {
          if (node.nodeValue.startsWith(" >")) {
            showHtml += "&lt;into&gt;<br>";
          } else if (node.nodeValue.startsWith(" ->")) {
            showHtml += "&lt;segue&gt;<br>";
          }
        }
      }
    }
  }
  if (hasSong) {
    html += showHtml;
    html += "<br>";
  }
}
var elem = document.createElement("DIV");
elem.id = "extracted";
elem.style.marginTop = "500px";
elem.innerHTML = html;
document.body.appendChild(elem);

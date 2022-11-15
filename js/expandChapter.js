var expandButtons = document.getElementsByClassName("chapter-expand");
for (var i = 0, len = expandButtons.length; i < len; ++i) {
    expandButtons[i].addEventListener("click", function () {
        updateDisplay(this);
    });
}
function updateDisplay(expandButton) {
    var contentArea = siblingContentArea(expandButton);
    if(contentArea.hasAttribute("hidden")){
        contentArea.removeAttribute("hidden");
    }else{
        contentArea.setAttribute("hidden","true");
    }
}
function siblingContent(expandButton) {
    var chapterTag = expandButton.parentElement;
    var articlesContainer = chapterTag.nextElementSibling;
    return articlesContainer;
}
var expandButtons = document.getElementsByClassName("article-expand");
for (var i = 0, len = expandButtons.length; i < len; ++i) {
    expandButtons[i].addEventListener("click", function () {
        updateDisplayState(this);
    });
}
function updateDisplayState(expandButton) {
    var contentArea = siblingContentArea(expandButton);
    updateSenteceDragging(contentArea);
    if(contentArea.classList.contains("collapse")){
        contentArea.setAttribute("display","block")
        contentArea.classList.remove("collapse");
        contentArea.setAttribute("aria-expanded","1");
    }else{
        contentArea.setAttribute("display","none");
        contentArea.classList.add("collapse");
        contentArea.setAttribute("aria-collapsed","1");
    }
} 
function siblingContentArea(expandButton) {
    var articleTag = expandButton.parentElement;
    var articleParagraphArea = articleTag.nextElementSibling;
    return articleParagraphArea;
}
function updateSenteceDragging(contentArea){
    var spanElements = contentArea.getElementsByTagName("span");
    for(var i=0, len=spanElements.length; i<len; ++i){
        var span = spanElements[i];
        if(span.getAttribute("draggable")==true){
            span.setAttribute("draggable",false);
        }else{
            span.setAttribute("draggable",true);
        }
    }
}

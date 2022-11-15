var writeButtons = document.getElementsByClassName("write-article-content");
for (var i = 0, len = writeButtons.length; i < len; ++i) {
    var writeButton = writeButtons[i];
    writeButton.addEventListener("click", function () {
        go(this);
    });
}
// INITIAL DOM MANIPULATION -> functions...
function activeArticleTag(buttonClicked) {
    var articleTag = buttonClicked.parentElement;
    return articleTag;
}
function articleContentArea(articleTag) {
    var articleParagraphArea = articleTag.nextElementSibling;
    return articleParagraphArea;
}
// MAIN FUNCTION -> [enable / disable] editing the article...
function go(buttonClicked) {
    var activeTag = activeArticleTag(buttonClicked);
    var contentArea = articleContentArea(activeTag);
    if (contentArea.classList.contains("edit-on")) {
        enableEditing(contentArea);
        contentArea.classList.replace("edit-on", "edit-off");
        contentArea.setAttribute("display","block");
    }
    else if (contentArea.classList.contains("edit-off")) {
        disableEditing(contentArea);
        updateNotification(contentArea);
        //contentArea.setAttribute("aria-expanded","true");
        contentArea.classList.replace("edit-off", "edit-on");   
    }
}
// DISABLE EDITING -> methods...
function disableEditing(contentArea) {
    var text = updateModifications(contentArea);
    while(contentArea.firstChild){
        contentArea.removeChild(contentArea.lastChild);
    }
    var spanSentences = splitText(text);
    for (var i = 0, len = spanSentences.length; i < len; ++i) {
        contentArea.appendChild(spanSentences[i]);
    }
}
function updateModifications(contentArea) {
    var textArea = contentArea.getElementsByTagName("textarea")[0];
    return textArea.value;
}
// ENABLE EDITING -> functions...
function enableEditing(contentArea) {
    var text = getArticleContent(contentArea);
    var editBox = createTextBox(text);
    placeTextBox(contentArea, editBox);
}
function getArticleContent(contentArea) {
    var contentSpanElements = contentArea.getElementsByTagName("span");
    var textContent = "";
    for (var i = 0, len = contentSpanElements.length; i < len; ++i) {
        textContent += contentSpanElements[i].innerText;
        textContent += " ";
    }
    return textContent;
}
function createTextBox(text) {
    var textarea = document.createElement("textarea");
    textarea.spellcheck = false;
    textarea.name = "Article Content";
    textarea.textContent = text;
    textarea.style.width = "100%";
    textarea.style.minHeight = "200px";
    return textarea;
}
function placeTextBox(contentArea, inputBox) {
    while(contentArea.firstChild){
        contentArea.removeChild(contentArea.lastChild);
    }
    contentArea.appendChild(inputBox);
}
// GENERAL HTML MANIPULATION -> functions
function expandText(contentArea) {
    contentArea.classList.add("show");
}
function updateNotification(contentArea) {
    contentArea.setAttribute("update","true");
}
function wrapInSpan(sentence) {
    var span = document.createElement("span");
    span.setAttribute("draggable",true);
    span.innerText = sentence;
    span.style.marginRight = "0.5%";
    return span;
}
// GENERAL STRING MANIPULATION -> functions
function splitText(text) {
    var sentences = text.split(/(?<=[.;:!?])\s*/g);
    var spanElements = [];
    for (var i = 0, len = sentences.length; i < len; ++i) { 
        if(sentences[i]==""){
            continue;
        }
        spanElements.push(wrapInSpan(sentences[i]));
    }
    return spanElements;
}
// MISSING: EDIT BUTTON COLOR WHEN EDITING (ON/OFF)
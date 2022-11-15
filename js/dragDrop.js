var draggedSpan;

var observeUpdates = new MutationObserver(function (mutations) {
    // declare elements to be iterated-through
    var articleSpanElements = document.querySelectorAll(".article-content > span");
    var contentAreaElements = document.getElementsByClassName("article-content");
    for (var i = 0, len = articleSpanElements.length; i < len; ++i) {
        articleSpanElements[i].addEventListener("dragstart", function () {
            draggedSpan = this;
        });
    }
    for (var i = 0, len = contentAreaElements.length; i < len; ++i) {
        contentAreaElements[i].addEventListener("dragenter", function (ev) {
            ev.preventDefault();
        });
        contentAreaElements[i].addEventListener("dragover", function (ev) {
            ev.preventDefault();
        });
        contentAreaElements[i].addEventListener("drop", function (ev) {
            ev.preventDefault();
            if (draggedSpan.parentElement.id != this.id) {
                draggedSpan.style.marginRight = "0.5%";
                this.appendChild(draggedSpan);
            }
        });
    }
    observeUpdates.disconnect();
});

observeUpdates.observe(document.body, {
    subtree: true,
    childList: true,
    characterData: true,
    attributes: true
});

from xml import Body, Chapter, Article
from airium import Airium
import re

class HTML(Body, Chapter, Article):
    _a = Airium()
    def __init__(self, xml_filepath: str) -> None:
         Body.__init__(self, xml_filepath)
         self.setHTML()
    def setHTML(self) -> None:
        """Call the <head/> and <body/> functions
        """
        a = self.getPointer()
        a('<!DOCTYPE html>')
        with a.html(lang="pl"):
            with a.head():
                self.setHead(a)
            with a.body():
                self.setBody(a)
                self.setScripts(a)
        self.updatePointer(a)

    def setScripts(self, a: Airium) -> None:
        """Create the <script/> tags at the end of the <body></body> tag
        """
        a.script(src="../js/dragDrop.js")
        a.script(src="../js/expandButton.js")
        a.script(src="../js/editArticle.js")
        a.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js", integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/",crossorigin="anonymous")


    def setBody(self, a: Airium) -> None:
        """create the <body></body> tag
        """
        with a.div(klass="body"):
            self.addChapters(a)
        self.updatePointer(a)
    def addChapters(self, a: Airium) -> None:
        """Iterate over the body: etree.Element and append all <chapter></chapter>
        """
        chapters = self.getChapters()
        for chapter in chapters:
            Chapter.__init__(self,chapter)
            with a.div(klass="chapter",number=self.chapter_number(),name=self.chapter_name(),chapter_identifier=self.chapter_identifier()):
                self.addChapterTag(a)
                with a.div(klass="articles collapse show", id=f"chapter-content-{self.chapter_identifier()}"):
                    self.addArticles(a)
        self.updatePointer(a)
    
    # chapter methods
    def addChapterTag(self, a: Airium) -> None:
        """Create an HTML displayer of the attributes of <chapter/>
        """
        with a.div(klass="chapter-tag row"):
            self.addChapterOpenSymbol(a)
            self.addChapterTagName(a)
            self.addChapterAttributesNumberName(a)
            self.addChapterIdentifier(a)
            self.addChapterAppendSymbol(a)
        self.updatePointer(a)
    def addChapterOpenSymbol(self, a: Airium) -> None:
        """Create an arrow button
        """
        with a.button(**{"klass": "chapter-expand col-sm-1 col-md-1 btn", "type":"button","aria-expanded":"true", "data-bs-target":f"#article-content-{self.chapter_identifier()}", "aria-controls":f"article-content-{self.chapter_identifier()}"}):
            with a.svg(klass="arrow-icon", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 100 100"):
                a.path(d="M 95,50 5,95 5,5 z")
        self.updatePointer(a)
    def addChapterTagName(self, a: Airium) -> None:
        """Display the tag name of <chapter/>
        """
        a.div(klass="tag-name col-sm-1 col-md-1",_t="chapter")
        self.updatePointer(a)
    def addChapterAttributesNumberName(self, a: Airium) -> None:
        with a.div(klass="attributes-number-name col-sm-2 col-md-2"):
            a.div(klass="attribute-number",_t="number:")
            a.div(klass="attribute-name", _t="name:")
        with a.div(klass="attributes-number-name-values col-sm-5 col-md-5"):
            with a.div(klass="attribute-number-value"):
                a.span(_t=self.chapter_number())
            with a.div(klass="attribute-name-value"):
                a.span(_t=self.chapter_name())
        self.updatePointer(a)
    def addChapterIdentifier(self, a: Airium) -> None:
        with a.div(klass="attribute-identifier col-sm-2 col-md-2"):
            a.div(klass="chapter-identifier",_t="chapter_identifier")
            with a.div(klass="chapter-identifier-value"):
                a.span(_t=self.chapter_identifier())
        self.updatePointer(a)
    def addChapterAppendSymbol(self, a: Airium) -> None:
        with a.button(klass="add-new-chapter col-sm-1 col-md-1"):
            with a.svg(klass="plus-sign", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 24 24"):
                a.path(d="M24 10h-10v-10h-4v10h-10v4h10v10h4v-10h10z")
        self.updatePointer(a)
    def addArticles(self, a: Airium) -> None:
        articles = self.getArticles()
        for article in articles:
            Article.__init__(self, article)
            with a.div(klass="article",number=self.article_number(),name=self.article_name(),article_identifier=self.article_identifier()):
                self.addArticleTag(a)
                with a.div(
                    **{"klass": "article-content collapse edit-on", 
                    "id": f"article-content-{self.article_identifier()}", 
                    "aria-expanded":"0",
                    "aria-collapsed": "0",
                    "update":"0",
                    }
                ):
                    self.addArticleContent(a)
        self.updatePointer(a)
    
    # article methods
    def addArticleTag(self, a: Airium) -> None:
        with a.div(klass="article-tag row"):
            self.addArticleOpenSymbol(a)
            self.addArticleTagName(a)
            self.addArticleAttributesNumberName(a)
            self.addArticleIdentifier(a)
            self.addArticleWriteSymbol(a)
        self.updatePointer(a)
    def addArticleOpenSymbol(self, a: Airium) -> None:
        with a.button(**{"klass": "article-expand col-sm-1 col-md-1 btn", "type":"button", "data-bs-toggle":"collapse"}):
            with a.svg(klass="arrow-icon", xmlns="http://www.w3.org/2000/svg", viewBox="0 0 100 100"):
                a.path(d="M 95,50 5,95 5,5 z")
        self.updatePointer(a)
    def addArticleTagName(self, a: Airium) -> None:
        a.div(klass="tag-name col-sm-1 col-md-1",_t="article")
        self.updatePointer(a)
    def addArticleAttributesNumberName(self, a: Airium) -> None:
        with a.div(klass="attributes-number-name col-sm-2 col-md-2"):
            a.div(klass="attribute-number",_t="number:")
            a.div(klass="attribute-name", _t="name:")
        with a.div(klass="attributes-number-name-values col-sm-5 col-md-5"):
            with a.div(klass="attribute-number-value"):
                a.span(_t=self.article_number())
            with a.div(klass="attribute-name-value"):
                a.span(_t=self.article_name())
        self.updatePointer(a)
    def addArticleIdentifier(self, a: Airium) -> None:
        with a.div(klass="attribute-identifier col-sm-2 col-md-2"):
            a.div(klass="chapter-identifier",_t="article_identifier")
            with a.div(klass="chapter-identifier-value"):
                a.span(_t=self.article_identifier())
        self.updatePointer(a)
    def addArticleWriteSymbol(self, a: Airium) -> None:
        with a.button(klass="write-article-content col-sm-1 col-md-1"):
            with a.svg(klass="write-symbol",xmlns="http://www.w3.org/2000/svg", fill="currentColor", viewBox="0 0 16 16"):
                a.path(d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z")
        self.updatePointer(a)
    def addArticleContent(self, a: Airium) -> None:
        text = self.getText().strip()
        textTupleMatchList = re.findall("([^\.!\?;:]+[\.!\?:;]+)|([^\.!\?:;]+$)",text)
        for sentence in textTupleMatchList:
            sentence_instance = sentence[0].strip()+sentence[1].strip()
            if(not sentence_instance.endswith(".")) and (not sentence_instance.endswith(";")) and (not sentence_instance.endswith(":")): 
                sentence_instance = sentence_instance+"."
            a.span(_t=(sentence_instance), draggable="false")
        self.updatePointer(a)
    
    # general methods
    def setHead(self, a: Airium) -> None:
        a.meta(charset="utf-8")
        a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
        self.setLinks(a)
        a.title(_t="TESTING ENVIRONMENT")
        self.updatePointer(a)
    def setLinks(self, a: Airium) -> None:
        a.link(rel="stylesheet", integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi", crossorigin="anonymous", href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css")
        a.link(rel="stylesheet", type="text/css", href="../styles/style.css")
        a.link(rel="stylesheet", type="text/css", href="../styles/chapter.css")
        a.link(rel="stylesheet", type="text/css", href="../styles/article.css")
        self.updatePointer(a)
    
    # manipulation methods
    def getPointer(self) -> Airium:
        return self._a
    def updatePointer(self, a: Airium) -> None:
        self._a = a


a = HTML("../xml/pta_1.xml")
x = str(a.getPointer())
with open("index.html","w") as f:
    f.write(x)


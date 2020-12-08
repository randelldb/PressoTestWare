# 64bit required

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from src import dir_path

font_config = FontConfiguration()
html = HTML('test.html')
css = CSS(string='''
    @font-face {
        font-family: Gentium;
        src: url(http://example.com/fonts/Gentium.otf);
    }
    h1 { font-family: Gentium }''', font_config=font_config)

html.write_pdf(dir_path + '/handlers/temp/example.pdf', stylesheets=[css], font_config=font_config)
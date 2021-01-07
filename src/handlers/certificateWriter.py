import bs4
from src import cache

from src.models import CertificateTemplate

def write_data(get_fixed_cert_data, reading):
    # load the file
    with open("src/handlers/cert_res/certificate_template_base.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt, 'html5lib')

        dynamic_data = soup.select(".dynamic_data")
        for i in dynamic_data:
            id = i.get('id')
            new_string = reading[id]
            new_tag = soup.new_tag("span")
            new_tag.string = str(new_string)
            i.span.replace_with(new_tag)

        # Loop over file find id and add fixed data
        fixed_cert_data = soup.select(".fixed_cert_data")
        for i in fixed_cert_data:
            id = i.get('id')
            new_string = getattr(get_fixed_cert_data, str(id))
            new_tag = soup.new_tag("span")
            new_tag.string = str(new_string)
            i.span.replace_with(new_tag)

    # save the file again
    with open("src/handlers/cert_res/certificate_template_base.html", "w") as outf:
        outf.write(str(soup))

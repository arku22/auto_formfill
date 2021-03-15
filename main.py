from PyPDF2 import PdfFileReader as pfr
import sys
import pyperclip
import webbrowser


def getfieldinfo(pfile):
    """This function will take in the name of the pdf form file
        and return a dictionary with details of each field in the pdf form
        as follows : -
        {field_id1: {type:_, value:_}, field_id2: {type:_, value:_}, ...}
        where 'type' tells whether the field is a checkbox/radio button(Btn) or
        text(Tx) or choice(Ch)."""

    # create a file object
    f = open(pfile, 'rb')
    # create an instance of pfr
    r = pfr(f)

    # access the catalog/root dictionary for the file
    my_dict = r.trailer["/Root"]
    # access key /AcroForm
    my_dict = my_dict['/AcroForm']
    # access the /Fields key to get an array object
    fields = my_dict['/Fields']

    extract = {}
    for obj in fields:
        real_obj = obj.getObject()
        # get unique id name
        try:
            id = real_obj['/TM']
        except KeyError:
            id = real_obj['/T']
        # get field type and value
        ft = real_obj['/FT']
        try:
            val = real_obj['/V']
        except KeyError:
            val = 'no_value'

        extract[id] = {'type': ft, 'value': val}

    f.close()
    return extract


def getjavascriptcode(out_file, field_dict):
    with open(out_file, 'w') as file_object:

        for k, v in field_dict.items():

            # for a text field
            if v['type'] == '/Tx':
                temp = "document.getElementById('{id_name}').value="
                temp += "'{val_name}';\n"
                file_object.write(temp.format(id_name=k, val_name=v['value']))

            # for a choice/drop down field
            elif v['type'] == '/Ch':
                temp = """function setdropdown(e, val)
                {
                    for(i=0; i< e.options.length; i++)
                    {
                        if(e.options[i].text==val)
                        {
                            e.options[i].selected = true;
                            return;
                        }
                    }
                }"""
                temp += "\nsetdropdown(document.getElementById('%s'), '%s');\n"
                file_object.write(temp % (k, v['value']))

            # for a checkbox/radio button field
            elif v['type'] == '/Btn':
                if v['value'] != 'no_value':
                    temp = "document.getElementById('{id_name}').checked=true;"
                    temp += "\n"
                    file_object.write(temp.format(id_name=k))


temp = sys.argv
filename = temp[1]
out = '/Users/architkumar/Documents/python_work/auto_formfill/js_code.txt'
getjavascriptcode(out, getfieldinfo(filename))

with open(out, 'r') as f:
    contents = f.read().rstrip()

pyperclip.copy(contents)

js_source = "/Users/architkumar/Documents/python_work/auto_formfill/"
js_source += "Automate-with-Python-_-Form-Filling-Script-/OnlineForm/"
js_source += "js/index.js"

with open(js_source, 'a') as f:
    f.write(pyperclip.paste())

url = "file:///Users/architkumar/Documents/python_work/auto_formfill/"
url += "Automate-with-Python-_-Form-Filling-Script-/OnlineForm/index.html"
webbrowser.open(url)

from datetime import datetime
from xml.sax.saxutils import escape
import pprint as pp
import jinja2
import pandas as pd

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%b/%Y %H:%M:%S")


df = pd.read_csv('test.csv')
df.fillna("NA", inplace=True)
df_dict = df.to_dict('records')

for item in df_dict:
    value_dict = item
    for key in value_dict.keys():
        if value_dict[key] == 'NA':
            value_dict[key] = "No " + key + " for this request"
        value_dict[key] = escape(value_dict[key])
        # print(value_dict[key])

# pp.pprint(df_dict)
html_header = (
    jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=""))
        .get_template(name="test.html")
        .render(
        df_dict=df_dict,
        title="Confirmation of Payee",
        timestamp=dt_string

    )
)
html_path = f'layout3.html'
html_file = open(html_path, 'w')
html_file.write(html_header)
html_file.close()


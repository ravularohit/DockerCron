from datetime import datetime
def get_html():    
    f = open('index.html', 'w')
      
    # the html code which will go in the file GFG.html
    html_template = """<html>
    <head>
    <title>Title</title>
    </head>
    <body>
    <h2>Welcome To GFG</h2>
      
    <p>updated time</p>
    <p>{0}</p>
    </body>
    </html>
    """.format(datetime.now())
      
    # writing the code into the file
    f.write(html_template)
      
    # close the file
    f.close()


if __name__=="__main__":
    get_html()


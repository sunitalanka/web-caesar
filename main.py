from flask import Flask, request
from ceasar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True
form="""
  <!DOCTYPE html>
  <html>
      <head>
          <style>
                form {{
                   background-color: #eee;
                   padding: 20px;
                   margin: 0 auto;
                   width: 540px;
                   font: 16px sans-serif;
                   border-radius: 10px;
                }}
                  textarea {{
                   margin: 10px 0;
                   width: 540px;
                   height: 120px;
                }}
           </style>
        </head>
      <body>
          <form  method="post">
             <lable for="Rotate by"> Rotate by:</lable>
               <br>
               <input id="Rotate by" type="text" name="rot" value="0"/>
                <br>
                <lable>
                 <textarea  name="text">{0}</textarea>
                 <br>
                <input type="submit"/>
                </lable>
           </form>  
      </body>
    </html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['post'])
def encrypt(): 
      rot_msg = request.form['text']
      rot_num = request.form['rot']
      new_rot = int(rot_num)
      new_txt = list(rot_msg)
      new_st = ''
      n_char = ''
      for char in new_txt:
          n_char = rotate_string(char,new_rot)
          new_st += n_char
      return form.format( new_st )

app.run()    

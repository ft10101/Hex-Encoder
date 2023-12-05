from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if request.method == 'POST':
        user_input = request.form['user_input']
        encrypted_result = encrypt_string(user_input)
        return render_template('result.html', user_input=user_input, encrypted_result=encrypted_result)

def encrypt_string(input_str):
    dic_to_hex = {'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9','K':'A','L':'B','M':'C','N':'D','O':'E','P':'F','Q':'10','R':'11','S':'12','T':'13','U':'14','V':'15','W':'16','X':'17','Y':'18','Z':'19','a':'1A','b':'1B','c':'1C','d':'1D','e':'1E','f':'1F','g':'20','h':'21','i':'22','j':'23','k':'24','l':'25','m':'26','n':'27','o':'28','p':'29','q':'2A','r':'2B','s':'2C','t':'2D','u':'2E','v':'2F','w':'30','x':'31','y':'32','z':'33','1':'34','2':'35','3':'36','4':'37','5':'38','6':'39','7':'3A','8':'3B','9':'3C','!':'3D','@':'3E','#':'3F','$':'40','%':'41','^':'42','&':'43','*':'44','-':'45','_':'46','=':'47','+':'48','`':'49'}
    result = ""
    for char in input_str:
        if char in dic_to_hex:
            result += dic_to_hex[char]
        else:
            result += char
    return result

if __name__ == '__main__':
    app.run(debug=True,port=5001)
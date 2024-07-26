

from flask import Flask,render_template,request
import pickle as pkl
#import pandas as pd
#import numpy as np

# loading the label encoder 
#le=pickle.load(open('label_encoder.pkl','rb'))


#loading Scaler
scalar=pkl.load(open('ms_saved.pkl','rb'))

model=pkl.load(open('saved_mode2.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def main_func():
    return render_template("index.html")

@app.route('/pred_page')
def pred_page():
    return render_template("prediction.html")

@app.route('/predict',methods=['POST'])
def pred_fun():
    if request.method=="POST":
        a = request.form["a"]
        b = request.form["b"]
        c = request.form["c"]
        d = request.form["d"]
        e = request.form["e"]
        f = request.form["f"]
        g = request.form["g"]
        h = request.form["h"]
        i = request.form["i"]
        j = request.form["j"]
        k = request.form["k"]
        l = request.form["l"]
        m = request.form["m"]
        n = request.form["n"]
        o = request.form["o"]
        p = request.form["p"]
        q = request.form["q"]
        r = request.form["r"]

        t =  [[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),float(i),float(j),float(k),float(l),float(m),float(n),float(o),float(p),float(q),float(r)]] 
        x=scalar.transform(t)
        output =model.predict(x)
        index1=['NORMAL FIND','METASTASES','MALIGN LYMPH','FIBROSIS']
        k=index1[output[0]-1]

        if(k=='NORMAL FIND'):
            data="No disease detected!"
        elif(k=='METASTASES'):
            data="Metastasis is a complex biological process by which cells from a primary tumor spread to other parts of the body, forming secondary tumors. This is a critical characteristic of malignant or cancerous tumors and is responsible for the majority of cancer-related deaths.Here are some key points about metastases:Formation of Primary Tumor: Cancer usually begins as a single, abnormal cell that starts to divide uncontrollably. This mass of abnormal cells is known as a primary tumor.Invasion: Cancer cells from the primary tumor can invade nearby tissues and blood vessels. This is facilitated by genetic mutations that allow the cells to ignore normal growth and division signals.Circulation: Cancer cells can enter the bloodstream or lymphatic system, which are the body's transportation networks for blood and lymph fluid. This allows the cells to travel to distant parts of the body.Arrest and Extravasation: Cancer cells can be carried by the bloodstream to other organs or tissues. However, they need to stop (arrest) and exit the bloodstream (extravasation) to form secondary tumors."
        elif(k=='MALIGN LYMPH'):
            data="When people talk about malignancy in the context of the lymphatic system, they often refer to cancer that has spread to the lymph nodes or originated in the lymphatic system. Lymph nodes are small, bean-shaped structures that produce and store cells that help fight infection. If cancer cells break away from a tumor, they can travel through the lymphatic system and form new tumors in other parts of the body.Common cancers that can involve lymph nodes include lymphomas (cancers of the lymphatic system) and metastatic cancers (cancers that have spread from their original site to other parts of the body)."
        else:
            data="Fibrosis is a condition characterized by the formation of excess fibrous connective tissue in an organ or tissue. This fibrous tissue, composed mainly of collagen, replaces normal tissue architecture and can disrupt the normal functioning of the affected organ. Fibrosis is often associated with chronic inflammation and is a common feature in various diseases."
    
    return render_template("result.html",prediction=k,desc=data)

if  __name__ == "__main__" :
    app.run(debug=True)


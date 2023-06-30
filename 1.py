# -*- coding: utf-8 -*-
import os
from flask import *
open('./ry.txt','w',encoding='utf-8').write('')
open('./jlsz.txt','w',encoding='utf-8').write('0')
open('./ml.txt','w',encoding='utf-8').write('')
def runfuwu():
    app = Flask(__name__)
    @app.route('/sc', methods=['POST'])
    def upload_file():
        file1 = request.files.get("file")
        file1.save("file/1.jpg")
        return "yes"
    @app.route('/ml')
    def ml():
        nr = open('./ml.txt','r',encoding='utf-8').read()
        open('./ml.txt', 'w', encoding='utf-8').write('')
        return nr
    @app.route('/dl', methods=['GET'])
    def dl():
        ip = request.args.get("ip")
        nr = open('./ry.txt', 'r', encoding='utf-8').read().split('\n')
        jl = 'yes'
        for i in nr:
            if i.replace(' ','') == '':
                continue
            elif i.split(' ')[1] == ip:
                jl = 'no'
        if jl == 'yes':
            open('./ry.txt', 'a', encoding='utf-8').write(open('./jlsz.txt','r',encoding='utf-8').read()+' '+ip+'\n')
        sz = open('./jlsz.txt','r',encoding='utf-8').read()
        open('./jlsz.txt', 'w', encoding='utf-8').write(str(int(sz)+1))
        return sz
    if __name__=="__main__":
        app.run(host='0.0.0.0',port=int(open('./config/lj.txt','r',encoding='utf-8').read().split(',')[2]))
runfuwu()
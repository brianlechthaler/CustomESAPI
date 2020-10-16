import flask as f
from flask import request
import elasticsearch as es
import elasticsearch_dsl as dsl
from elasticsearch_dsl import Search as search
from datetime import datetime as d
from connect import connection

app = f.Flask(__name__)

@app.route('/ip', methods=['POST'])
def ipaddr():
    find = request.form['keyword']
    findstr = str(find)
    ra = search(using=connection)
    ra = ra.index(es_idx)
    ra = ra.query("match", src_ip__keyword=findstr)
    rb = ra.execute()
    for hit in rb:
        return rb.to_dict()

@app.route('/typesearch', methods=['POST'])
def typesearch():
    find = request.form['keyword']
    findstr = str(find)
    ra = search(using=connection)
    ra = ra.index(es_idx)
    ra = ra.query("match", type__keyword=findstr)
    rb = ra.execute()
    for hit in rb:
        return rb.to_dict()

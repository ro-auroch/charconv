# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:51:00 2018


@author: auroch
@github: github.com/ro-auroch
@License: MIT License
"""

import pandas as pd
import getopt
import sys

import ESTELA.UTILIDADES.herramientas as util


def get_metadata(headers_file):
    df=pd.read_csv(headers_file, delimiter=',', names=None, index_col=None, encoding='1252', low_memory=False)
    dic=df.to_dict(orient='list')
    headers=dic['TX_CAMPO']
    types=dic['TIPO']
    long=len(headers)
    dtype={headers[0]:types[0]}
    for i in range(1,long):
        dtype.update({headers[i]:types[i]})

    def get_headers():
        return headers
    def get_dtypes():
        return dtype

    metadata=[headers,dtype]
    return metadata


def csv2df(file, delimit, headers, index_c, ltype,enc):
    df=pd.read_csv(file, delimiter= delimit, names=headers, index_col=index_c,dtype=ltype,encoding=enc, low_memory=False)
    return df

def convert(df, headers_n, output,delimiter_out,headers,indexes,enc_out):
    df.loc[:,headers_n].to_csv(output,sep=delimiter_out,header=headers,index=indexes,encoding=enc_out)
    #print(df.loc[:5,:])
    print('Done!')
    return

def get_ops():
    try:
        opt,args=getopt.getopt(sys.argv[1:], 'x', ['src=',
                               'output=',
                               'delimiter_src=',
                               'enc_src=',
                               'enc_out=',
                               'delimiter_out',
                               'l_src=',
                               'l_output=',
                               'headers='])
    except getopt.GetoptError as err:
        print(err)
    u_args=[]
    src=None
    l_src=None
    output=None
    l_output=None
    delimiter_src='~'
    enc_src='1252'
    enc_out='utf-8'    
    delimiter_out='~'
    headers=None
    for o, a in opt:
        if o=="--src":
            src=a
        elif o=="--output":
            output=a
        elif o=="--delimiter_src":
            delimiter_src=a
        elif o=="--enc_src":
            enc_src=a
        elif o=="--enc_out":
            enc_out=a
        elif o=="--delimiter_out":
            delimiter_out=a
        elif o=="--l_src":
            l_src=a
        elif o=="--l_output":
            l_output=a
        elif o=="--headers":
            headers=a
        else:
            print("Opción no reconocida")
    u_args.append(src)
    u_args.append(output)
    u_args.append(delimiter_src)
    u_args.append(enc_src)
    u_args.append(enc_out)
    u_args.append(delimiter_out)
    u_args.append(l_src)
    u_args.append(l_output)
    u_args.append(headers)
    return u_args



if __name__=="__main__":
    ops=get_ops()
    src=ops[0]
    output=ops[1]
    delimiter_src=ops[2]
    enc_src=ops[3]
    enc_out=ops[4]
    delimiter_out=ops[5]
    l_src=ops[6]
    l_output=ops[7]
    headers_file=ops[8]

    index_col=None
    headers=False
    index_n=False
    metadata=get_metadata(headers_file)
    headers_n=metadata[0]
    ltype=metadata[1]
    print(headers_n)
    print(ltype)
    error_msg="""
    Error:
        -Para convertir un solo archivo, asigna valor a los parámetros: 'src' y 'output'
        -Para convertit un conjunto de archivos, asigna valor a los parámetros: 'l_src' y 'l_output'

    """
    
    
    if(src != None and output != None):
        if(l_src == None and l_output == None):
            df=csv2df(src,delimiter_src, headers_n, index_col, ltype,enc_src)
            convert(df, headers_n, output, delimiter_out,headers,index_n, enc_out)
        else:
            print(error_msg)
    elif(l_src != None and l_output != None):
        if(src == None and output == None):
            tools=util.herramientas()
            lista=tools.lista_archivos('$csv', l_src)
            l_files=lista[0]
            n_files=lista[1]
            for i in range(0, len(l_files)):
                src_i=l_files[i]            
                output_i=l_output+'UTF8_'+n_files[i]
                df=csv2df(src_i,delimiter_src, headers_n, index_col, ltype,enc_src)
                convert(df, headers_n, output_i, delimiter_out,headers,index_n, enc_out)
        else:
            print(error_msg)
    


        



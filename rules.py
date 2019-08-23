# coding:utf-8

from flask import Flask, jsonify, request
import logging
# 请求方式错误
method_err = {
    "code": 301,
    "msg": "请求方式错误，只支持POST请求"
}
# 参数错误
param_err = {
    "code": 302,
    "msg": "请求参数错误，请检查入参"
}

# 无可借渠道返回信息
channel_false_msg = {"code":"4011","success":False,"subcode":"0","msg":"无可借渠道"}

# 有可借渠道返回信息
channel_success_msg = {"code":"0","success":True,"subcode":"0","msg":"成功","data":{"assetChannel":"YZD","productType":"LARGE","capitalChannel":"JINSHANGXJ","capitalName":"晋商消金","assetProductCapitalCode":"YZD-LARGE-JINSHANGXJ","hold":False}}

# 渠道hold住返回信息
channel_hold_msg = {"code":"0","success":True,"subcode":"0","msg":"成功","data":{"assetChannel":"YZD","productType":"LARGE","capitalChannel":"JINSHANGXJ","capitalName":"晋商消金","assetProductCapitalCode":"YZD-LARGE-JINSHANGXJ","hold":True}}

# 这个是初始化一个服务，__name__代表是咱们写的这个python文件,
# 也就是咱们这个python文件就是一个服务了，然后赋值给app，app就代表这个服务了
server = Flask(__name__)


@server.route('/sevend/financial/channel/route', methods=['POST'])
def channel_route():
    if request.method != 'POST':
        return jsonify(method_err)
    else:
        loan_principal = request.json["loanPrincipal"]
        print(loan_principal)
        print(request.json)
        if loan_principal:
            if loan_principal == 10000000:
                return jsonify(channel_false_msg)
            elif loan_principal == 6000000:
                return jsonify(channel_hold_msg)
            else:
                return jsonify(channel_success_msg)
        else:
            return jsonify(param_err)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=7001, debug=True)

#server.run(port=6688,debug=True,host='0.0.0.0')#启动服务,接口才能访问
# port=6688指定端口为6688
# debug=True设置代码修改后服务自动重启
# host='0.0.0.0'设置同一局域网的可以访问
# server.run() 必须在所有接口定义完后再定义, 否则, server.run()检测不到之后定义的接口, 接口是无法被运行的

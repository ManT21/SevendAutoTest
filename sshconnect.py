# -*- coding:utf-8 -*-

import paramiko

ssh = paramiko.SSHClient()  # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
ssh.connect(hostname='10.40.11.141', port=22, username='admin', password='admin##1')  # 连接服务器
co = "grep 'jsdkfq queryRepayChannel request' /data/logs/loanrepay-rpc/server.log | grep 2904334"
stdin, stdout, stderr = ssh.exec_command(co)  # 执行命令并获取命令结果
# stdin为输入的命令
# stdout为命令返回的结果
# stderr为命令错误时返回的结果
res, err = stdout.read(), stderr.read()
result = res if res else err
resultstr = bytes.decode(result)
print(resultstr)
ssh.close()  # 关闭连接

import hashlib


class SignatureAndVerification(object):
    """MD5签名和验签"""

    @classmethod
    def data_processing(cls, data):
        """
        :param data: 需要签名的数据，字典类型
        :return: 处理后的字符串，格式为：参数名称=参数值，并用&连接
        """
        if "sign" in data:
            del data["sign"]
        # if "sign_type" in data:
        #    del data["sign_type"]
        dataList = []
        for key in sorted(data):
            dataList.append("%s=%s" % (key, data[key]))
        return "&".join(dataList).strip()

    @classmethod
    def md5_sign(cls, data, api_key):
        """
        MD5签名
        :param api_key: MD5签名需要的字符串
        :return: 签名后的字符串sign
        """
        data = data + api_key.strip()
        md5 = hashlib.md5()
        md5.update(data.encode(encoding='UTF-8'))
        return md5.hexdigest()

    @classmethod
    def md5_verify(cls, data, signature):
        """
        md5验签
        :param data: 接收到的数据
        :param signature: 接收到的sign
        :return: 验签结果,布尔值
        """
        if cls.md5_sign(data) == signature:
            return True
        else:
            return False


# data = 'creditType=insuranceJob&customerId=2904342&infoAuditCode=1&infoAuditErrorReason=&manualJudgmentType=2&quota=0&quotaAuditType=1&quotaState=0&realYearIRR=&riskRank=&seqId=534345764&signType=free_sign'
# data = 'creditType=insuranceJob&customerId=2904342&infoAuditCode=1&infoAuditErrorReason=&manualJudgmentType=1&quota=1000000&quotaAuditType=2&quotaState=1&realYearIRR=&riskRank=GROUP_5&seqId=534345764&signType=freeSign'
# data = 'creditType=insuranceJob&customerId=2904342&infoAuditCode=1&manualJudgmentType=1&quota=1000000&quotaAuditType=2&quotaState=1&riskRank=GROUP_5&seqId=534345764&signType=freeSign'
data = {
    "sign": "8ce23e6043c659cc33c084fc69fecd95",
    "infoAuditCode": 1,
    "quotaState": 1,
    "quota": 1000000,
    "seqId": 534345764,
    "infoAuditErrorReason": "",
    "quotaAuditType": 2,
    "customerId": 2904342,
    "signType": "freeSign",
    "manualJudgmentType": 1,
    "riskRank": "GROUP_5",
    "realYearIRR": "",
    "creditType": "insuranceJob"
}
data = SignatureAndVerification.data_processing(data)
print(data)
key = 'w#i*234(14-+21adf~2d2!17'
after = SignatureAndVerification.md5_sign(data, key)
print(after)

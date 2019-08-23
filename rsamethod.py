import rsa
import base64


def rsaEncrypt(str):

    #导入秘钥
    #privateKey 字符串的开头和结尾一定要是 RSA PRIVATE KEY，否则会报错
    privateKey = """
    -----BEGIN RSA PRIVATE KEY-----
    接口文档里获取，或者找开发人员
    -----END RSA PRIVATE KEY-----
    """
    publicKey = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC81szNatpNfepRp5MHXKJ+sMpHLV6mpVZBRYrLKz2HfYs8uzhxI6Wy3GtlYl8Q5PKVR1zCRP5mJj7JrCr5kt2PshO/nAzP4McrN/yqz0YBGH/Xuj6KT2MHA1jLzdOfybPo4gm1046sQgEFqgs9mbJb25VjsklQEgapz2XqPTP+/QIDAQAB
    -----END PUBLIC KEY-----
    """
    message = str #需要加密的参数
    #print('Before encrypted:', message)
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(publicKey.encode())#将公钥由string格式的字符串转化为一个pem格式的对象
    #private_Key = rsa.PrivateKey.load_pkcs1(privateKey.encode()) #将私钥由string格式的字符串转化为一个pem格式的对象
    message = message.encode(encoding='utf-8') #定义参数格式
    cryptedMessage = rsa.encrypt(message, pub_key)# 字符串用公钥加密
    #print('After encrypted:\n',cryptedMessage) # 打印加密后的文件
    key_str_text = base64.b64encode(cryptedMessage)  # base64进行二进制编码
    return key_str_text
    #decryptedmessage = rsa.decrypt(cryptedMessage, private_Key) # 将加密的参数用私钥进行解密
    #decryptedmessage = decryptedmessage.decode(encoding='utf-8') #定义解密后的参数格式
    #print('After decrypted:',decryptedmessage)

class SMSConfig:
    secretId = ""
    secretKey = ""
    SdkAppId = ""
    signName = ""
    templateId = ""
    sendPhone = ["+"]
    TemplateParamSet = []


class EmailConfig:
    smtpserver = ""
    smtpport = 465
    from_mail = ""
    password = ""  # 16位授权码

    my_sender = ''  # 发件人邮箱账号
    my_user = ''  # 收件人邮箱账号，我这边发送给自己



currency_cate = [
            # {"start_time": "08-09 00:03:00", 'buy_in_price': "0.017599", "currency": "btc_usdt"},
        ]


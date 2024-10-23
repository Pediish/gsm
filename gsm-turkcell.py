import requests

res = requests.request(
    method="post",
    url="http://192.168.0.1:80/goform/goform_process",
    headers={
        "accept-language":"en-US,en;q=0.9,fa;q=0.8",
        # content-type: "application/x-www-form-urlencoded",
        "cookie":"mLangage=tr; lucknum=44197",
        "host":"192.168.0.1:80",
        "origin":"http://192.168.0.1:80",
        "referer":"192.168.0.1:80/adm/home_wan.asp",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    },
    data={
        "goformId":"NET_CONNECT",
        "lucknum_NET_CONNECT":"44197",
        "dial_mode":"auto_dial",
        "action":"connect",
        "wan_conn_which_page":"wan_operation"
    }
)
print(res.content,res.status_code)













# 使用方法
## 使用py文件
运行<br>
```
Python wol.py
```
首次运行完成后会生成 `config.ini` <br>

将[MAC]与[IP]替换为待开机电脑的MAC地址与IPV6地址或链接<br>

填写完成后再次运行 Python wol.py 即可开机

或者你可以直接使用下面的`config.ini`

    [WOL]
    mac_address = [MAC]
    ipv6_address = [IP]

## 使用exe(不需要Python环境)
下载[wol.exe](https://github.com/3281221832/IPV6WOL/releases)<br>

后续方法同上

# PS:此脚本只支持IPV6地址或链接,不支持IPV4地址

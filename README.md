# 北大数院新闻推送

本项目抓取北大数院门户的最新信息，并通过 Bark (iOS 客户端) 推送到手机上。实现方式为 Python 中的 `requests` 和正则表达式。

如您需要使用此脚本，请确保正确配置 `home_path`、`bark_key`、`pku_math.pkl`。

你可以使用 `crontab` 设置定时运行，例如可以使用以下命令使得每 10 分钟运行一次该脚本。

```bash
*/10 * * * * /usr/bin/python /root/math/pku_math.py >> /root/math/log.out
```
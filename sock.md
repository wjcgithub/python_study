# 清除python3.4不使用的端口

```powershell
sudo netstat -tuanlp | grep python3.4 | awk '{print $7}' | cut -d / -f 1 | xargs sudo kill -9
```
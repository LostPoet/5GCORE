# 5GCORE
删去了源代码中UPF的网桥配置部分, 对UDM数据库连接部分做了微调

## 运行方法

1. 注意5GCORE文件夹须放在用户根目录 `~/` 下

2. 环境: python 3.6+, 用virtualenv创建虚拟环境后执行 `pip install -r requirements.txt` 安装所有依赖

3. 配置数据库: mysql5.7, 修改下面两个文件中的连接配置, 然后执行users.py的 `create()` 及 `add()` 函数建表并写入一行数据, 之后可以用 `query()` 测试是否生效

   ```
   ~/5GCORE/UDM/Nudm_UEAuthentication/v1/users.py
   ~/5GCORE/UDM/Nudm_UEAuthentication/v1/api/UE_Auth.py
   ```

4. 开两个终端, 第一个运行核心网代码, 第二个当做UE, 执行完成后应当能看到完整的log信息

```shell
# 第一个终端执行
./run5gCore
# 第二个执行
cd ~/5GCORE/UE
python AN2.py
```

5. 如果使用Windows, 需要自己写.bat脚本, 可参考fork版代码的.bat文件
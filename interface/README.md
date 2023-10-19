# 通信接口程序文件  
程序文件分为两部分：  
  
    environment：存放B0-based Remote API环境配置的14个标准文件。  
    
    interfacein.py：直接定义通信接口函数并调用的文件。
    interface_class.py：单独定义通信接口函数类的文件。
    interface.py：用于调用interface_class.py文件内封装的函数。

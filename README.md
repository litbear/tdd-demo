# 读书笔记

## 搭建环境

- 在windows中为mingw添加python命令

    ln -s /c/Python34/python.exe /bin/python3.exe

- 为新版火狐浏览器添加驱动[geckodriver](https://github.com/mozilla/geckodriver)

- 初始化工作目录

- 初始化git版本管理

- 初始化virtualenv

- 进入virtualenv，安装selenium开发版`pip install selenium==ver-num`
- 安装django

## 名词

功能测试 = 验收测试 = 端到端测试 这几个属于一般属于黑箱测试

- test fixture 测试夹具

测试夹具，代表执行一个或多个测试时的准备工作，以及执行完毕后必要的清理工作。这些工作包括：创建临时或代理数据库，文件夹，或启动测试需要的进程。

- test case 测试用例

测试用例，是测试中的个体单元。用于检查程序对一组特定输入的响应。` unittest`模块提供了一个基类`TestCase`可以用于创建新的测试用例。

- test suite 测试套件

测试套件是一系列的测试用例或测试套件的集合。他们用于综合测试，应当在一起执行。

- test runner 测试运行器

测试运行器，是一个组织测试运行并向用户提供运行结果的组件。运行器可以使用图形界面，文本界面或返回指定值以表明测试的运行结果。



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

## 一些问题的解决方法

- Selenium3.0.0b3无法使用get_attribute的一个坑 [解决方法](http://stackoverflow.com/questions/39527858/how-can-i-disable-web-driver-exceptions-when-using-the-mozilla-marionette-web-dr)

- 另一个坑，Django 1.10中会为同一HttpRequest多次渲染时分配不同的csrf_token

因此`render_to_string`方法和`response.content.decode()`传入同一HttpRequest对象时渲染的静态页必然不同。

详见：[Django 中的 csrf_token 与单元测试](http://www.cnblogs.com/panzeyan/p/5819373.html)，以及[How can I disable Web Driver Exceptions when using the Mozilla Marionette web driver with Selenium](http://stackoverflow.com/questions/39527858/how-can-i-disable-web-driver-exceptions-when-using-the-mozilla-marionette-web-dr) 以及 [Django 1.10 release notes](https://docs.djangoproject.com/en/1.10/releases/1.10/) To protect against BREACH attacks, the CSRF protection mechanism now changes the form token value on every request (while keeping an invariant secret which can be used to validate the different tokens).

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



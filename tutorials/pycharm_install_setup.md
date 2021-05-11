# PyCharm Installation and Setup

We'll be using the PyCharm IDE from JetBrains.

An IDE or **I**ntegrated **D**evelopment **E**nvironment gives you the ability to write, run, test, and lint code all in one place. The PyCharm interface looks like this:

![PyCharm IDE interface](/images/pycharm_1.png)

This tutorial will walk you through installation and setup of PyCharm.

## Installation

Any user with a `.edu` email address can get PyCharm for free by [signing up for an educational account](https://www.jetbrains.com/student/).

Once you have signed up for an account, you will receive an email activation to confirm your email. When you click on the link you will be able to download PyCharm.

![JetBrains Student Installation Page](/images/pycharm_2.png)

Alternately, you can download PyCharm through this [direct link](https://www.jetbrains.com/pycharm/download/).

![PyCharm Installation](/images/pycharm_3.png)

The installation process differs slightly between Mac and Windows but you can select the default settings in both cases.

_For Mac, you will need to choose M1 or Intel processor._

## Initialization
Once the installation process is finished, open up the PyCharm application. This
will open up an activation screen. You can activate PyCharm by entering the email
and password that you used before to sign up for a Jetbrains account.

![PyCharm activation screen](../images/pycharm_activation_1.png)

Next, you will get to a setup menu.

In the first window, select "Do not import settings". We'll import settings at a
later stage.

![PyCharm initialization](../images/pycharm_init_1.png)

Once the setup is finished, the screen below will be displayed. Select "Open"
to select the existing `lssdh-python-git` directory.

![PyCharm add directory](/images/pycharm_init_6.png)

Select the path to your `lssdh-python-git` directory.

This will bring up the main PyCharm window with the loaded `lssdh-python-git` directory
on the left.

## Configuration

Ensure that you use a Python 3 interpreter. 

You'll next run the following to set up the project:

```python
python setup.py develop
```

You're now done with the PyCharm installation and configuration.

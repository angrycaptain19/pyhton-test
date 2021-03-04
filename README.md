# Prerequisites

**Python**  3.6 or major

Selenium webdrivers in the path:
Chrome: "C:\\selenium\\chromedriver.exe"
Firefox: "C:\\selenium\\geckodriver.exe"
Edge: "C:\\selenium\\msedgedriver.exe"

Or change them in the conftest.py file

# Installation

Clone the repo

```sh
git clone https://github.com/ruvaz/pyhton-test.git
```

Open downloaded files folder

```sh
cd pyhton-test
```

Install Virtualenv

```sh
pip install virtualenv
```

Create new virtualenv

```sh
virtualenv test
```

Start new virtualenv
```
.\test\Scripts\activate
``` 

Install python packages

```sh
pip install pytest selenium
```

# Run Test

Chrome is the default browser just need to run the command:

```sh
py.test 
```

For Firefox

```sh
py.test --browser_name firefox 
```

For Edge

```sh
py.test --browser_name edge 
```

Author
- Rubén Vázquez
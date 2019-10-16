The fast ping
-

The fast ping to hosts via multi threads.

    !!! This work only for linux hosts !!! 

# Install

## Form git repository

pipenv installation
```bash
pipenv install -e git+https://github.com/yuryrunx/fping.git#egg=fping
```

or classic pip
```bash
pip install git+https://github.com/yuryrunx/fping.git
```

## From sourse

```bash
git clone {url_to_gitrepo} {path_to_folder}
pip install {path_to_folder}/dist/fping-1.0.tar.gz
```

## Example
```python
import fping 
ping = fping.FPing()
>>> result = ping.run(['127.0.0.1', '127.0.0.2', '172.16.100.1'])
>>> print(result)
(['127.0.0.2', '127.0.0.1'], ['172.16.100.1'])
>>> print(result[0])    # Ok
['127.0.0.2', '127.0.0.1']
>>> print(result[1])    # Fail
['172.16.100.1']
```


# How to use

```python
import fping

hosts = ['127.0.0.1', '127.0.0.2', '127.0.0.3'] # Your host's list
ping = fping.FPing()
result = ping.run(hosts)
print('Online: {}, Offline: {}'.format(result[0], result[1]))
```

# Tests's Run

```bash
cd fping/tests
python test_main.py -v
```
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
from fping import FPing

ping = FPing()
result = ping.run(['127.0.0.1', '127.0.0.2', '172.16.100.1'])
print(result[0]) 
# ['127.0.0.2', '127.0.0.1']  # Ok

print(result[1]) 
# ['172.16.100.1']            # Fail

```


# How to use

```python
from fping import FPing

hosts = ['127.0.0.1', '127.0.0.2', '127.0.0.3'] # Your host's list
ping = FPing()
result = ping.run(hosts)
print('Online: {}, Offline: {}'.format(result[0], result[1]))
```

# Tests's Run

```bash
cd fping/tests
python test_main.py -v
```
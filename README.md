# install latest python in ubuntu from tar file 

1. download the tar file from python official website. For example download the `Python-3.14.3.tar.xz` file.
2. extract the tar file
```
atulkrishnathakur@atul-pc:~/Downloads$ tar -xf Python-3.14.3.tar.xz
```
3. update the apt
```
atulkrishnathakur@atul-pc:~$ sudo apt update
```
4. Install the build dependencies
```
atulkrishnathakur@atul-pc:~$ sudo apt install -y build-essential \
    libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev \
    libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev \
    libbz2-dev libexpat1-dev liblzma-dev tk-dev uuid-dev

```
5. go in extracted tar file
```
atulkrishnathakur@atul-pc:~/Downloads$ cd Python-3.14.3
```
6. configure the build
```
atulkrishnathakur@atul-pc:~/Downloads/Python-3.14.3$ ./configure --enable-optimizations --prefix=/usr/local

```
7. compile
```
atulkrishnathakur@atul-pc:~/Downloads/Python-3.14.3$ make -j$(nproc)
```

7. Install 
```
atulkrishnathakur@atul-pc:~/Downloads/Python-3.14.3$ sudo make altinstall
```
Note: Use altinstall instead of install to avoid overwriting the default python3 binary that Ubuntu uses internally.

8. verify python installation
```
atulkrishnathakur@atul-pc:~/Downloads/Python-3.14.3$ python3.14 --version
```
9. check pip version
```
atulkrishnathakur@atul-pc:~/Downloads/Python-3.14.3$ python3.14 -m pip --version
pip 25.3 from /usr/local/lib/python3.14/site-packages/pip (python 3.14)

```

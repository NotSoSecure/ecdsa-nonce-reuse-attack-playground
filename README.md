# ECDSA Nonce Reuse Attack - Playground

### Challenge is to extract the content of /etc/passwd

### Build and run docker
```
sudo docker build -t ecdsa-nonce-reuse-playground . 
sudo docker run -it -p 5000:5000 ecdsa-nonce-reuse-playground
```

### Access 
```
http://localhost:5000
```

### To run exploit - install pre-requisite

```
pip3 install -r requirement.txt
```

### Run exploit - to generate signature for /etc/paaswd

```
python3 exploit.py
```


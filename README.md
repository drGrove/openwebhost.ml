# openwebhost.ml

OpenWebHost primary server

This repository is set up to secretlessly set up an exact clone of a webserver
used to register users for servers configured using [TODO]. This server also
(functions|will function) as a blog to post status updates.

To set up this server on a personal setup, the prefered server setup would be
to run a CoreOS server with mysql and OWH linked, described in [this](#CoreOS)
section. A Debian server (at least one) also should be configured in an etcd
list running the [Debian](#Debian) servers.

### CoreOS

```sh
git clone https://github.com/OpenWebHost/openwebhost.ml
cd openwebhost.ml
sudo systemctl enable openwebhost.service
sudo systemctl daemon-reload
sudo systemctl start openwebhost
sudo systemctl start mysql
```

### Debian

[TODO]

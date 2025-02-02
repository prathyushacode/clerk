## Prerequisites for Local Development

This repository should work on Linux, Mac and maybe WSL. It is unlikely to work with Windows machines.

You will need:

- `docker` ([install](https://docs.docker.com/install/#supported-platforms))
- `docker-compose` ([install](https://docs.docker.com/compose/install/))
- `transcrypt` ([install](https://github.com/elasticdog/transcrypt#usage))
- `inv` ([install](https://www.pyinvoke.org/installing.html))

## Getting Started

Envars are stored in .env and encrypted using transcrypt. You can see encryoted files with `transcrypt --list`.

To intialise the repository on cloning run

```bash
transcrypt -c aes-256-cbc -p $TRANSCRYPT_PASSWORD
```

The values of these secrets will be provided to you if you need them. They should be available in the Tech team Bitwarden account.

Next, you want to build the Docker environment that we'll be using:

```bash
inv build
```

Now you can set up your database with this reset command:

```bash
inv reset
```

Finallly you can exit the container shell and bring up the webserver:

```bash
inv dev
```

Now you should be able to visit [`http://localhost:8000/admin`](http://localhost:8000/admin) and see the Clerk site.

You can view other commands with

```bash
inv -l
```

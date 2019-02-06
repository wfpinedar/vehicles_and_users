# This project provide simple docker configuration for make easy django project

## For user this clone repository and them run:

### Fist install dependencies for use docker:

```bash
sudo pacman -S docker docker-compose
```
Add user to docker group, first crate docker group:

```bash
sudo groupadd docker
```
Now add your user to the docker group.

```bash
sudo usermod -aG docker $USER
```
Finally retart session and run docker

```bash
systemctl start docker
```
Now create app with the next command
```bash
sh begin_django_project.sh -n <app_name>
```
before run replace in __settings.py__ this code:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

for this one:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
and begin with:

```bash
sh run.sh
```

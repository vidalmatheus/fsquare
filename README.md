# F-square template with Vue.js and Django


```
         ______      _____
        |  ____|    / ____|
        | |__ _____| (___   __ _ _   _  __ _ _ __ ___
        |  __|______\___ \ / _` | | | |/ _` | '__/ _ \
        | |         ____) | (_| | |_| | (_| | | |  __/
        |_|        |_____/ \__, |\__,_|\__,_|_|  \___|
                              | |
                              |_|

                Configure your installation

? Project name: myProject
? Python 3.10.0 (Y/n): n
? Node.js 16 and NVM (Y/n): n
? Vue.js (Y/n): n
? Docker (Y/n): n
? Docker Compose (Y/n): n
? Have a f-square instance in ~/projects/ (y/N):

Are you sure? (Y/n):
```

# Download and execute our setup shell script
```bash
wget https://raw.githubusercontent.com/vidalmatheus/fsquare/master/template/setup.sh
bash setup.sh # Shell script for installation of a F-Square app.
```
# Or you can do yourself the following steps:

# 0. Define these environment variables
```bash
export PYTHON_VERSION=3.10.0
export PYTHON_MAJOR=3
export NODE_VERSION=16
export COMPOSER_VERSION=1.29.2  # ver https://github.com/docker/compose/releases
```

# 1. Compile & install Python 3.10/pip 3.10
```bash

sudo apt update
sudo apt upgrade
sudo apt install curl build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

curl -O https://raw.githubusercontent.com/vidalmatheus/fsquare-install/main/fsquare.sh
tar -xvzf Python-${PYTHON_VERSION}.tgz
cd Python-${PYTHON_VERSION}

./configure --enable-optimizations

sudo make install -j4


# Set Python3.10 as python
# sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1

# Set Pip3.10 as pip
# sudo update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.10 1

python3.10 --version
pip3.10 --version


# Clear python installation files
cd
sudo rm -rf Python-${PYTHON_VERSION}.tar.xz
sudo rm -rf Python-${PYTHON_VERSION}


# Clear python installation files
cd
sudo rm -rf Python-${PYTHON_VERSION}.tar.xz
sudo rm -rf Python-${PYTHON_VERSION}
```

# 2. Install nvm
```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

nvm --version

nvm install 16
node --version
```

# 3. Install vue, vue/cli and vue/cli-init
```bash
nvm use 16
npm install vue
npm install -g @vue/cli
npm install -g @vue/cli-init
```

# 4. Install docker
```bash
sudo apt-get update
sudo apt-get install \
ca-certificates \
curl \
gnupg \
lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt-get install docker-ce

sudo docker run hello-world

sudo usermod -aG docker $USER
```


# 5. Install docker-compose
```bash
sudo curl -L https://github.com/docker/compose/releases/download/$COMPOSER_VERSION/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version
```


# 6. Instanciate Vue CLI F-Square template
```bash
# Create projects directory
cd
if ! [ -d "projects" ]; then
    mkdir projects
fi
cd ~/projects

vue init vidalmatheus/fsquare $project_name
```

# 7. Create alias for the project
```bash
echo "alias ${project_name}='cd ~/projects/${project_name};
        source ~/projects/.virtualenv/${project_name}/bin/activate;
        nvm use 16;
        source dev.sh'

export DB_NAME=${project_name}
export DB_USER=${project_name}
export DB_PASSWORD=${project_name}
export DB_HOST=localhost
export DB_PORT=5432
export CACHALOT_ENABLED=1" | sudo tee -a ~/.bashrc
```

# 8. Configuring hosts
```bash
echo "
127.0.0.1       metabase
127.0.0.1       mock" | sudo tee -a /etc/hosts
```

# 8. Create a virtualenv for the project
```bash
pip3.10 install virtualenv
cd projects
mkdir .virtualenv
python3.10 -m virtualenv .virtualenv/$project_name
. ~/projects/.virtualenv/$project_name/bin/activate
cd $project_name
```

# 9. Install python modules
```bash
pip install -r requirements.txt
```

# 10. Install node modules
```bash
cd frontend
npm i
cd ..
```

# 11. Check virtualenv
```bash
python --version
pip --version
```

## You are good to go!
### You can use <project_name> anywhere to go to your project
### You need to logoff and login for running docker without sudo, if you have installed it

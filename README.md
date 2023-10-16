
<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [SETUP-SERVER] <<<<<<<<<<<<<<<<<<<<<<<<< -->
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository -y ppa:certbot/certbot

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce

sudo apt update -y
sudo apt upgrade -y
sudo apt-get install -y curl \
 vim \
 ffmpeg \
 htop \
 nmap \
 iptraf \
 tree \
 gnupg \
 curl \
 virtualenv \
 curl \
 graphicsmagick-imagemagick-compat \
 gunicorn \
 git \
 python3.8 \
 python3.8-venv \
 python3.8-dev \
 python3-pip \
 ipython3 \
 certbot \
 python3-certbot-nginx \
 zip \
 ca-certificates \
 curl \
 gnupg \
 lsb-release \
 docker-ce \
 docker-ce-cli \
 containerd.io \
 docker-compose-plugin 
sudo apt install docker-compose

<!-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<< -->

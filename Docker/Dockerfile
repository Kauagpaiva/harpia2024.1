### crie um dockerfile que descreva uma imagem com o ubuntu 20.04 e que instale o tmux e o htop
FROM ubuntu:20.04

RUN apt update && apt install -y tmux htop

RUN echo "set -g mouse on" >> /root/.tmux.config
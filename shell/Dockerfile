FROM node:latest
WORKDIR /install/
COPY sources.list /etc/apt/sources.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32 && \
apt-get update && \
apt-get install -y git && \
npm install -g grunt-cli && \
git clone https://github.com/gchq/CyberChef && \
cd CyberChef && \
npm install
EXPOSE 8080/tcp
WORKDIR /install/CyberChef
ENTRYPOINT ["grunt"]
CMD ["dev"]
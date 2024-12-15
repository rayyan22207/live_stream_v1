FROM debian:bookworm

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    wget \
    libpcre3-dev \
    zlib1g-dev \
    libssl-dev

# Download and build Nginx with the RTMP module
RUN wget http://nginx.org/download/nginx-1.22.1.tar.gz && \
    wget https://github.com/arut/nginx-rtmp-module/archive/master.zip && \
    tar -zxvf nginx-1.22.1.tar.gz && \
    unzip master.zip && \
    cd nginx-1.22.1 && \
    ./configure --add-module=../nginx-rtmp-module-master --with-http_ssl_module && \
    make && make install

# Copy the custom nginx.conf
COPY nginx.conf /usr/local/nginx/conf/nginx.conf

# Expose necessary ports
EXPOSE 1935 80

# Run Nginx
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]

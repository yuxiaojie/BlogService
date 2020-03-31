FROM python:3.8

COPY requirements.txt /home/app/requirements.txt
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r /home/app/requirements.txt

COPY ./entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

RUN addgroup www && adduser --system www && adduser www www
WORKDIR /home/www
COPY ./ /home/www

ENV LOG_DIR /var/log/tissue
RUN mkdir -p "$LOG_DIR" && chown -R www:www "$LOG_DIR"
VOLUME /var/log/tissue
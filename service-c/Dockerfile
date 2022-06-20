FROM python
WORKDIR /usr/src/app
COPY . .
RUN pip3 install flask
RUN pip3 install requests
CMD ["service-c.py"]
ENTRYPOINT ["python3"]
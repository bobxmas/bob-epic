FROM python
WORKDIR /usr/src/app
COPY . .
RUN pip3 install flask
RUN pip3 install requests
CMD ["service-b-v1.py"]
ENTRYPOINT ["python3"]
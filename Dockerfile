FROM python:3.12

WORKDIR /usr/src/app

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY pip_file.txt ./
RUN pip install --no-cache-dir -r pip_file.txt

COPY . .

CMD ["/bin/bash", "-c", "python Bot_memorizer.py"]
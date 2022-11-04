FROM --platform linux/amd64 python:3.8

WORKDIR /OSRS_Item_Investment_Project

COPY build/frontend/app/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN yum install python3-tkinter -y

COPY . .

CMD [ "python3", "src/frontend/app/app.py"]




FROM python:3.8-slim-buster

WORKDIR /OSRS_Item_Investment_Project

COPY build/backend/transform/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "src/backend/transform/analysis/analysis.py"]




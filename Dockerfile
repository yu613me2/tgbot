FROM python:3.13-slim
ENV TOKEN='7471125756:AAEHw_ZVFA1_8-8i2P15jYKaUTT_t-LP7Ow'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python","bot.py"]
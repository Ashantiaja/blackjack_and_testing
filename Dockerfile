FROM python:3

WORKDIR $HOME/blackjack_and_testing

COPY . .

RUN pip install coverage
RUN pip install pyinstaller

CMD ["python3", "source_files/ui.py"]
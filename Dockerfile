# Use a imagem oficial do Python 3.9
FROM python:3.10

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o container
COPY requirements.txt /app/

# Atualize o pip antes de instalar as dependências
RUN pip install --upgrade pip

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o diretório de trabalho
COPY . /app/

# Exponha a porta 8000
EXPOSE 8000

# Defina o comando de inicialização, rodando as migrações antes de iniciar o servidor Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

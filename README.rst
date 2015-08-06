=======================
Site Aerofácil (SAC/PR)
=======================

Implementação Plone do website "Aerofácil, seu guia para viajar de avião". Um projeto da Secretaria de Aviação Civil da Presidência da República, com código-fonte disponível https://github.com/Clickweb/sac.aerofacil/.

*Plone implementation of Aerofácil website, brazilian government's official guide to air travelling. A project for Secretaria de Aviação Civil (Presidency of Republic), with open source available at https://github.com/Clickweb/sac.aerofacil/.*


Instruções para instalação / *Installation instructions*
========================================================

**1) Instale as seguintes dependências de sistema:**

*1) Install the following system dependencies:*

  $ sudo apt-get install build-essential autoconf automake autotools-dev build-essential bzip2 curl git html2text libbz2-1.0 libfreetype6-dev libgif-dev libjpeg8 libjpeg8-dev libmemcache-dev libncurses5-dev libpcre3-dev libpng12-dev libreadline5-dev libsasl2-dev libssl-dev libxml2-dev libxslt1.1 libxslt1-dev lynx memcached ntpdate pdftohtml pidentd pkg-config poppler-utils ppthtml python-celementree python-cjson python-dev python-imaging python-lxml python-setuptools sudo unzip wget wv zlib1g-dev zlib-bin zlibcvim libexpat1-dev libdb4.8-dev libncurses5-dev libreadline6-dev openssl-dev libghc6-zlib-dev liblcms-utils

**2) Adicione o usuário aerofacil:**

*2) Add aerofacil user:*

  $ sudo adduser aerofacil
  
  $ cd /home/aerofacil

**3) Continue a instalação com o usuário aerofacil:**

*3) Proceed installation with aerofacil user:*

  $ su - aerofacil

**4) Clone o repositório do pacote `buildout.python`, pois não será usado o Python padrão do sistema:**

*4) Clone `buildout.python` package repository since we will not use default system Python:*

  $ git clone https://github.com/collective/buildout.python.git python
  
  $ cd python
  
  $ python bootstrap.py
  
  $ ./bin/buildout -Nv

**5) Após a configuração do Python, é necessário criar o virtualenv com o Python versão 2.7:**

*5) After Python is configured it is necesssary to create a virtualenv with Python version 2.7:*

  $ ./python/bin/virtualenv-2.7 --no-site-packages env27

  $ source env27/bin/active

**6) Com o ambiente virtual preparado, clone o repositório do projeto, inicialize-o e execute seu buildout:**

*6) With the virtualenv set, clone project's repository, bootstrap it and run its buildout:*

  (env27) $ git clone https://github.com/Clickweb/sac.aerofacil sac.aerofacil

  (env27) $ cd sac.aerofacil
  
  (env27) $ python bootstrap.py
  
  (env27) $ ./bin/buildout -Nv
  
O buildout irá montar todo o ambiente com todos os pacotes necessários para o funcionamento do site.

*Buildout will configure all your environment, with all needed packages for site functioning.*

Caso ocorra um erro ao executar o bootstrap.py, realize o seguinte procedimento:

*In case there's an error whhen running bootstrap.py, use the following procedure:*

  (env27) $ pip install -U setuptools

**7) Para subir o ambiente:**

*7) Run the application server:*

  $ ./bin/instance start

**8) Após configurar o ambiente do buildout, descompacte o arquivo `aerofacil_09_05_2014.tar.bz2 <http://162.209.60.226/aerofacil_09_05_2014.tar.bz2>`_ dentro de /home/aerofacil/sac.aerofacil/var**

*8) After configuring buildout's environment, extract `aerofacil_09_05_2014.tar.bz2 <http://162.209.60.226/aerofacil_09_05_2014.tar.bz2>`_ into /home/aerofacil/sac.aerofacil/var*

  $ rm -rf ./var/${file,blob}storage

  $ curl http://162.209.60.226/aerofacil_09_05_2014.tar.bz2 | tar jx -C ./var/

**9) Após descompactar, reinicie o ambiente:**

*9) After extracting, restart the server:*

  $ ./bin/instance restart

**10) Acesse o site em http://localhost:8080/aerofacil**

*10) Access the site at http://localhost:8080/aerofacil*

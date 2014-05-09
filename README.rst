=======================
Site Aerofácil (SAC/PR)
=======================

Implementação Plone do website "Aerofácil, seu guia para viajar de avião". Um projeto da Secretaria de Aviação Civil da Presidência da República, com código-fonte disponível https://github.com/Clickweb/sac.aerofacil/.


Instruções para instalação
==========================

1) Instale as seguintes dependências de sistema:

  $ sudo apt-get install build-essential autoconf automake autotools-dev build-essential bzip2 curl git html2text libbz2-1.0 libfreetype6-dev libgif-dev libjpeg8 libjpeg8-dev libmemcache-dev libncurses5-dev libpcre3-dev libpng12-dev libreadline5-dev libsasl2-dev libssl-dev libxml2-dev libxslt1.1 libxslt1-dev lynx memcached ntpdate pdftohtml pidentd pkg-config poppler-utils ppthtml python-celementree python-cjson python-dev python-imaging python-lxml python-setuptools sudo unzip wget wv zlib1g-dev zlib-bin zlibcvim libexpat1-dev libdb4.8-dev libncurses5-dev libreadline6-dev openssl-dev libghc6-zlib-dev liblcms-utils

2) Adicione o usuário aerofacil:

  $ sudo adduser aerofacil
  
  $ cd /home/aerofacil

3) Continue a instalação com o usuário aerofacil:

  $ su - aerofacil

4) Clone o repositório do pacote `buildout.python`, pois não será usado o Python padrão do sistema:

  $ git clone https://github.com/collective/buildout.python.git python
  
  $ cd python
  
  $ python bootstrap.py
  
  $ ./bin/buildout -Nv

5) Após a configuração do Python, é necessário criar o virtualenv com o Python versão 2.7:

  $ ./python/bin/virtualenv-2.7 --no-site-packages env27

  $ source env27/bin/active

6) Com o ambiente virtual preparado, clone o repositório do projeto, inicialize-o e execute seu buildout:

  (env27) $ git clone https://github.com/Clickweb/sac.aerofacil sac.aerofacil

  (env27) $ cd sac.aerofacil
  
  (env27) $ python bootstrap.py
  
  (env27) $ ./bin/buildout -Nv
  
O buildout irá montar todo o ambiente com todos os pacotes necessários para o funcionamento do site.

Caso ocorra um erro ao executar o bootstrap.py, realize o seguinte procedimento:

  (env27) $ pip install -U setuptools

7) Para subir o ambiente:

  $ ./bin/instance start

8) Após configurar o ambiente do buildout, descompacte o arquivo `aerofacil_09_05_2014.tar.bz2 <http://162.209.60.226/aerofacil_09_05_2014.tar.bz2>`_ dentro de /home/aerofacil/sac.aerofacil/var

  $ rm -rf ./var/${file,blob}storage

  $ curl http://162.209.60.226/aerofacil_09_05_2014.tar.bz2 | tar jx -C ./var/

9) Após descompactar, reinicie o ambiente:

  $ ./bin/instance restart

10) Acesse o site em http://localhost:8080/aerofacil

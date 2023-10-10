# @title Первая страница
from posixpath import join
import random
from PIL import Image
itr = 1
wModel =  1052
hModel = 300
wName = 470
hName = 80
wTitle = 266
hTitle = 290




for i in range(2):
  print(i+1)
  int(i+1)
  if (i+1 == 1):#КЕССОН БИОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/КЕССОН БИО-С.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/kessonbios.png'
    septicSavePath = 'kessonbioshead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
          back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
          septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
          septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTitle1kes/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
            suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1


  if (i+1 == 1):#АКВАЛОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК АКВАЛОС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicaqualos.png'
    septicSavePath = 'aqualoshead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 2):#АЛЬТА БИО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК АЛЬТА БИО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicaltabio.png'
    septicSavePath = 'altabiohead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 3):#АЛЬФА ЛОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК АЛЬФА ЛОС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicalphalos.png'
    septicSavePath = 'alphaloshead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 4):#АСТРА
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК АСТРА.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicastra.png'
    septicSavePath = 'astrahead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 1):#АЭРОБОКС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК АЭРОБОКС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicaerbox.png'
    septicSavePath = 'aeroboxhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 6):#БИО-С КОМФОРТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК БИО-С КОМФОРТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicbioscomfort.png'
    septicSavePath = 'bioscomforthead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 7):#БИОДЕВАЙС ЭКО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК БИОДЕВАЙС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicbiodeviceeco.png'
    septicSavePath = 'biodeviceecohead'
    hModel = 400
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 8):#БИОДЕКА
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК БИОДЕКА.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicbiodeka.png'
    septicSavePath = 'biodekahead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 9):#БИОПУРИТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК БИОПУРИТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicboipurit.png'
    septicSavePath = 'biopurit'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 10):#ВОЛГАРЬ ГАРДА
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ВОЛГАРЬ ГАРДА.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicvolgargarda.png'
    septicSavePath = 'volgargarda'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 11):#ВОЛГАРЬ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ВОЛГАРЬ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicvolgar.png'
    septicSavePath = 'volgarhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 12):#ГРИНЛОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ГРИНЛОС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicgreenlos.png'
    septicSavePath = 'greenloshead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 1):#ДИАМАНТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ДИАМАНТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicdiamant.png'
    septicSavePath = 'diamanthead'
    hModel = 800
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 2):#ДОЧИСТА
    for j in range(7):
      septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ДОЧИСТА.png'
      septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicdochosta.png'
      septicSavePath = 'dochostahead'
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 15):#ЕВРОБИОН РАУНД
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЕВРОБИОН РАУНД.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicevrobion.png'
    septicSavePath = 'evrobionraundhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 16):#ЕВРОЛОС БИО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЕВРОЛОС БИО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicevrolosbio.png'
    septicSavePath = 'evrolosbiohead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 17):#ЕВРОЛОС ПРО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЕВРОЛОС ПРО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicevrolospro.png'
    septicSavePath = 'evrolosprohead'
    hModel = 600
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 18):#ЕВРОЛОС ЭКО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЕВРОЛОС ЭКО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicevroloseco.png'
    septicSavePath = 'evrolosecohead'
    hModel = 650
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 19):#ЕВРОТАНК
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЕВРОТАНК.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicevrotank.png'
    septicSavePath = 'evrotankhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 20):#ЗАУБЕР
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЗАУБЕР.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septiczauber.png'
    septicSavePath = 'sauberhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 21):#ИТАЛ АНТЛЕЙ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ИТАЛ АНТЕЙ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicitalantley.png'
    septicSavePath = 'italantleyhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 22):#КИТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК КИТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septickit.png'
    septicSavePath = 'kithead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 23):#КРИСТАЛЛ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК КРИСТАЛЛ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septickristall.png'
    septicSavePath = 'kristallhead'
    hModel = 570
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 24):#МАЛАХИТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК МАЛАХИТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicmalahit.png'
    septicSavePath = 'malahithead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 25):#ОНИКС БИОЛОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ОНИКС БИОЛОС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septiconix.png'
    septicSavePath = 'onixbioloshead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 26):#ПЕГАС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ПЕГАС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicpegas.png'
    septicSavePath = 'pegashead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 27):#ПРО БИО
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ПРО БИО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicprobio.png'
    septicSavePath = 'probiohead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 28):#РУСАНИТ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК РУСАНИТ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicrusanit.png'
    septicSavePath = 'rusanithead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 29):#РУСЛОС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК РУСЛОС БИО.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicruslosbio.png'
    septicSavePath = 'ruslosbiohead'
    hModel = 550
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 30):#ТВЕРЬ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ТВЕРЬ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septictver.png'
    septicSavePath = 'tverhead'
    hModel = 700
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 31):#ТОПАС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ТОПАС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septictopas.png'
    septicSavePath = 'topashead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 32):#ТОПОЛЬ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ТОПОЛЬ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septictopol.png'
    septicSavePath = 'topolhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 33):#ЭКОГРАНД
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЭКО-ГРАНД.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicecogrant.png'
    septicSavePath = 'ecograndhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTilel1/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
  if (i+1 == 34):#ЭНЕРГОБОКС
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/СЕПТИК ЭНЕРГОБОКС.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/septicenergobox.png'
    septicSavePath = 'energoboxhead'
    hModel = 600
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
        back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
        septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
        septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTitle1kes/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
          suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1
    hModel = 300
  if (i+1 == 1):#КЕССОН МЕТАЛЛ
    septicNamePath = '/content/drive/MyDrive/Colab Notebooks/namesForLabel1and3/КЕССОН МЕТАЛЛИЧЕСКИЙ.png'
    septicModelPath = '/content/drive/MyDrive/Colab Notebooks/septicModel/kessonmetall.png'
    septicSavePath = 'kessonmetallhead'
    for j in range(7):
      filename =  f'/content/drive/MyDrive/Colab Notebooks/label1/label1_{j+1}.png'
      with Image.open(filename) as back1:
          back1.load()
      filename = septicModelPath
      with Image.open(filename) as septicModel:
          septicModel.load()
      filename = septicNamePath
      with Image.open(filename) as septicName:
          septicName.load()
      back1.paste(septicModel, (wModel, hModel), septicModel)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      back1.paste(septicName, (wName, hName), septicName)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      numRand = random.randint(1,3)
      filename = f'/content/drive/MyDrive/Colab Notebooks/suppTitle1kes/suppTitleLab1_{numRand}.png'
      with Image.open(filename) as suppTitleLab1:
            suppTitleLab1.load()
      back1.paste(suppTitleLab1, (wTitle, hTitle), suppTitleLab1)
      back1.save(f'/content/drive/MyDrive/Colab Notebooks/result/head/{septicSavePath}{itr}.png')
      itr = itr + 1
    itr = 1

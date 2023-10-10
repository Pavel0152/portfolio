import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"image")#записываю изображние


def sp_noise(image,prob):#передаю пропорцию и изображение

    output = np.zeros(image.shape,np.uint8)#создаю нулевую матрицу shape - возвращает высоту ширину и каналы,uint8 - Целые числа в диапазоне от -128 по 127 (числа размером 1 байт).
    thres = 1 - prob # устанавливаю порог 

    for i in range(image.shape[0]):#проход по ширине
        for j in range(image.shape[1]):#проход по высоте
            rdn = random.random()
            if rdn < prob:# если порог больше сгенирированного n(0,1)
                output[i][j] = 0 # "солинка"
            elif rdn > thres:
                output[i][j] = 255 # максимальный оттенок цвета
            else:
                output[i][j] = image[i][j] #дефолт

    return output


def gasuss_noise(image, mean=0, var=0.001): # мат. ожидание и мат. отклоление    
    image = np.array(image/255, dtype=float) # приобразование к N от 0 до 1
    noise = np.random.normal(mean, var ** 0.5, image.shape) # создание единицы шума 
    out = image + noise # шум + изображние
    if out.min() < 0:
        low_clip = -1. #добавление минимального порога массива 
    else:
        low_clip = 0.#дефолт
    out = np.clip(out, low_clip, 1.0)#добовление границ выходного массива
    out = np.uint8(out*255)#возвращение в исходное состояние 

    return out

#    ,   0,02
out1 = sp_noise(img, prob=0.02)

# Добавить гауссовский шум, среднее значение 0, а дисперсия составляет 0,03
out2 = gasuss_noise(img, mean=0, var=0.03)


# Отображать изображение
titles = ['Оригиинал фото', 'Шум "Солённый перец"','Шум Гаусса']
images = [img, out1, out2]# массив с картинками 

plt.figure(figsize = (20, 15))#размеры фигур на окне plot
for i in range(3):# т.к 3 картинки
    plt.subplot(1,3,i+1)#3 картинки и счетчик
    plt.imshow(images[i])# картинка с индексом
    plt.title(titles[i])#названия
    plt.xticks([]),plt.yticks([])#вывод осей
plt.show()
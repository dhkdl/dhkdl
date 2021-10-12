from PIL import Image, ImageFilter
import os

# 해당 파일이 없다면 => 특정 파일을 생성하기 (os를 쓰지 않음)
# 일단 파일을 open => 예외 처리

# https://pillow.readthedocs.io/en/stable/reference/Image.html

targetRoot = "./target/"
sourceRoot = "./source/"

fileList = os.listdir(sourceRoot)

for fileName in fileList:
    sourceImg = Image.open(sourceRoot + fileName).convert("RGB")
    fName = fileName[:-len(fileName.split('.')[-1]) - 1]
    fileNum = 0

    width = sourceImg.width
    height = sourceImg.height

    widt = sourceImg.width
    heigh = sourceImg.height

    widthDiff = width * 20 // 100
    heighthDiff = height * 20 // 100
    widthDif = widt * 30 // 100
    heighthDif = heigh * 30 // 100
    
    os.mkdir(targetRoot + fName)
    targetDirectory = targetRoot + fName + "/"
    # targetDirectory = "./target/imageName/"

    for degree in range(-20, 21, 4):
        targetImg = sourceImg.rotate(degree, fillcolor=(255, 255, 255, 255))
        targetImg = targetImg.convert("RGB")
        targetImg.save(targetDirectory + f'{fileNum}.jpg', "JPEG")
        fileNum += 1

        targetImgBlur = targetImg.filter(filter=ImageFilter.BLUR)
        targetImgBlur.save(targetDirectory + f'{fileNum}.jpg', "JPEG")
        fileNum += 1

        targetImgCrop = targetImg.crop((widthDiff, heighthDiff, width-widthDiff, height-heighthDiff))
        targetImgCrop.save(targetDirectory + f'{fileNum}.jpg', "JPEG")
        fileNum += 1
        
        targetImgCrop = targetImg.crop((widthDif, heighthDif, widt-widthDif, heigh-heighthDif))
        targetImgCrop.save(targetDirectory + f'{fileNum}.jpg', "JPEG")
        fileNum += 1
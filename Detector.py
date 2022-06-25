import cv2
from cv2 import filterSpeckles
import numpy as np
import time
import os

class Detector:
  def __init__(self, videoPath, configPath, modelPath, classesPath):
    self.videoPath = videoPath
    self.configPath = configPath
    self.modelPath = modelPath
    self.classesPath = classesPath

    self.net = cv2.dnn_DetectionModel(self.modelPath, self.configPath)
    self.net.setInputSize(320, 320)
    self.net.setInputScale(1.0/127.5)
    self.net.setInputMean((127.5, 127.5, 127.5))
    self.net.setInputSwapRB(True)
  
    self.readClasses()

  def readClasses(self):
    with open(self.classesPath, 'r') as f:
      self.classesList = f.read().splitlines()

    self.classesList.insert(0, '__Background__')
    self.colorList = np.random.uniform(low = 0, high = 255, size=(len(self.classesList), 3))


  def onVideo(self):
    cap = cv2.VideoCapture(self.videoPath)

    if cap.isOpened() == False:
      print("Error opening file...")
      return

    (success, image) = cap.read()

    startTime = 0
    start = time.time() 
    stop = time.time()
    count_cups = 0

    while success:
      check = False
      currentTime = time.time()
      stop = time.time()
      fps = 1 / (currentTime - startTime)
      startTime = currentTime

      classLabelIDs, confidences, bboxs = self.net.detect(image, confThreshold = 0.4)

      bboxs = list(bboxs)
      confidences = list(np.array(confidences).reshape(1,-1)[0])
      confidences = list(map(float, confidences))

      bboxIdx = cv2.dnn.NMSBoxes(bboxs, confidences, score_threshold = 0.5, nms_threshold = 0.2)

      if len(bboxIdx) != 0:
        for i in range(0, len(bboxIdx)):
          bbox = bboxs[np.squeeze(bboxIdx[i])]
          classConfidence = confidences[np.squeeze(bboxIdx[i])]
          classLabelID = np.squeeze(classLabelIDs[np.squeeze(bboxIdx[i])])
          classLabel = self.classesList[classLabelID]
          classColor = [int(c) for c in self.colorList[classLabelID]]

          displayText = "{}:{:.2f}".format(classLabel, classConfidence)

          x, y,w, h = bbox

          cv2.rectangle(image, (x, y), (x+w, y+h), color = classColor, thickness = 1)
          cv2.putText(image, displayText, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 1, classColor, 2)

#          print(classLabel)
          if classLabel == 'bottle' or classLabel == 'wine glass' or classLabel == 'cup':
            count_cups = count_cups + 1
            if count_cups >= 5:
              check = True
              break
          
          stop = time.time()
  #        print(stop-start)

          if (int)(stop-start) >= 360:
            os.system("shutdown /s /t 1")
            os.system("shutdown now -h")


      cv2.putText(image, "FPS: " + str(int(fps)), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 1)      
      cv2.putText(image, "Remaining Time: " + str(int(360-(stop-start))), (10, 40), cv2.FONT_HERSHEY_PLAIN, 1.2, (0, 255, 0), 1)      
      cv2.imshow("Result", image)

      if check == True:
        break
      key = cv2.waitKey(1) & 0xFF
      # if key == ord("q"):
     #  break

      (success, image) = cap.read()

    cv2.destroyAllWindows()

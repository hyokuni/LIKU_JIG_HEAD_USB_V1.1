import pyaudio
import numpy as np
import threading

count =0
flagRun =0
def startTimer():
    global count
    #print("timer",str(count))
    
    timer = threading.Timer(1, startTimer) # n sec
    
    count = count + 1
    if(count <= 5):
        timer.start()
    else:
        timer.cancel()
        #print("timer stop")
        #off condition
        global flagRun
        flagRun = 1

#return Array over threshold number
def thdArray(thdNum,array):
    newArr = []
    for tmp in array:
        if(tmp > thdNum):
            newArr.append(tmp)
    #print(newArr)
    return newArr

#
def test_result(target,maxi_count):
    if(target > maxi_count):
        print("fail mic test")
    else:
        print("OK mic test")

#run Timer - n sec running
startTimer()

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            #print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
            pass

stream=p.open(format=pyaudio.paInt16,channels=4,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

peakdata1 = 0
peakdata2 = 0
peakthdMIC1 = 0
peakthdMIC2 = 0
peakthdMIC3 = 0
peakthdMIC4 = 0

#get mic data for Nsec
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    dataMIC1 = data[0::4]
    dataMIC2 = data[1::4]
    dataMIC3 = data[2::4]
    dataMIC4 = data[3::4]
    
    thdM1 =np.size( thdArray(30000,dataMIC1) )
    thdM2 =np.size( thdArray(30000,dataMIC2) )
    thdM3 =np.size( thdArray(30000,dataMIC3) )
    thdM4 =np.size( thdArray(30000,dataMIC4) )
    
    #print("threshold MIC count:",str(thdM1))
    
    maxMIC1 = np.max(dataMIC1)
    maxMIC2 = np.max(dataMIC2)
    maxMIC3 = np.max(dataMIC3)
    maxMIC4 = np.max(dataMIC4)

    peakMIC1 =np.average(np.abs(dataMIC1))* 2
    peakMIC2 =np.average(np.abs(dataMIC2))* 2
    peakMIC3 =np.average(np.abs(dataMIC3))* 2
    peakMIC4 =np.average(np.abs(dataMIC4))* 2
    
    bars1="#"*int(50*peakMIC1/2**16)
    bars2="#"*int(50*peakMIC2/2**16)
    bars3="#"*int(50*peakMIC3/2**16)
    bars4="#"*int(50*peakMIC4/2**16)

    #display max data 
    #if(maxMIC1 > peakdata1):
    #    peakdata1 = maxMIC1 
    #    print("mic1:",str(peakdata1))

    #if(maxMIC2 > peakdata2):
    #    peakdata2 = maxMIC2
    #    print("mic2:",str(peakdata2))

    if(thdM1 > peakthdMIC1):
        peakthdMIC1 = thdM1
        #print("peak cound MIC1:",str(peakthdMIC1))

    if(thdM2 > peakthdMIC2):
        peakthdMIC2 = thdM2
        #print("peak cound MIC2:",str(peakthdMIC2))

    if(thdM3 > peakthdMIC3):
        peakthdMIC3 = thdM3
        #print("peak cound MIC3:",str(peakthdMIC3))
        
    if(thdM4 > peakthdMIC4):
        peakthdMIC4 = thdM4
        #print("peak cound MIC4:",str(peakthdMIC4))

    #termination
    if flagRun:
        break

test_result(11,peakthdMIC1)
stream.stop_stream()
stream.close()
p.terminate()
#print("program end")
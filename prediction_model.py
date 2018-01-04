import numpy as np 
  
def loadRawDataSet(fileName):

    numFeat  = len(open(fileName).readline().split(',')) - 1  
    dataMat  = []  
    labelMat = []

    fr = open(fileName)

    for line in fr.readlines():  
        lineArr = []  
        curLine = line.strip().split(',')  
        for i in range(numFeat):  
            lineArr.append(float(curLine[i]))  
        dataMat.append(lineArr)  
        labelMat.append(float(curLine[-1])) 

    return dataMat,labelMat  
  
  
def regularize(xMat):				#regularize raw data by columns  
    inMat   = xMat.copy()  
    inMeans = np.mean(inMat,0)   	#calculate mean then subtract it off  
    inVar   = np.var(inMat,0)       #calculate variance then divide by it  
    inMat   = (inMat - inMeans)/inVar  
    return inMat  

def rssError(yArr, yHatArr):  
    return ((yArr - yHatArr) ** 2).sum() 
  
def stageWise(xArr, yArr, eps = 0.01, numIt = 100): 

    xMat  = np.mat(xArr)  
    yMat  = np.mat(yArr).T

    yMean = np.mean(yMat, 0)
    yVar  = np.var(yMat, 0)  
    yMat  = (yMat - yMean)

    xMat  = regularize(xMat)
    m,n   = np.shape(xMat) 

    returnMat = np.zeros((numIt,n))		# matrix used to store weights

    ws        = np.zeros((n,1))  
    wsTemp    = ws.copy()  
    wsBest    = ws.copy()

    for i in range(numIt):    
        lowestError = np.inf

        for j in range(n):

            for sign in [-1,1]:  
                wsTemp    =  ws.copy()  
                wsTemp[j] += eps * sign  
                yTest     = xMat * wsTemp  
                rssE      = rssError(yMat.A,yTest.A)  
                if rssE < lowestError:  
                    lowestError = rssE  
                    wsBest      = wsTemp

        ws = wsBest.copy()  
        returnMat[i,:] = ws.T

    return returnMat[-1]  
  
def MSE(target, predictions):
    squared_deviation = np.power(target - predictions, 2)
    return np.mean(squared_deviation)

if __name__ == '__main__':

	xArr_same,yArr_same = loadRawDataSet('raw_data_same_gender.csv') 
	xArr_diff,yArr_diff = loadRawDataSet('raw_data_diff_gender.csv')

	yMat_same  = np.mat(yArr_same).T
	yMean_same = np.mean(yMat_same, 0)

	yMat_diff  = np.mat(yArr_diff).T
	yMean_diff = np.mean(yMat_diff, 0)

	print "Dateset has been loaded successfully!"
	print "---------------------------------------\n"

	print "Begin training model."
	weight_same = stageWise(xArr_same,yArr_same,0.01,20000)
	weight_diff = stageWise(xArr_diff,yArr_diff,0.01,20000)
	print "Model has been trained successfully. "
	print "---------------------------------------\n"

	print "Evaluate the model:"
	print "-------------------\n"

	print "If these sample users chat with person of the same gender: "
	print "The predicted values are:"

	predictions_same = np.dot(regularize(np.mat(xArr_same)),weight_same)	+ yMean_same
	print predictions_same

	print "The true values are:"
	target_same 	 = np.mat(yArr_same)
	print target_same
	print "--------------------"
	print "MSE: " + str(MSE(predictions_same, target_same))
	print "---------------------------------------------------------------\n"

	print "If these sample users chat with person of the different gender: "
	print "The predicted values are:"

	predictions_diff = np.dot(regularize(np.mat(xArr_diff)),weight_diff)	+ yMean_diff
	print predictions_diff

	print "The true values are:"
	target_diff 	 = np.mat(yArr_diff)
	print target_diff
	print "--------------------"
	print "MSE: " + str(MSE(predictions_diff, target_diff))
	print "---------------------------------------------------------------\n"





    


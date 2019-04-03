import sys

orig_stdout = sys.stdout
f = open('../trainingCode/positive_samples.txt', 'a+')
sys.stdout = f


for i in range(1,421):
 
 if(i>99):
  i=str(i)	
  print("positiveSamples/carsgraz_"+ i + ".bmp")
 elif(i>9 & i<100):
  i=str(i)	
  print("positiveSamples/carsgraz_0"+ i + ".bmp")
 else:
  i=str(i)	
  print("positiveSamples/carsgraz_00"+ i + ".bmp")

sys.stdout = orig_stdout
f.close()  

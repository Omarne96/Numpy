## First of all you have to install numpy framework
## go to your Terminal and type this commands :
## pip install numpy
## if you have any error check the pip update

## then import the numpy library
import numpy as np
from io import StringIO

## to make a simple array
## dtype which allows to you to specify your types
a=np.array([[1,2,3,0,4],[4,4,0,4,4],[1,2,3,0,4]], dtype="int16" )
print(a)

## get the dimention
print(a.ndim) 

##get shape:
print(a.shape) ## will gives you : (num of rows , num in each array)

## get the type:
print(a.dtype)
print(a.itemsize) ## will gives you the number of bits
print(a.size)  ## will gives you the total size 
print(a.nbytes) ## will gives you the total number of bytes


b=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
##get a specific element [r,c]:
##-- Remember that python count from 0 --##

print(b[1,4]) ## will gives you the number 11
print(b[1,-2]) ## will gives you the number 11 too

print(b[0,:]) ## get a specific row:
print(b[:,2]) ## get a specific column:

## get lot of elements [startindex: endindex : stepsize] 
## or [num of row,startindex: endindex : stepsize]
print("--------------------------")
print(b[1,0:-1:2]) 

c=np.array([[1,2,3,4,5],[5,4,3,2,1]])
## change a value in a array
## b[r,c]= the value
c[0,0]=99
## to chane whole column |
c[:,2]=6
c[:,3]=[55,66] ## with different values
print(c)


########################################################
#####################  3D Examples #####################
########################################################
print("-------------- 3D Examples --------------")
k=np.array([ [[1,2],[3,4]] , [[6,7],[8,9]] ])
## get a spesific element ( work outside in ): 
## this is outside [[1,2],[3,4]] , [[6,7],[8,9]]
## [number of array , num of row , num of column]

print(k[1,1,1]) ## This will gives you the number 9
print(k[0,1,1]) ## This will gives you the number 4
print(k[0,0,:]) ## This will gives you the number [1 2]
print(k[:,0,:]) ## This will gives you the number [1 2] and [6 7]
print(k[:,1,:]) ## This will gives you the number [3 4] and [8 9]

### Replace  ###
k[:,1,:]=[[11,22],[44,55]]
print(k[:,1,:])
#print(k)


#################################################
print("----------------------------------------")
#################################################
## all 0s matrix :
print(np.zeros(5))
print(np.zeros((2,3)))        ## 2D matrix of zero
print(np.zeros((2,3,3)))      ## 3D matrix of zero
print(np.zeros((2,3,3,2)))    ## 4D matrix of zero

## all 1s matrix :
print(np.ones((3,2,2),dtype="int32"))  ## 
print("--------------------------------")

## Any other numbers: np.full(shape,vaue) you can use c.shape too here
print(np.full((2,2),44,dtype="float32"))
print(np.full_like(c,5)) ## shape like c 

################# Random #######################
################################################
## 1 - decimal numbers
print(np.random.rand(4,2,3))
print("--------------------------------")
print(np.random.random_sample(c.shape))
print("--------------------------------")
## 2 - integer  number less then(x)
print(np.random.randint(5))
print(np.random.randint(5,size=(4,4)))
print(np.random.randint(-5,5,size=(4,4)))
print("--------------------------------")
################################################
## identity matrix ( the principal diagonal = 1 ):
print(np.identity(5))
##################################################
## Repeat an array 
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=1) #axis=0 normal ,axis=1 repeat 111222333
print(r1)
####################################################################
############################# Quiz  ################################
print("------------------------------")
ok=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
ok[1:-1,1:-1]=z ## or ok[1:4,1:4]=z

print(ok)
print("------------------------------")
#####################################################################
#####################################################################
################ Be Carful when you copy an array  ##################
################     use the .copy() function      ##################
#####################################################################
#####################################################################
 
## Mathemetics :
###############
f=np.array([1,2,3,4,5])
#f+=2
#f-=2
#f*=2
#f/2
#f**=2
print(f)
print(np.sin(f))
print(np.cos(f))  
print(np.tan(f))
####################################################################
######################### Linear Algebra ###########################
c=np.ones((2,3))
v=np.full((3,2),2)
w=np.matmul(c,v)
print(w)

## Find determinant :
q=np.identity(3)
print(np.linalg.det(q))

####################################################################
########################### Statistics #############################
p=np.array([[1,2,3],[4,5,6]])
print(np.max(p)) ## np.min(p)
print(np.max(p,axis=1)) ## will gives you max in first row and second row
print(np.max(p,axis=0)) ## will gives you max of column
print(np.sum(p,axis=1)) ## axis=0 will gives you sum of comlumn
print("-------------------------")

## reorganizing arrays
t=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
tt=t.reshape(4,3) ## change the shape of an array
print(tt)

## Vertically stacking Vectors :
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.vstack([v1,v2,v2,v2,v1])  ## Merge Vertically
print(v3)
## Horizantal stacking Vectors :
k1=np.zeros([2,2])
k2=np.ones([2,4])
k3=np.hstack([k1,k2])
v4=np.hstack([v1,v1,v2])   ## Merge Horizantal 
print(v4)
print(k3)
print("-----------------------------------------")

#########################################################
################### miscellaneous #######################
#########################################################

############# Load data from file #######################
filedata=np.genfromtxt('data.txt',delimiter=",")
filedata.astype('int32')
print(filedata)
print("------------------------------------------------")

########## boolean masking and advanced indexing ########
print(filedata >= 50)
print(filedata[filedata >= 44])
print(np.any(filedata > 50, axis=1))            #, axis=1
print(np.all(filedata > 50, axis=1))
print("***************************************************")
vaar=(~((filedata > 50) &( filedata <60)))    ## ~ not
print(vaar)
print("***************************************************")



## You can index with a list in Numpy
new_var=np.array([10,14,0,74,58,17,222,7785,1452])
print(new_var[[2,5,-1]])














## in the last check itemsezie if bits or bytes 
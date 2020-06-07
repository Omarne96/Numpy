


                ###############################################################
                ##                                                           ##
                ## Here you are going to learn NumPy Framework For Beginners ##
                ##               https://github.com/Omarne96                 ##
                ##                  Instagram : Omar_ne16                    ##
                ###############################################################

'''
        First of all you have to install numpy framework
        go to your Terminal and type this commands :
        pip3 install numpy
        if you have any error check the pip update or use pip3
'''
## Then import the numpy library
import numpy as np


## To make a simple array :
###########################

a=np.array([[1,2,3,0,4],[4,4,0,4,4],[1,2,3,0,4]], dtype="int16" )
        ### dtype which allows to you to specify your types ###

## get the dimention :
#####################
a.ndim

##get shape:
############
a.shape          ## will gives you : (num of rows , num in each array)

## get the type:
################

a.dtype          ## will gives you data type of all colums you have in your data
a.itemsize       ## will gives you the number of bits
a.size           ## will gives you the total size 
a.nbytes         ## will gives you the total number of bytes



##get a specific element [r,c]:
###############################
b=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
##--- Remember that python count from 0 ---##

b[1,4]             ## will gives you the number 11
b[1,-2]            ## will gives you the number 11 too

b[0,:]             ## get a specific row:
b[:,2]             ## get a specific column:

## get lot of elements [startindex: endindex : stepsize] 
## or [num of row,startindex: endindex : stepsize]
b[1,0:-1:2]

c=np.array([[1,2,3,4,5],[5,4,3,2,1]])
## change a value in a array
## b[r,c]= the value
c[0,0]=99
## to chane whole column |
c[:,2]=6
c[:,3]=[55,66] ## with different values



    ########################################################################
    #############################  3D Examples #############################
    ########################################################################




## Get a spesific element ( work outside in ):
##############################################

k=np.array([ [[1,2],[3,4]] , [[6,7],[8,9]] ])
## This is outside [[1,2],[3,4]] , [[6,7],[8,9]]
## [number of array , num of row , num of column]

k[1,1,1]                    ## This will gives you the number 9
k[0,1,1]                    ## This will gives you the number 4
k[0,0,:]                    ## This will gives you the number [1 2]
k[:,0,:]                    ## This will gives you the number [1 2] and [6 7]
k[:,1,:]                    ## This will gives you the number [3 4] and [8 9]


### Replace  ###
################

k[:,1,:]=[[11,22],[44,55]]
k[:,1,:]




#################################################
## all 0s matrix :
np.zeros(5)
np.zeros((2,3))                     ## 2D matrix of zero
np.zeros((2,3,3))                   ## 3D matrix of zero
np.zeros((2,3,3,2))                 ## 4D matrix of zero


## all 1s matrix :
##################
np.ones((3,2,2),dtype="int32")            ## Onse matrix with ??


## Any other numbers:
#####################    np.full(shape,vaue) you can use c.shape too here  

np.full((2,2),44,dtype="float32")
np.full_like(c,5)                          ## shape like c 


            ################################################################
            ########################## Random ##############################
            ################################################################


## 1 - decimal numbers :
########################

np.random.rand(4,2,3)
np.random.random_sample(c.shape)



## 2 - integer  number less then(x):
####################################
np.random.randint(5)
np.random.randint(5,size=(4,4))
np.random.randint(-5,5,size=(4,4))



## identity matrix ( the principal diagonal = 1 ):
##################################################
np.identity(5)



## Repeat an array :
####################

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=1) #axis=0 normal ,axis=1 repeat 111222333





            ####################################################################
            ############################# Quiz  ################################
            ####################################################################
ok=np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9
ok[1:-1,1:-1]=z                ## You can use   ok[1:4,1:4]=z







            #####################################################################
            #####################################################################
            ################ Be Carful when you copy an array  ##################
            ################     use the .copy() function      ##################
            #####################################################################
            #####################################################################
 





## Mathemetics :
################

f=np.array([1,2,3,4,5])
#f+=2
#f-=2
#f*=2
#f/2
#f**=2

np.sin(f)             ## SIN
np.cos(f)             ## COS
np.tan(f)             ## TAN


                ####################################################################
                ######################### Linear Algebra ###########################
                ####################################################################

c=np.ones((2,3))
v=np.full((3,2),2)
w=np.matmul(c,v)


## Find determinant :
#####################
q=np.identity(3)
np.linalg.det(q)



                ####################################################################
                ########################### Statistics #############################
                ####################################################################

p=np.array([[1,2,3],[4,5,6]])
np.max(p)                        ## np.min(p)
np.max(p,axis=1)                 ## will gives you max in first row and second row
np.max(p,axis=0)                 ## will gives you max of column
np.sum(p,axis=1)                 ## axis=0 will gives you sum of comlumn
 


## reorganizing arrays :
########################

t=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
tt=t.reshape(4,3) ## change the shape of an array

## Vertically stacking Vectors :
################################

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.vstack([v1,v2,v2,v2,v1])     ## Merge Vertically


## Horizantal stacking Vectors :
################################

k1=np.zeros([2,2])
k2=np.ones([2,4])
k3=np.hstack([k1,k2])
v4=np.hstack([v1,v1,v2])            ## Merge Horizantal 
 
 




                #########################################################
                ################### miscellaneous #######################
                #########################################################


############# Load data from file #######################

filedata=np.genfromtxt('data.txt',delimiter=",")
filedata.astype('int32')



## Boolean masking and advanced indexing :
##########################################

filedata >= 50
filedata[filedata >= 44]
np.any(filedata > 50, axis=1)                 # axis=1
np.all(filedata > 50, axis=1)

vaar=(~((filedata > 50) &( filedata <60)))    ## ~ not



## You can index with a list in Numpy :
#######################################

new_var=np.array([10,14,0,74,58,17,222,7785,1452])
new_var[[2,5,-1]]






            ###############################################################
            ##                                                           ##
            ##    to Learn more about NumPy check W3SCHOOLS WEBSITE      ##
            ##     https://www.w3schools.com/python/numpy_intro.asp      ##
            ##                                                           ##
            ###############################################################







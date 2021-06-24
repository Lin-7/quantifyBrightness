from utils import *

data_type = 'data1'
dic = 'brightness/pic/' + data_type 
save_dic = 'brightness/GreyPic/' + data_type
if not os.path.exists(save_dic):
    os.makedirs(save_dic)
pics = readAllPictures(dic)
for pic in pics:
    hist(pic, save_dic)
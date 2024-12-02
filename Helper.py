from pydantic import BaseModel
from Item import Item
import math
purchaseList={}
class Product(BaseModel):
    retailer:str
    purchaseDate:str
    purchaseTime:str
    items:list[Item]
    total:str
def calculate_points(product):
    total_points=0
    total_points=getRetailerPoints(product,total_points)
    total_points=getTotalCostPoints(product,total_points)
    total_points=getItemPairPoints(product,total_points)
    total_points=getDatePoints(product,total_points)
    total_points=getItemDetailPoints(product,total_points)
    total_points=getTimePoints(product,total_points)
    return total_points
def getDatePoints(product,total_points):
    date_list=product.purchaseDate.split('-')
    if (int(date_list[2])%2)==1:
        total_points=total_points+6
    return total_points
def getItemPairPoints(product,total_points):
    item_pairs=len(product.items)//2
    total_points=total_points+(5*item_pairs)
    return total_points
def getTotalCostPoints(product,total_points):
    total=float(product.total)
    if (total%.25)==0:
        total_points=total_points+25
    if (total%1.00)==0:
        total_points=total_points+50
    return total_points
def getItemDetailPoints(product,total_points):
    for item in product.items:
        trim_descrip=item.shortDescription.strip()
        if len(trim_descrip)%3==0:
            amount_added=math.ceil(float(item.price)*.2)
            total_points=total_points+amount_added
    return total_points
def getTimePoints(product,total_points):
    time_list=product.purchaseTime.split(':')
    if int(time_list[0])>14 and int(time_list[0]) < 16:
        total_points=total_points+10
    elif int(time_list[0])==14:
        if int(time_list[1])>0:
            total_points=total_points+10
    return total_points
def getRetailerPoints(product,total_points):
    retailer=product.retailer
    clean_retailer=''.join(char for char in retailer if char.isalnum())
    total_points=total_points+len(clean_retailer)
    return total_points

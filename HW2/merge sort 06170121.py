#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def merge_sort(self, nums):
        if len(nums)<2:#當nums於2時
            return nums#回傳nums
        else:
            left=nums[:len(nums)//2] #左邊數值
            right=nums[len(nums)//2:]#右側數值
            return merge(mergeSort(left), mergeSort(right))#回傳左右數值
    def merge(self,left,right):
        a=0#紀錄left的位置
        b=0#紀錄right的位置
        c=[]#用來放置比較後的數值
        while a<len(left) and b<len(right):#當2個list的值都沒跑完時
            if left[a]<=right[b]:
                c.append(left[a])#把left第a個值存到c裡
                a+=1#因為左邊第一個排序完成，所以換第二個
            else:  
                c.append(right[b])#把right第b個值存到c裡
                b+=1#因為右邊第一個排序完成，所以換第二個
        while a<len(left):#左方有值時執行的while迴圈
            c.append(left[a])#將左方執行結果加進c裡面
            a+=1
        while b<len(right)::#右方有值時執行的while迴圈
            c.append(right[b];#將右方執行結果加進c裡面
        return c#回傳c


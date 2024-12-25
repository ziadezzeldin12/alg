def counting_sort(arr):
    max_value=max(arr)# عشان نعرف اكبر عنصر فى المصفوفه عشان نعرف اخر عنصر
   
    counting = [0] * (max_value + 1)  # بنعمل مصفوفه فاضيه عشان نرتب فيها العناصر وزودنا واحد عشان نوصل لاكبر عنصر 
    
    for num in arr:# هنا بنعدى على كل العناصر فى المصفوفه والعنصر الموجود نحسب موجود كام مره ولو مش موجود 0
        counting[num] += 1
        
    for i in range(1, len(counting)): # عشان خطوه ال PREFIX
        counting[i] += counting[i - 1]
        
        output = [0] * len(arr) # عشان نحط العناصر بعد ما اترتبت
    
    for num in reversed(arr): # بنشمى على المصفوفه من الاول للاخر عشان نحافظ على ال stable sort
        output[counting[num] - 1] = num
        counting[num] -= 1 # عشان نقلل الindex ونروح للعنصر الى قبله 
    
    return output



user_input = input("")
arr = list(map(int, user_input.split(','))) 
sorted_arr = counting_sort(arr)


print("", sorted_arr)
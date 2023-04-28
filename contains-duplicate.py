def list_duplicates(nums):

    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)


list_duplicates(nums = input("Lütfen bir sayı giriniz:"))


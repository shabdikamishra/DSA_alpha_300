def removeDuplicatesII(nums: list[int]) -> int:
    
    if len(nums) <= 2:
        return len(nums)
    
    write_ptr = 2
    
    for read_ptr in range(2, len(nums)):
        if nums[read_ptr] != nums[write_ptr - 2]:
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
            
    return write_ptr
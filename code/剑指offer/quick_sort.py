class quick_sort(object):

    def sort(self, list):
        self.sort_handle(list, 0, len(list) - 1)
        return list
    
    def sort_handle(self, list, left_index, right_index):
        if left_index >= right_index:
            return
        mid_index = left_index
        change_index = mid_index + 1
        while change_index <= right_index:
            if list[change_index] >= list[mid_index]:
                change_index += 1
            else:
                tmp = list[mid_index + 1]
                list[mid_index + 1] = list[change_index]
                list[change_index] = tmp

                tmp_mid = list[mid_index]
                list[mid_index] = list[mid_index + 1]
                list[mid_index + 1] = tmp_mid
                mid_index += 1
                change_index = mid_index + 1

        self.sort_handle(list, left_index, mid_index)
        self.sort_handle(list, mid_index + 1, right_index)

s = quick_sort()
list = [10, 2, 11, 3, 5, 4, 7, 2, 1, 3, 6, 2, 9, 11, 10, 7]
s.sort(list)
print(list)

        
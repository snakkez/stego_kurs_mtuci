from itertools import chain


def getsubarray(x1, y1, x2, y2, array):
    return [item[x1:x2] for item in array[y1:y2]]


def slice_into_subarrays(array, slice_dim=8):
    dim_y = len(array)
    dim_x = len(array[0])
    sliced = [[getsubarray(x, y, x+slice_dim, y+slice_dim, array) for x in range(0, dim_x, slice_dim)]
              for y in range(0, dim_y, slice_dim)]
    return sliced


def merge_from_subarrays(subarrays, slice_dim=8):
    dim_y_s = len(subarrays)
    dim_x_s = len(subarrays[0])

    unsliced = []
    for s_y in range(dim_y_s):
        for s_d in range(slice_dim):
            for s_x in range(dim_x_s):
                unsliced.append(subarrays[s_y][s_x][s_d])

    unsliced_rowed = [unsliced[i:i+dim_x_s] for i in range(0, len(unsliced), dim_x_s)]
    array = [list(chain.from_iterable(row)) for row in unsliced_rowed]
    return array

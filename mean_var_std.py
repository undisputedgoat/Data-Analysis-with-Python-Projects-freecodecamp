import numpy as np

np.set_printoptions(legacy='1.25') #because I don't want to see np.float64(x) in the output
# axis1 = columns
# axis2 = rows

calculations = {}

def calculate(data_list):
    try:
        data_list = np.array(data_list)
        data_array = data_list.reshape(3, 3)
        columns_mean = []
        rows_mean = []
        columns_var = []
        rows_var = []
        columns_std = []
        rows_std = []
        columns_max = []
        rows_max = []
        columns_min = []
        rows_min = []
        columns_sum = []
        rows_sum = []

        for x in range(3):
            columns_value = data_array[:, x]
            rows_value = data_array[x]

            columns_mean.append(columns_value.mean())
            rows_mean.append(rows_value.mean())
            calculations['mean'] = [columns_mean, rows_mean]

            columns_var.append(columns_value.var())
            rows_var.append(rows_value.var())
            calculations['variance'] = [columns_var, rows_var]

            columns_std.append(columns_value.std())
            rows_std.append(rows_value.std())
            calculations['standard deviation'] = [columns_std, rows_std]

            columns_max.append(columns_value.max())
            rows_max.append(rows_value.max())
            calculations['max'] = [columns_max, rows_max]

            columns_min.append(columns_value.min())
            rows_min.append(rows_value.min())
            calculations['min'] = [columns_min, rows_min]

            columns_sum.append(columns_value.sum())
            rows_sum.append(rows_value.sum())
            calculations['sum'] = [columns_sum, rows_sum]

        calculations['mean'].append(float(data_list.mean()))
        calculations['variance'].append(float(data_list.var()))
        calculations['standard deviation'].append(float(data_list.std()))
        calculations['max'].append(float(data_list.max()))
        calculations['min'].append(float(data_list.min()))
        calculations['sum'].append(float(data_list.sum()))

        return calculations

    except ValueError:
        print("You have to enter a list with 9 values.")

# for key, value in calculations.items():
#     print(f''{key}': {value}')